"""第004节：概念复习与张量创建、形状排错。
依赖torch。运行python lessons/004/lesson.py。
CPU、种子42；所有输入均在文件中，无外部数据。
输出张量元信息、预期错误的捕获结果、修复后的MSE与PASS。
"""
# 1. 创建与描述张量
import torch

torch.manual_seed(42)
torch.set_num_threads(1)
device = torch.device("cpu")


def describe(name, value):
    print(f"{name}: shape={tuple(value.shape)}, ndim={value.ndim}, "
          f"numel={value.numel()}, dtype={value.dtype}, device={value.device}")


scalar = torch.tensor(5., dtype=torch.float32, device=device)
vector = torch.arange(12, dtype=torch.float32, device=device)
matrix = vector.reshape(3, 4)
cube = torch.zeros((2, 3, 4), dtype=torch.float32, device=device)
ones = torch.ones((2, 2), dtype=torch.float32, device=device)
class_ids = torch.tensor([0, 1, 2], dtype=torch.int64, device=device)
print("PyTorch", torch.__version__)
for name, value in [("scalar", scalar), ("vector", vector), ("matrix", matrix),
                    ("cube", cube), ("ones", ones), ("class_ids", class_ids)]:
    describe(name, value)
assert scalar.ndim == 0 and scalar.numel() == 1
assert matrix.ndim == 2 and matrix.numel() == 12
assert cube.numel() == 24


# 2. 元素数量与reshape
print("matrix values", matrix.tolist())
assert torch.equal(vector, matrix.reshape(-1))
assert torch.equal(matrix, vector.reshape(-1, 4))
# 先预测错误原因，再运行。异常被捕获，整个学习文件仍可执行完成。
try:
    vector.reshape(3, 5)
except RuntimeError:
    print("invalid reshape rejected: 12 elements cannot fill (3, 5)")
else:
    raise AssertionError("Expected incompatible reshape to fail")
print("reshape fixed", tuple(vector.reshape(3, 4).shape))


# 3. 调试预测与标签的形状
def checked_mse(predictions, labels):
    if predictions.shape != labels.shape:
        raise ValueError("Prediction and label shapes must match")
    return torch.mean((predictions - labels) ** 2).item()


labels = torch.tensor([1., 2., 3.], dtype=torch.float32, device=device)
predictions = (labels + 1).reshape(-1, 1)
print("prediction shape", tuple(predictions.shape), "label shape", tuple(labels.shape))
# 此处只展示隐式扩展的结果形状；完整广播规则在005节展开。
print("unchecked difference shape", tuple((predictions - labels).shape))
try:
    checked_mse(predictions, labels)
except ValueError:
    print("shape mismatch rejected")
else:
    raise AssertionError("Expected shape guard to reject mismatched shapes")
fixed_labels = labels.reshape(-1, 1)
correct_loss = checked_mse(predictions, fixed_labels)
assert abs(correct_loss - 1.0) < 1e-6
print(f"fixed MSE {correct_loss:.6f}")


# 4. 结束前再核对元信息
assert matrix.dtype == torch.float32
assert class_ids.dtype == torch.int64
assert predictions.shape == fixed_labels.shape == (3, 1)
assert predictions.device == fixed_labels.device
print("PASS")
