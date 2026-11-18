"""第002节：本地 Notebook 状态与预测问题。
依赖 torch；运行 python lessons/002/lesson.py。
CPU、种子42、4个合成样本；无外部输入和数据下载。
输出标签、形状、旧/新预测误差、四个候选模型的MSE和PASS。
"""
# 1. 准备可复现的本机CPU环境
import torch

torch.manual_seed(42)
torch.set_num_threads(1)
device = torch.device("cpu")
print("PyTorch", torch.__version__, "device", device)


# 2. 数据、模型与损失
# 只在本单元格修改目标规则；修改后需要重跑下游单元格。
TARGET_WEIGHT = 2.0
TARGET_BIAS = 1.0
x = torch.tensor([0., 1., 2., 3.], device=device).reshape(-1, 1)
y = TARGET_WEIGHT * x + TARGET_BIAS


def predict(features, weight, bias):
    return weight * features + bias


def mse(predictions, labels):
    # 避免(4,)和(4,1)广播，掩盖预测问题的错误。
    assert predictions.shape == labels.shape
    return torch.mean((predictions - labels) ** 2).item()


print("shapes", tuple(x.shape), tuple(y.shape))
print("labels", y.flatten().tolist())


# 3. 已保存的预测不会因参数重赋值自动变化
weight, bias = 1.0, 0.0
saved_prediction = predict(x, weight, bias)
saved_copy = saved_prediction.clone()
old_loss = mse(saved_prediction, y)
weight, bias = 2.0, 1.0
stale_loss = mse(saved_prediction, y)
fresh_prediction = predict(x, weight, bias)
fresh_loss = mse(fresh_prediction, y)
assert torch.equal(saved_prediction, saved_copy)
assert old_loss == stale_loss
print(f"before {old_loss:.6f}; stale {stale_loss:.6f}; recomputed {fresh_loss:.6f}")


# 4. 在同一数据上比较候选模型
# 这里只比较预设模型；没有执行梯度训练，也没有评估真实泛化。
candidates = [
    ("constant_mean", 0.0, y.mean().item()),
    ("x", 1.0, 0.0),
    ("2x+1", 2.0, 1.0),
    ("3x-1", 3.0, -1.0),
]
scores = []
for name, candidate_weight, candidate_bias in candidates:
    value = mse(predict(x, candidate_weight, candidate_bias), y)
    scores.append((name, value))
    print(f"{name}: MSE={value:.6f}")
best_name, best_loss = min(scores, key=lambda item: item[1])
assert best_loss < 1e-6
print("best", best_name)
print("PASS")
