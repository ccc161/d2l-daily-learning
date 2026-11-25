"""第009节：偏导、梯度、链式法则与自动求导。
依赖torch。运行python lessons/009/lesson.py。
本机CPU、种子42；自动求导用float32，差分核对用CPU float64。
内嵌小张量，无外部文件或下载。输出计算图属性、梯度与PASS。
"""
# 1. 叶子张量与前向计算图
import torch

torch.manual_seed(42)
torch.set_num_threads(1)
device = torch.device("cpu")
x = torch.tensor([2., 3.], dtype=torch.float32, device=device, requires_grad=True)
# a=x[0]、b=x[1]，a通过乘法与加法两条路径影响s。
product = x[0] * x[1]
s = product + x[0]
loss = s ** 2
print("PyTorch", torch.__version__, "device", device)
print("leaf", x.is_leaf, "requires_grad", x.requires_grad, "grad before", x.grad)
print("values", product.item(), s.item(), loss.item())
print("shapes", tuple(x.shape), tuple(s.shape), tuple(loss.shape))
print("graph recorded", loss.grad_fn is not None)
assert x.grad is None and loss.item() == 64


# 2. 链式法则与反向求导
# s=a(b+1)，dL/da=2s(b+1)，dL/db=2sa。
loss.backward()
expected = torch.tensor([64., 32.], dtype=torch.float32, device=device)
assert x.grad is not None and x.grad.shape == x.shape
assert torch.allclose(x.grad, expected)
assert torch.equal(x, torch.tensor([2., 3.], device=device))
print("autograd gradient", x.grad.tolist())
print("input after backward", x.tolist())


# 3. 用中心差分逐坐标核对
def value_at(point):
    inner = point[0] * point[1] + point[0]
    return inner ** 2


# 差分核对沿用008节CPU float64方案，与前向图分开计算。
point = torch.tensor([2., 3.], dtype=torch.float64, device="cpu")
h = 1e-5
numerical = []
for index in range(point.numel()):
    step = torch.zeros_like(point)
    step[index] = h
    estimate = (value_at(point + step) - value_at(point - step)) / (2 * h)
    numerical.append(estimate.item())
numerical = torch.tensor(numerical, dtype=torch.float64)
assert torch.allclose(numerical, expected.cpu().to(torch.float64), atol=1e-6, rtol=0)
print("finite difference", [round(value, 6) for value in numerical.tolist()])


# 4. 先把逐项结果合成标量目标
# 使用新叶子张量和新计算图，避免复用已反向计算的图。
z = torch.tensor([-1., 0., 2.], dtype=torch.float32, device=device, requires_grad=True)
terms = z ** 2 + 3 * z
total = terms.sum()
total.backward()
assert terms.shape == (3,) and total.shape == ()
assert z.grad is not None and z.grad.shape == (3,)
assert torch.allclose(z.grad, 2 * z + 3)
print("terms", terms.tolist(), "total", total.item())
print("sum gradient", z.grad.tolist())
print("PASS")
