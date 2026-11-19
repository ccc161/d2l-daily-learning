"""第003节：回归、分类与任务定义。
依赖torch。运行python lessons/003/lesson.py。
CPU、种子42，6个合成输入，无需外部数据或云服务。
输出标签、形状、MSE、BCE、准确率、概率与PASS。
"""
# 1. 本机CPU与两种标签
import torch

torch.manual_seed(42)
torch.set_num_threads(1)
device = torch.device("cpu")
# x为6个样本，每个样本1个特征。无需下载或读写数据。
x = torch.tensor([-2., -1., 0., 1., 2., 3.], device=device).reshape(-1, 1)
regression_target = 2 * x + 1
LABEL_THRESHOLD = 1.0
class_target = (x >= LABEL_THRESHOLD).float()
print("PyTorch", torch.__version__, "device", device)
print("shapes", tuple(x.shape), tuple(regression_target.shape), tuple(class_target.shape))
print("regression labels", regression_target.flatten().tolist())
print("class labels", class_target.flatten().tolist())


# 2. 连续值预测与MSE
# 比较预设模型，今天不进行梯度训练。
rough_prediction = 2 * x
exact_prediction = 2 * x + 1
assert rough_prediction.shape == regression_target.shape
mse = torch.nn.MSELoss()
rough_mse = mse(rough_prediction, regression_target).item()
exact_mse = mse(exact_prediction, regression_target).item()
print(f"regression MSE rough={rough_mse:.6f}, exact={exact_mse:.6f}")
assert abs(rough_mse - 1.0) < 1e-6
assert exact_mse < 1e-6


# 3. 二元类别、logit与交叉熵
def binary_metrics(logits, labels):
    assert logits.shape == labels.shape
    # BCEWithLogitsLoss接收原始分数，内部处理sigmoid，勿提前调用sigmoid。
    loss = torch.nn.BCEWithLogitsLoss()(logits, labels).item()
    predictions = (logits >= 0).float()
    accuracy = (predictions == labels).float().mean().item()
    return loss, accuracy, predictions


for center in [0.5, 1.5]:
    logits = x - center
    loss, accuracy, predictions = binary_metrics(logits, class_target)
    print(f"center={center:.1f}: BCE={loss:.6f}, accuracy={accuracy:.6f}")
    print("predicted classes", predictions.flatten().tolist())
    assert torch.isfinite(torch.tensor(loss))


# 4. 分数、概率和硬分类不是同一个量
logits = x - 0.5
probabilities = torch.sigmoid(logits)
_, _, predicted_classes = binary_metrics(logits, class_target)
assert torch.equal(predicted_classes, (probabilities >= 0.5).float())
print("probabilities", [round(value, 4) for value in probabilities.flatten().tolist()])
print("PASS")
