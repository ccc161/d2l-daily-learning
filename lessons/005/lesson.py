"""第005节：索引、广播与共享存储。
依赖torch。运行python lessons/005/lesson.py。
CPU、种子42，小型合成张量，无数据下载或外部输入。
输出切片、广播结果、视图/副本变化与PASS。
"""
# 1. 索引、切片与按元素计算
import torch

torch.manual_seed(42)
torch.set_num_threads(1)
device = torch.device("cpu")
X = torch.arange(12, dtype=torch.float32, device=device).reshape(3, 4)
row = X[1]
row_kept = X[1:2]
block = X[:2, 1:3]
print("PyTorch", torch.__version__, "device", device)
print("X", X.tolist())
print("row shapes", tuple(row.shape), tuple(row_kept.shape))
print("last value", X[-1, -1].item())
print("block", block.tolist())
print("doubled first row", (X * 2)[0].tolist())
assert row.shape == (4,) and row_kept.shape == (1, 4)
assert torch.equal(block, torch.tensor([[1., 2.], [5., 6.]], device=device))
assert (X * X).shape == X.shape


# 2. 逐轴判断广播
feature_offsets = torch.tensor([10., 20., 30., 40.], device=device)
shifted = X + feature_offsets
column = torch.tensor([[100.], [200.], [300.]], device=device)
row_offsets = torch.tensor([1., 2., 3., 4.], device=device)
grid = column + row_offsets
print("feature broadcast", tuple(shifted.shape), shifted.tolist())
print("outer broadcast", tuple(grid.shape), grid.tolist())
assert grid.shape == (3, 4)
assert grid[2, 3].item() == 304
try:
    X + torch.ones(3, device=device)
except RuntimeError:
    print("incompatible broadcast rejected: (3, 4) and (3,)")
else:
    raise AssertionError("Expected trailing axes 4 and 3 to conflict")


# 3. 别名、基本切片与clone
base = torch.arange(6, dtype=torch.float32, device=device).reshape(2, 3)
alias = base
view = base[:, 1:]
independent = view.clone()
view[0, 0] = 99
print("base after view edit", base.tolist())
print("clone after view edit", independent.tolist())
assert alias is base
assert base[0, 1].item() == 99
assert independent[0, 0].item() == 1


# 4. 新结果与原地修改
before = base.clone()
rebound = base + 10
assert torch.equal(base, before)
alias.add_(1)
print("base after in-place add", base.tolist())
print("view after in-place add", view.tolist())
print("new result kept", rebound.tolist())
assert base[0, 1].item() == 100
assert view[0, 0].item() == 100
assert independent[0, 0].item() == 1
assert rebound[0, 1].item() == 109
print("PASS")
