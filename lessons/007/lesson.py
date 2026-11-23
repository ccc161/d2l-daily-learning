"""第007节：向量、点积与矩阵批量计算。
依赖torch。运行python lessons/007/lesson.py。
CPU、种子42，内嵌小矩阵，无外部文件或数据下载。
输出形状、点积、单输出与多输出结果，预期错误被捕获，末行PASS。
"""
# 1. 向量与矩阵的形状
import torch

torch.manual_seed(42)
torch.set_num_threads(1)
device = torch.device("cpu")
# 两行样本，每行三个特征；参数按特征顺序排列。
X = torch.tensor([[1., 2., 3.], [4., 5., 6.]], dtype=torch.float32, device=device)
w = torch.tensor([2., -1., 0.5], dtype=torch.float32, device=device)
w_column = w.reshape(-1, 1)
print("PyTorch", torch.__version__, "device", device)
print("input shapes", tuple(X.shape), tuple(w.shape), tuple(w_column.shape))
print("transpose shape", tuple(X.T.shape))
assert X.shape == (2, 3) and X.T.shape == (3, 2)


# 2. 点积是按元素乘后求和
first_dot = torch.dot(X[0], w)
first_sum = (X[0] * w).sum()
print("first dot", first_dot.item(), "shape", tuple(first_dot.shape))
print("first element products", (X[0] * w).tolist())
assert torch.allclose(first_dot, first_sum)
assert abs(first_dot.item() - 1.5) < 1e-6


# 3. 把多个样本一起计算
per_row = torch.stack([torch.dot(row, w) for row in X])
batch_scores = X @ w
column_scores = X @ w_column
element_products = X * w
print("elementwise shape", tuple(element_products.shape))
print("batch scores", batch_scores.tolist(), "shape", tuple(batch_scores.shape))
print("column scores", column_scores.tolist(), "shape", tuple(column_scores.shape))
assert torch.allclose(batch_scores, per_row)
assert torch.allclose(batch_scores, element_products.sum(dim=1))
assert torch.allclose(column_scores.squeeze(1), batch_scores)
assert batch_scores.shape == (2,) and column_scores.shape == (2, 1)
single_output = batch_scores + 0.25
print("single output with bias", single_output.tolist())
assert torch.allclose(single_output, torch.tensor([1.75, 6.25], device=device))


# 4. 矩阵乘法与多个输出
# W的每一列对应一个输出，两个输出共享同一批输入。
W = torch.tensor([[2., 1.], [-1., 0.], [0.5, -1.]], dtype=torch.float32, device=device)
bias = torch.tensor([0.25, 1.], dtype=torch.float32, device=device)
multi_output = X @ W + bias
by_columns = torch.stack([X @ W[:, j] for j in range(W.shape[1])], dim=1) + bias
print("matrix shapes", tuple(X.shape), tuple(W.shape), tuple(multi_output.shape))
print("multi output", multi_output.tolist())
assert torch.allclose(multi_output, by_columns)
assert torch.allclose(multi_output, torch.tensor([[1.75, -1.], [6.25, -1.]], device=device))
try:
    X @ torch.ones((2, 1), dtype=torch.float32, device=device)
except RuntimeError:
    print("incompatible matmul rejected: inner dimensions 3 and 2")
else:
    raise AssertionError("Expected mismatched inner dimensions to fail")
print("PASS")
