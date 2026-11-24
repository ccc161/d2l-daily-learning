"""第008节：范数、线性变换与有限差分。
依赖torch。运行python lessons/008/lesson.py。
CPU、float64、种子42，小型内嵌向量与标量，无外部文件或下载。
输出范数、变换结果、差分表与小步长观察，最后PASS。
"""
# 1. 用不同范数测量同一向量
import torch

torch.manual_seed(42)
torch.set_num_threads(1)
device = torch.device("cpu")
dtype = torch.float64
v = torch.tensor([3., -4.], dtype=dtype, device=device)
l1 = torch.linalg.vector_norm(v, ord=1)
l2 = torch.linalg.vector_norm(v, ord=2)
linf = torch.linalg.vector_norm(v, ord=float("inf"))
print("PyTorch", torch.__version__, "dtype", dtype, "device", device)
print("vector shape", tuple(v.shape), "L1", l1.item(), "L2", l2.item(), "Linf", linf.item())
assert l1.item() == 7 and l2.item() == 5 and linf.item() == 4
assert torch.allclose(torch.linalg.vector_norm(-2 * v), 2 * l2)


# 2. 线性变换对长度的影响
A = torch.tensor([[2., 0.], [0., 0.5]], dtype=dtype, device=device)
R = torch.tensor([[0., -1.], [1., 0.]], dtype=dtype, device=device)
scaled = A @ v
rotated = R @ v
u = torch.tensor([-1., 2.], dtype=dtype, device=device)
assert torch.allclose(A @ (u + v), A @ u + A @ v)
assert torch.allclose(A @ (-2 * v), -2 * (A @ v))
assert torch.allclose(rotated, torch.tensor([4., 3.], dtype=dtype, device=device))
assert torch.allclose(torch.linalg.vector_norm(rotated), l2)
frobenius = torch.linalg.matrix_norm(A, ord="fro")
print("scaled", scaled.tolist(), "L2", round(torch.linalg.vector_norm(scaled).item(), 9))
print("rotated", rotated.tolist(), "L2", torch.linalg.vector_norm(rotated).item())
print("A Frobenius", round(frobenius.item(), 9))


# 3. 由差分逼近一个导数
def f(z):
    return z ** 2


def forward_difference(function, point, h):
    if h == 0:
        raise ValueError("Difference step must be nonzero")
    return (function(point + h) - function(point)) / h


def central_difference(function, point, h):
    if h == 0:
        raise ValueError("Difference step must be nonzero")
    return (function(point + h) - function(point - h)) / (2 * h)


x0 = torch.tensor(2., dtype=dtype, device=device)
exact_derivative = 4.0
steps = [1e-1, 1e-2, 1e-4, 1e-6]
rows = []
for h in steps:
    forward = forward_difference(f, x0, h).item()
    central = central_difference(f, x0, h).item()
    rows.append((h, forward, central))
    print(f"h={h:.0e} forward={forward:.9f} central={central:.9f}")
assert abs(rows[-1][1] - exact_derivative) < 1e-5
assert all(abs(row[2] - exact_derivative) < 1e-6 for row in rows)


# 4. 观察过小步长与有限精度
tiny_h = 1e-16
collapsed = bool((x0 + tiny_h == x0).item())
tiny_estimate = forward_difference(f, x0, tiny_h).item()
print("tiny step collapses", collapsed, "forward estimate", tiny_estimate)
# 这里只记录观察，不把极小步长结果作为跨平台精度要求。
assert x0.ndim == 0 and scaled.shape == rotated.shape == (2,)
assert torch.isfinite(scaled).all()
print("PASS")
