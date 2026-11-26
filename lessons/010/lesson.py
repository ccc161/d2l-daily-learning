"""第010节：梯度缓冲区、detach、控制流与条件概率。
依赖torch。运行python lessons/010/lesson.py。
本机CPU，自动求导float32，种子42；骰子模拟6000次，无外部数据。
输出梯度对照、分支结果、精确与经验条件概率，最后PASS。
"""
# 1. 新图的梯度累加到同一叶子
import torch

torch.manual_seed(42)
torch.set_num_threads(1)
device = torch.device("cpu")
x = torch.tensor(2., dtype=torch.float32, device=device, requires_grad=True)
(x ** 2).backward()
first = x.grad.item()
# 新建前向表达式，不复用第一次反向已释放的图。
(3 * x).backward()
accumulated = x.grad.item()
x.grad.zero_()
cleared = x.grad.item()
(x ** 2).backward()
fresh = x.grad.item()
print("PyTorch", torch.__version__, "device", device)
print("gradients first/accumulated/cleared/fresh", first, accumulated, cleared, fresh)
assert (first, accumulated, cleared, fresh) == (4., 7., 0., 4.)


# 2. detach改变参与求导的路径
a = torch.tensor(2., dtype=torch.float32, device=device, requires_grad=True)
square = a * a
fixed_square = square.detach()
detached_output = fixed_square * a
detached_output.backward()
b = torch.tensor(2., dtype=torch.float32, device=device, requires_grad=True)
full_output = b * b * b
full_output.backward()
print("same forward values", detached_output.item(), full_output.item())
print("detached/full gradients", a.grad.item(), b.grad.item())
assert not fixed_square.requires_grad
assert a.grad.item() == 4 and b.grad.item() == 12


# 3. 控制流记录本次实际执行的运算
def piecewise(value):
    if value.item() > 0:
        return value ** 2
    return 3 * value


branch_rows = []
for initial in [2., -2.]:
    leaf = torch.tensor(initial, dtype=torch.float32, device=device, requires_grad=True)
    result = piecewise(leaf)
    result.backward()
    branch_rows.append((initial, result.item(), leaf.grad.item()))
print("branch input/output/gradient", branch_rows)
assert branch_rows == [(2., 4., 4.), (-2., -6., 3.)]


# 4. 随机试验与条件概率
def conditional_frequency(event, condition):
    assert event.shape == condition.shape
    count = int(condition.sum().item())
    if count == 0:
        return None
    return int((event & condition).sum().item()) / count


# 公平六面骰的六个等可能结果：A为偶数，B为大于3。
outcomes = torch.arange(1, 7, device="cpu")
A = outcomes % 2 == 0
B = outcomes > 3
p_A = int(A.sum().item()) / outcomes.numel()
p_B = int(B.sum().item()) / outcomes.numel()
p_joint = int((A & B).sum().item()) / outcomes.numel()
p_conditional = conditional_frequency(A, B)
print("exact P(A), P(B), P(A and B), P(A|B)", p_A, p_B, p_joint, p_conditional)
assert p_conditional is not None and abs(p_conditional - 2/3) < 1e-12
assert abs(p_joint - p_A * p_B) > 0.01

generator = torch.Generator(device="cpu").manual_seed(42)
draws = torch.randint(1, 7, (6000,), generator=generator, device="cpu")
sample_A = draws % 2 == 0
sample_B = draws > 3
estimate = conditional_frequency(sample_A, sample_B)
print("sample counts B/AB", int(sample_B.sum().item()), int((sample_A & sample_B).sum().item()))
print("empirical P(A|B)", None if estimate is None else round(estimate, 6))
assert estimate is not None and 0 <= estimate <= 1
assert conditional_frequency(A, torch.zeros_like(B)) is None
print("PASS")
