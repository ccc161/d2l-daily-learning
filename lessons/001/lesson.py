"""第001节：本机 CPU 环境检查与微型回归实验。
依赖：torch。运行：python lesson.py。无需下载数据。
输入为8个训练样本、2个留出样本；输出设备、形状、损失与参数。
"""
import torch


def run_experiment():
    # 本节固定CPU作为可复现基线。CUDA/MPS仅报告可用性。
    torch.manual_seed(42)
    torch.set_num_threads(1)
    device = torch.device("cpu")
    print("PyTorch", torch.__version__)
    print("device", device)
    print("CUDA available", torch.cuda.is_available())
    print("MPS available", torch.backends.mps.is_available())

    # 每行一个样本、每个样本一个特征；标签也保留列维度。
    x = torch.tensor([-2., -1.5, -1., -.5, .5, 1., 1.5, 2.]).reshape(-1, 1)
    y = 2 * x + 1
    x_test = torch.tensor([[-1.25], [.75]])
    y_test = 2 * x_test + 1
    model = torch.nn.Linear(1, 1).to(device)
    with torch.no_grad():
        model.weight.zero_()
        model.bias.zero_()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
    loss_fn = torch.nn.MSELoss()
    initial_loss = loss_fn(model(x), y).item()
    print("train shapes", tuple(x.shape), tuple(y.shape))
    for _ in range(120):
        prediction = model(x)
        loss = loss_fn(prediction, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    with torch.no_grad():
        final_loss = loss_fn(model(x), y).item()
        test_prediction = model(x_test)
        test_loss = loss_fn(test_prediction, y_test).item()
    print(f"train MSE {initial_loss:.6f} -> {final_loss:.6f}")
    print(f"test MSE {test_loss:.6f}")
    print(f"weight {model.weight.item():.6f}, bias {model.bias.item():.6f}")
    print("test predictions", test_prediction.flatten().tolist())
    assert final_loss < initial_loss
    assert test_loss < 1e-4
    assert abs(model.weight.item() - 2) < .01
    assert abs(model.bias.item() - 1) < .01
    print("PASS")


if __name__ == "__main__":
    run_experiment()
