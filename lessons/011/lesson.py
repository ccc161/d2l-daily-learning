"""第011节：期望、方差、采样估计与API最小核对。
依赖torch>=2.0（correction接口）。运行python lessons/011/lesson.py。
本机CPU float64、种子42；最多20000个骰子样本，无外部数据。
输出理论矩、correction对照、归约形状和采样估计表，最后PASS。
"""
# 1. 从概率模型计算期望和方差
import torch

torch.manual_seed(42)
torch.set_num_threads(1)
device = torch.device("cpu")
dtype = torch.float64
values = torch.arange(1, 7, dtype=dtype, device=device)
probabilities = torch.full((6,), 1/6, dtype=dtype, device=device)
expectation = (values * probabilities).sum()
variance = ((values - expectation) ** 2 * probabilities).sum()
second_moment = (values ** 2 * probabilities).sum()
assert torch.allclose(variance, second_moment - expectation ** 2)
assert abs(expectation.item() - 3.5) < 1e-12
assert abs(variance.item() - 35/12) < 1e-12
print("PyTorch", torch.__version__, "dtype", dtype, "device", device)
print(f"fair die expectation={expectation.item():.9f} variance={variance.item():.9f}")


# 2. 查文档，用三个数核对默认参数
available = [name for name in dir(torch) if name in ("mean", "var", "std")]
print("API names", available)
print("local var signature", torch.var.__doc__.strip().splitlines()[0])
small = torch.tensor([1., 2., 3.], dtype=dtype, device=device)
manual_variance = ((small - small.mean()) ** 2).mean()
variance_0 = torch.var(small, correction=0)
variance_1 = torch.var(small, correction=1)
default_variance = torch.var(small)
print("small mean", small.mean().item())
print("small variances correction0/correction1/default",
      round(variance_0.item(), 9), variance_1.item(), default_variance.item())
assert torch.allclose(variance_0, manual_variance)
assert abs(variance_0.item() - 2/3) < 1e-12
assert variance_1.item() == default_variance.item() == 1.0
assert torch.allclose(torch.var(values, correction=0), variance)


# 3. 核对归约轴和输出形状
matrix = torch.tensor([[1., 2., 3.], [4., 5., 6.]], dtype=dtype, device=device)
row_means = torch.mean(matrix, dim=1)
row_variances = torch.var(matrix, dim=1, correction=0)
kept_variances = torch.var(matrix, dim=1, correction=0, keepdim=True)
print("row means", row_means.tolist(), "shape", tuple(row_means.shape))
print("row variances", [round(value, 9) for value in row_variances.tolist()])
print("variance shapes", tuple(row_variances.shape), tuple(kept_variances.shape))
assert row_means.shape == row_variances.shape == (2,)
assert kept_variances.shape == (2, 1)
assert torch.allclose(row_variances, torch.full((2,), 2/3, dtype=dtype))


# 4. 用有限样本估计总体量
generator = torch.Generator(device="cpu").manual_seed(42)
draws = torch.randint(1, 7, (20000,), generator=generator, device="cpu").to(dtype)
estimates = []
for n in [20, 200, 2000, 20000]:
    sample = draws[:n]
    mean_estimate = sample.mean().item()
    # 本表描述样本自身的平均平方偏差，明确使用分母n。
    variance_estimate = torch.var(sample, correction=0).item()
    mean_error = abs(mean_estimate - expectation.item())
    variance_error = abs(variance_estimate - variance.item())
    estimates.append((n, mean_estimate, variance_estimate, mean_error, variance_error))
    print(f"n={n} mean={mean_estimate:.6f} var0={variance_estimate:.6f} "
          f"mean_error={mean_error:.6f} variance_error={variance_error:.6f}")
    assert 1 <= mean_estimate <= 6
    assert variance_estimate >= 0
# 不把误差逐次下降或某个随机结果设成必然规律。
print("PASS")
