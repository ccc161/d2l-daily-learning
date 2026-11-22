"""第006节：CSV、缺失值、类别编码与PyTorch张量。
依赖pandas、torch。运行python lessons/006/lesson.py。
CPU、种子42，内嵌4行训练CSV和2行后续输入，无数据下载。
输出缺失计数、训练均值、列名、张量形状与数值，最后PASS。
"""
# 1. 读取CSV并分开输入与目标
from io import StringIO
import math
import pandas as pd
import torch

torch.manual_seed(42)
torch.set_num_threads(1)
device = torch.device("cpu")
# 内嵌CSV确保脚本与Notebook都不依赖额外文件。
train_csv = "Rooms,Street,Price\n2,Pave,100\n,Gravel,150\n4,,200\n6,Pave,300\n"
later_csv = "Rooms,Street\n,Dirt\n10,\n"
train = pd.read_csv(StringIO(train_csv))
later = pd.read_csv(StringIO(later_csv))
targets = train["Price"].copy()
print("versions", pd.__version__, torch.__version__)
print("training missing counts", train.isna().sum().to_dict())


# 2. 只从训练表确定预处理规则
room_mean = float(train["Rooms"].mean())
if not math.isfinite(room_mean):
    raise ValueError("Training Rooms must contain a finite observed value")
known_streets = sorted(train["Street"].dropna().unique().tolist())
# 本课原始类别不使用以下两个保留标记。
categories = known_streets + ["__MISSING__", "__OTHER__"]
print("training room mean", room_mean)
print("known streets", known_streets)
assert room_mean == 4.0


# 3. 填补数值并保持固定的独热列
def make_features(frame, mean_rooms, street_categories):
    rooms = pd.to_numeric(frame["Rooms"], errors="raise").fillna(mean_rooms)
    streets = frame["Street"].astype("string").fillna("__MISSING__")
    streets = streets.where(streets.isin(street_categories), "__OTHER__")
    encoded = pd.get_dummies(
        pd.Categorical(streets, categories=street_categories),
        prefix="Street", dtype=float,
    )
    # 保留原表索引，拼接时维持样本对应关系。
    encoded.index = frame.index
    numeric = rooms.to_frame(name="Rooms")
    return pd.concat([numeric, encoded], axis=1).astype("float32")


train_features = make_features(train, room_mean, categories)
later_features = make_features(later, room_mean, categories)
feature_names = train_features.columns.tolist()
assert later_features.columns.tolist() == feature_names
assert "Price" not in feature_names
assert not train_features.isna().any().any()
assert not later_features.isna().any().any()
print("feature columns", feature_names)


# 4. 转换为CPU浮点张量并验收
X_train = torch.tensor(train_features.to_numpy(dtype="float32"), dtype=torch.float32, device=device)
X_later = torch.tensor(later_features.to_numpy(dtype="float32"), dtype=torch.float32, device=device)
y_train = torch.tensor(targets.to_numpy(dtype="float32"), dtype=torch.float32, device=device).reshape(-1, 1)
print("tensor shapes", tuple(X_train.shape), tuple(y_train.shape), tuple(X_later.shape))
print("train tensor", X_train.tolist())
print("later tensor", X_later.tolist())
print("target tensor", y_train.tolist())
assert X_train.shape == (4, 5) and y_train.shape == (4, 1)
assert X_later.shape == (2, 5)
assert torch.isfinite(X_train).all() and torch.isfinite(X_later).all()
assert torch.isfinite(y_train).all()
assert X_later[0, 0].item() == 4.0
assert later_features.iloc[0]["Street___OTHER__"] == 1.0
assert later_features.iloc[1]["Street___MISSING__"] == 1.0
print("dtype", X_train.dtype, "device", X_train.device)
print("PASS")
