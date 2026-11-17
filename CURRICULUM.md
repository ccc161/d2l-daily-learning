# 完整课程目录

每天一节，每节约 40 分钟：阅读 10 分钟、代码 20 分钟、作业 10 分钟。共 136 节。

| 课次 | 本节目标 | 教材 |
| --- | --- | --- |
| 001 | 学习路线与一次机器学习实验的全貌；准备 Python 与 PyTorch 环境并运行检查 | [Preface](https://d2l.ai/chapter_preface/index.html) / [Installation](https://d2l.ai/chapter_installation/index.html) |
| 002 | 使用 Notebook 运行、修改和重启实验；用数据、模型、损失描述预测问题 | [23.1](https://d2l.ai/chapter_appendix-tools-for-deep-learning/jupyter.html) / [1](https://d2l.ai/chapter_introduction/index.html) |
| 003 | 区分回归、分类与其他学习任务；理解深度学习的发展与适用场景 | [1](https://d2l.ai/chapter_introduction/index.html) |
| 004 | 认识深度学习复习：检索概念、调试代码与小测；创建张量并读取形状 | [1](https://d2l.ai/chapter_introduction/index.html) / [2.1](https://d2l.ai/chapter_preliminaries/ndarray.html) |
| 005 | 索引、切片与按元素计算；广播规则与内存共享 | [2.1](https://d2l.ai/chapter_preliminaries/ndarray.html) |
| 006 | 读取表格并处理缺失值；编码类别特征并转换为张量 | [2.2](https://d2l.ai/chapter_preliminaries/pandas.html) |
| 007 | 向量与矩阵的形状；点积、矩阵乘法与批量计算 | [2.3](https://d2l.ai/chapter_preliminaries/linear-algebra.html) / [Notation](https://d2l.ai/chapter_notation/index.html) |
| 008 | 范数与线性变换；用差分理解导数 | [2.3](https://d2l.ai/chapter_preliminaries/linear-algebra.html) / [2.4](https://d2l.ai/chapter_preliminaries/calculus.html) |
| 009 | 偏导数、梯度与链式法则；构建计算图并自动求导 | [2.4](https://d2l.ai/chapter_preliminaries/calculus.html) / [2.5](https://d2l.ai/chapter_preliminaries/autograd.html) |
| 010 | 梯度累积、分离与控制流；随机试验与条件概率 | [2.5](https://d2l.ai/chapter_preliminaries/autograd.html) / [2.6](https://d2l.ai/chapter_preliminaries/probability.html) |
| 011 | 期望、方差与采样估计；查找 API 并核对最小示例 | [2.6](https://d2l.ai/chapter_preliminaries/probability.html) / [2.7](https://d2l.ai/chapter_preliminaries/lookup-api.html) |
| 012 | 张量与数学基础复习：检索概念、调试代码与小测；写出线性模型与平方损失 | [2](https://d2l.ai/chapter_preliminaries/index.html) / [3.1](https://d2l.ai/chapter_linear-regression/linear-regression.html) |
| 013 | 手算一次梯度下降；组织 Module、DataModule 与 Trainer | [3.1](https://d2l.ai/chapter_linear-regression/linear-regression.html) / [3.2](https://d2l.ai/chapter_linear-regression/oo-design.html) |
| 014 | 跟踪一次训练循环的数据流；生成带噪声的回归数据 | [3.2](https://d2l.ai/chapter_linear-regression/oo-design.html) / [3.3](https://d2l.ai/chapter_linear-regression/synthetic-regression-data.html) |
| 015 | 构造小批量与训练验证划分；从零实现预测和损失 | [3.3](https://d2l.ai/chapter_linear-regression/synthetic-regression-data.html) / [3.4](https://d2l.ai/chapter_linear-regression/linear-regression-scratch.html) |
| 016 | 实现参数更新并检查收敛；使用 nn.Linear 与优化器复现回归 | [3.4](https://d2l.ai/chapter_linear-regression/linear-regression-scratch.html) / [3.5](https://d2l.ai/chapter_linear-regression/linear-regression-concise.html) |
| 017 | 辨认训练误差和泛化误差；用验证集比较模型复杂度 | [3.6](https://d2l.ai/chapter_linear-regression/generalization.html) |
| 018 | 理解 L2 正则化；用权重衰减改善小样本拟合 | [3.7](https://d2l.ai/chapter_linear-regression/weight-decay.html) |
| 019 | 回归与泛化复习：检索概念、调试代码与小测；把分数变为类别概率 | [3](https://d2l.ai/chapter_linear-regression/index.html) / [4.1](https://d2l.ai/chapter_linear-classification/softmax-regression.html) |
| 020 | 交叉熵与数值稳定性；读取 Fashion MNIST 的一个小批量 | [4.1](https://d2l.ai/chapter_linear-classification/softmax-regression.html) / [4.2](https://d2l.ai/chapter_linear-classification/image-classification-dataset.html) |
| 021 | 计算分类准确率与基线；从零实现 softmax 与交叉熵 | [4.3](https://d2l.ai/chapter_linear-classification/classification.html) / [4.4](https://d2l.ai/chapter_linear-classification/softmax-regression-scratch.html) |
| 022 | 训练一个小型分类器；用 CrossEntropyLoss 简化分类训练 | [4.4](https://d2l.ai/chapter_linear-classification/softmax-regression-scratch.html) / [4.5](https://d2l.ai/chapter_linear-classification/softmax-regression-concise.html) |
| 023 | 比较分类误差与交叉熵；选择验证指标并分析错误样本 | [4.6](https://d2l.ai/chapter_linear-classification/generalization-classification.html) |
| 024 | 识别协变量、标签和概念偏移；检查数据泄漏与部署分布 | [4.7](https://d2l.ai/chapter_linear-classification/environment-and-distribution-shift.html) |
| 025 | 分类与分布偏移复习：检索概念、调试代码与小测；加入隐藏层与非线性激活 | [4](https://d2l.ai/chapter_linear-classification/index.html) / [5.1](https://d2l.ai/chapter_multilayer-perceptrons/mlp.html) |
| 026 | 比较激活函数的梯度；手写两层感知机 | [5.1](https://d2l.ai/chapter_multilayer-perceptrons/mlp.html) / [5.2](https://d2l.ai/chapter_multilayer-perceptrons/mlp-implementation.html) |
| 027 | 使用 Sequential 实现同一模型；画出计算图并做前向传播 | [5.2](https://d2l.ai/chapter_multilayer-perceptrons/mlp-implementation.html) / [5.3](https://d2l.ai/chapter_multilayer-perceptrons/backprop.html) |
| 028 | 沿计算图反向计算梯度；观察梯度消失和爆炸 | [5.3](https://d2l.ai/chapter_multilayer-perceptrons/backprop.html) / [5.4](https://d2l.ai/chapter_multilayer-perceptrons/numerical-stability-and-init.html) |
| 029 | 比较初始化对激活分布的影响；诊断深层网络的过拟合 | [5.4](https://d2l.ai/chapter_multilayer-perceptrons/numerical-stability-and-init.html) / [5.5](https://d2l.ai/chapter_multilayer-perceptrons/generalization-deep.html) |
| 030 | 理解训练期与推理期的 Dropout；通过小实验比较正则化效果 | [5.6](https://d2l.ai/chapter_multilayer-perceptrons/dropout.html) |
| 031 | 房价项目的数据清洗与基线；交叉验证与对数误差 | [5.7](https://d2l.ai/chapter_multilayer-perceptrons/kaggle-house-price.html) |
| 032 | 整理可复现的预测流程；多层感知机与正则化复习：检索概念、调试代码与小测 | [5.7](https://d2l.ai/chapter_multilayer-perceptrons/kaggle-house-price.html) / [5](https://d2l.ai/chapter_multilayer-perceptrons/index.html) |
| 033 | 组合模块并实现自定义 forward；查看、共享与冻结参数 | [6.1](https://d2l.ai/chapter_builders-guide/model-construction.html) / [6.2](https://d2l.ai/chapter_builders-guide/parameters.html) |
| 034 | 编写并验证参数初始化；观察延后初始化如何确定形状 | [6.3](https://d2l.ai/chapter_builders-guide/init-param.html) / [6.4](https://d2l.ai/chapter_builders-guide/lazy-init.html) |
| 035 | 编写含参数和无参数的自定义层；保存、载入并核对模型预测 | [6.5](https://d2l.ai/chapter_builders-guide/custom-layer.html) / [6.6](https://d2l.ai/chapter_builders-guide/read-write.html) |
| 036 | 选择设备并检查张量位置；模型构建与保存复习：检索概念、调试代码与小测 | [6.7](https://d2l.ai/chapter_builders-guide/use-gpu.html) / [6](https://d2l.ai/chapter_builders-guide/index.html) |
| 037 | 从局部性与平移性质理解卷积；手算二维互相关 | [7.1](https://d2l.ai/chapter_convolutional-neural-networks/why-conv.html) / [7.2](https://d2l.ai/chapter_convolutional-neural-networks/conv-layer.html) |
| 038 | 用卷积核学习边缘特征；计算填充、步幅与输出尺寸 | [7.2](https://d2l.ai/chapter_convolutional-neural-networks/conv-layer.html) / [7.3](https://d2l.ai/chapter_convolutional-neural-networks/padding-and-strides.html) |
| 039 | 跟踪输入输出通道；理解 1×1 卷积 | [7.4](https://d2l.ai/chapter_convolutional-neural-networks/channels.html) |
| 040 | 比较最大汇聚与平均汇聚；搭建 LeNet 并检查各层形状 | [7.5](https://d2l.ai/chapter_convolutional-neural-networks/pooling.html) / [7.6](https://d2l.ai/chapter_convolutional-neural-networks/lenet.html) |
| 041 | 在小数据集上训练与评估 LeNet；卷积基础复习：检索概念、调试代码与小测 | [7.6](https://d2l.ai/chapter_convolutional-neural-networks/lenet.html) / [7](https://d2l.ai/chapter_convolutional-neural-networks/index.html) |
| 042 | 跟踪 AlexNet 的特征图与参数量；用重复卷积块搭建缩小版 VGG | [8.1](https://d2l.ai/chapter_convolutional-modern/alexnet.html) / [8.2](https://d2l.ai/chapter_convolutional-modern/vgg.html) |
| 043 | 用 NiN 理解全局平均汇聚；实现并验证一个 Inception 块 | [8.3](https://d2l.ai/chapter_convolutional-modern/nin.html) / [8.4](https://d2l.ai/chapter_convolutional-modern/googlenet.html) |
| 044 | 手算批量规范化；区分训练统计量与推理统计量 | [8.5](https://d2l.ai/chapter_convolutional-modern/batch-norm.html) |
| 045 | 实现恒等残差与投影残差；理解 ResNeXt 的分组卷积 | [8.6](https://d2l.ai/chapter_convolutional-modern/resnet.html) |
| 046 | 实现 DenseNet 的拼接与过渡层；比较卷积网络的深度、宽度与计算量 | [8.7](https://d2l.ai/chapter_convolutional-modern/densenet.html) / [8.8](https://d2l.ai/chapter_convolutional-modern/cnn-design.html) |
| 047 | 设计一个受预算约束的小型网络；现代卷积网络复习：检索概念、调试代码与小测 | [8.8](https://d2l.ai/chapter_convolutional-modern/cnn-design.html) / [8](https://d2l.ai/chapter_convolutional-modern/index.html) |
| 048 | 把时间序列转为监督学习样本；比较单步预测与滚动预测 | [9.1](https://d2l.ai/chapter_recurrent-neural-networks/sequence.html) |
| 049 | 分词、词表与未知词；构造文本序列小批量 | [9.2](https://d2l.ai/chapter_recurrent-neural-networks/text-sequence.html) |
| 050 | 计算序列概率与困惑度；展开 RNN 并跟踪隐藏状态 | [9.3](https://d2l.ai/chapter_recurrent-neural-networks/language-model.html) / [9.4](https://d2l.ai/chapter_recurrent-neural-networks/rnn.html) |
| 051 | 手算一步 RNN 的输出；从零实现 RNN 前向计算 | [9.4](https://d2l.ai/chapter_recurrent-neural-networks/rnn.html) / [9.5](https://d2l.ai/chapter_recurrent-neural-networks/rnn-scratch.html) |
| 052 | 实现截断训练与梯度裁剪；用小语料生成字符 | [9.5](https://d2l.ai/chapter_recurrent-neural-networks/rnn-scratch.html) |
| 053 | 使用 nn.RNN 复现语言模型；理解时间反向传播与长程梯度 | [9.6](https://d2l.ai/chapter_recurrent-neural-networks/rnn-concise.html) / [9.7](https://d2l.ai/chapter_recurrent-neural-networks/bptt.html) |
| 054 | 序列与循环网络复习：检索概念、调试代码与小测；跟踪 LSTM 的记忆状态与门 | [9](https://d2l.ai/chapter_recurrent-neural-networks/index.html) / [10.1](https://d2l.ai/chapter_recurrent-modern/lstm.html) |
| 055 | 实现并测试一个 LSTM 单元；跟踪 GRU 的更新门与重置门 | [10.1](https://d2l.ai/chapter_recurrent-modern/lstm.html) / [10.2](https://d2l.ai/chapter_recurrent-modern/gru.html) |
| 056 | 比较 GRU 与 LSTM 的输出形状；堆叠循环层并检查状态维度 | [10.2](https://d2l.ai/chapter_recurrent-modern/gru.html) / [10.3](https://d2l.ai/chapter_recurrent-modern/deep-rnn.html) |
| 057 | 理解双向 RNN 与信息可用范围；准备平行语料、填充与有效长度 | [10.4](https://d2l.ai/chapter_recurrent-modern/bi-rnn.html) / [10.5](https://d2l.ai/chapter_recurrent-modern/machine-translation-and-dataset.html) |
| 058 | 搭建编码器和解码器接口；实现教师强制与序列损失 | [10.6](https://d2l.ai/chapter_recurrent-modern/encoder-decoder.html) / [10.7](https://d2l.ai/chapter_recurrent-modern/seq2seq.html) |
| 059 | 在小语料上运行 seq2seq；检查推理过程与 BLEU 指标 | [10.7](https://d2l.ai/chapter_recurrent-modern/seq2seq.html) |
| 060 | 手动跟踪贪心搜索和束搜索；门控网络与机器翻译复习：检索概念、调试代码与小测 | [10.8](https://d2l.ai/chapter_recurrent-modern/beam-search.html) / [10](https://d2l.ai/chapter_recurrent-modern/index.html) |
| 061 | 用查询、键和值解释注意力；计算相似度权重与加权平均 | [11.1](https://d2l.ai/chapter_attention-mechanisms-and-transformers/queries-keys-values.html) / [11.2](https://d2l.ai/chapter_attention-mechanisms-and-transformers/attention-pooling.html) |
| 062 | 实现加性和点积评分；构造注意力掩码并检查数值 | [11.3](https://d2l.ai/chapter_attention-mechanisms-and-transformers/attention-scoring-functions.html) |
| 063 | 在 seq2seq 中接入 Bahdanau 注意力；拆分多头并跟踪张量形状 | [11.4](https://d2l.ai/chapter_attention-mechanisms-and-transformers/bahdanau-attention.html) / [11.5](https://d2l.ai/chapter_attention-mechanisms-and-transformers/multihead-attention.html) |
| 064 | 实现一个小型多头注意力层；理解自注意力的信息流 | [11.5](https://d2l.ai/chapter_attention-mechanisms-and-transformers/multihead-attention.html) / [11.6](https://d2l.ai/chapter_attention-mechanisms-and-transformers/self-attention-and-positional-encoding.html) |
| 065 | 构造位置编码并观察位置差异；搭建 Transformer 编码器块 | [11.6](https://d2l.ai/chapter_attention-mechanisms-and-transformers/self-attention-and-positional-encoding.html) / [11.7](https://d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html) |
| 066 | 搭建带因果掩码的解码器块；完成一次小批量训练 | [11.7](https://d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html) |
| 067 | 跟踪逐词生成与缓存状态；把图像切成词元并加入位置编码 | [11.7](https://d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html) / [11.8](https://d2l.ai/chapter_attention-mechanisms-and-transformers/vision-transformer.html) |
| 068 | 运行一个缩小版 ViT 前向过程；区分编码器与解码器预训练目标 | [11.8](https://d2l.ai/chapter_attention-mechanisms-and-transformers/vision-transformer.html) / [11.9](https://d2l.ai/chapter_attention-mechanisms-and-transformers/large-pretraining-transformers.html) |
| 069 | 分析预训练的规模、数据与迁移方式；注意力与 Transformer复习：检索概念、调试代码与小测 | [11.9](https://d2l.ai/chapter_attention-mechanisms-and-transformers/large-pretraining-transformers.html) / [11](https://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html) |
| 070 | 区分优化误差与泛化误差；判断凸集、凸函数与局部极小值 | [12.1](https://d2l.ai/chapter_optimization/optimization-intro.html) / [12.2](https://d2l.ai/chapter_optimization/convexity.html) |
| 071 | 比较不同学习率的梯度下降轨迹；观察随机梯度的噪声 | [12.3](https://d2l.ai/chapter_optimization/gd.html) / [12.4](https://d2l.ai/chapter_optimization/sgd.html) |
| 072 | 比较小批量大小与梯度估计；手算并实现动量更新 | [12.5](https://d2l.ai/chapter_optimization/minibatch-sgd.html) / [12.6](https://d2l.ai/chapter_optimization/momentum.html) |
| 073 | 用 Adagrad 累积平方梯度；用 RMSProp 跟踪梯度尺度 | [12.7](https://d2l.ai/chapter_optimization/adagrad.html) / [12.8](https://d2l.ai/chapter_optimization/rmsprop.html) |
| 074 | 理解 Adadelta 的更新尺度；手算 Adam 的矩估计与偏差修正 | [12.9](https://d2l.ai/chapter_optimization/adadelta.html) / [12.10](https://d2l.ai/chapter_optimization/adam.html) |
| 075 | 比较 Adam 与 SGD 的训练曲线；实现预热与学习率衰减 | [12.10](https://d2l.ai/chapter_optimization/adam.html) / [12.11](https://d2l.ai/chapter_optimization/lr-scheduler.html) |
| 076 | 优化算法复习：检索概念、调试代码与小测；区分即时执行与编译执行 | [12](https://d2l.ai/chapter_optimization/index.html) / [13.1](https://d2l.ai/chapter_computational-performance/hybridize.html) |
| 077 | 正确计时并解释异步计算；识别数据传输与计算的并行机会 | [13.2](https://d2l.ai/chapter_computational-performance/async-computation.html) / [13.3](https://d2l.ai/chapter_computational-performance/auto-parallelism.html) |
| 078 | 用内存、带宽与算力解释瓶颈；手动拆分批次并聚合梯度 | [13.4](https://d2l.ai/chapter_computational-performance/hardware.html) / [13.5](https://d2l.ai/chapter_computational-performance/multiple-gpus.html) |
| 079 | 理解数据并行中的参数同步；阅读并缩小多设备训练示例 | [13.5](https://d2l.ai/chapter_computational-performance/multiple-gpus.html) / [13.6](https://d2l.ai/chapter_computational-performance/multiple-gpus-concise.html) |
| 080 | 模拟参数服务器的一轮更新；计算性能复习：检索概念、调试代码与小测 | [13.7](https://d2l.ai/chapter_computational-performance/parameterserver.html) / [13](https://d2l.ai/chapter_computational-performance/index.html) |
| 081 | 实现图像增广并比较训练和验证流程；替换分类头并冻结特征 | [14.1](https://d2l.ai/chapter_computer-vision/image-augmentation.html) / [14.2](https://d2l.ai/chapter_computer-vision/fine-tuning.html) |
| 082 | 比较冻结训练与整体微调；转换边界框坐标并计算 IoU | [14.2](https://d2l.ai/chapter_computer-vision/fine-tuning.html) / [14.3](https://d2l.ai/chapter_computer-vision/bounding-box.html) |
| 083 | 生成锚框并理解正负匹配；编码边界框偏移 | [14.4](https://d2l.ai/chapter_computer-vision/anchor.html) |
| 084 | 实现非极大值抑制；比较不同尺度的检测特征图 | [14.4](https://d2l.ai/chapter_computer-vision/anchor.html) / [14.5](https://d2l.ai/chapter_computer-vision/multiscale-object-detection.html) |
| 085 | 读取目标检测样本并构造批次；搭建 SSD 的预测头 | [14.6](https://d2l.ai/chapter_computer-vision/object-detection-dataset.html) / [14.7](https://d2l.ai/chapter_computer-vision/ssd.html) |
| 086 | 计算分类与回归损失；运行小规模检测与可视化 | [14.7](https://d2l.ai/chapter_computer-vision/ssd.html) |
| 087 | 区分 R CNN 系列的候选区域流程；理解 RoI 汇聚与共享特征 | [14.8](https://d2l.ai/chapter_computer-vision/rcnn.html) |
| 088 | 准备逐像素标签并检查类别映射；手算转置卷积与输出尺寸 | [14.9](https://d2l.ai/chapter_computer-vision/semantic-segmentation-and-dataset.html) / [14.10](https://d2l.ai/chapter_computer-vision/transposed-conv.html) |
| 089 | 搭建 FCN 并对齐输出分辨率；运行小图像分割与 IoU 评估 | [14.11](https://d2l.ai/chapter_computer-vision/fcn.html) |
| 090 | 区分内容损失与风格损失；优化一张低分辨率风格迁移图像 | [14.12](https://d2l.ai/chapter_computer-vision/neural-style.html) |
| 091 | 搭建 CIFAR 10 训练验证流程；分析增广与模型选择结果 | [14.13](https://d2l.ai/chapter_computer-vision/kaggle-cifar10.html) |
| 092 | 为犬种识别建立迁移学习基线；整理错误分析与项目报告 | [14.14](https://d2l.ai/chapter_computer-vision/kaggle-dog.html) |
| 093 | 计算机视觉实践复习：检索概念、调试代码与小测；比较 Skip gram 与 CBOW | [14](https://d2l.ai/chapter_computer-vision/index.html) / [15.1](https://d2l.ai/chapter_natural-language-processing-pretraining/word2vec.html) |
| 094 | 理解词向量的预测目标；构造负采样与近似训练目标 | [15.1](https://d2l.ai/chapter_natural-language-processing-pretraining/word2vec.html) / [15.2](https://d2l.ai/chapter_natural-language-processing-pretraining/approx-training.html) |
| 095 | 构造词窗口、负例与填充掩码；训练一个微型 word2vec 模型 | [15.3](https://d2l.ai/chapter_natural-language-processing-pretraining/word-embedding-dataset.html) / [15.4](https://d2l.ai/chapter_natural-language-processing-pretraining/word2vec-pretraining.html) |
| 096 | 检查相似词与训练损失；理解共现统计与 GloVe 目标 | [15.4](https://d2l.ai/chapter_natural-language-processing-pretraining/word2vec-pretraining.html) / [15.5](https://d2l.ai/chapter_natural-language-processing-pretraining/glove.html) |
| 097 | 用子词表示处理未登录词；计算余弦相似度与词类比 | [15.6](https://d2l.ai/chapter_natural-language-processing-pretraining/subword-embedding.html) / [15.7](https://d2l.ai/chapter_natural-language-processing-pretraining/similarity-analogy.html) |
| 098 | 理解 BERT 的输入表示；构造掩码语言模型与句间任务 | [15.8](https://d2l.ai/chapter_natural-language-processing-pretraining/bert.html) |
| 099 | 准备 BERT 的句对和掩码样本；运行微型 BERT 的预训练损失 | [15.9](https://d2l.ai/chapter_natural-language-processing-pretraining/bert-dataset.html) / [15.10](https://d2l.ai/chapter_natural-language-processing-pretraining/bert-pretraining.html) |
| 100 | 检查掩码位置与参数更新；词向量与 BERT 预训练复习：检索概念、调试代码与小测 | [15.10](https://d2l.ai/chapter_natural-language-processing-pretraining/bert-pretraining.html) / [15](https://d2l.ai/chapter_natural-language-processing-pretraining/index.html) |
| 101 | 准备情感分类数据并防止泄漏；搭建双向 RNN 情感分类器 | [16.1](https://d2l.ai/chapter_natural-language-processing-applications/sentiment-analysis-and-dataset.html) / [16.2](https://d2l.ai/chapter_natural-language-processing-applications/sentiment-analysis-rnn.html) |
| 102 | 搭建 Text CNN 并比较分类错误；区分蕴含、矛盾与中立标签 | [16.3](https://d2l.ai/chapter_natural-language-processing-applications/sentiment-analysis-cnn.html) / [16.4](https://d2l.ai/chapter_natural-language-processing-applications/natural-language-inference-and-dataset.html) |
| 103 | 实现句对的注意力对齐；完成推断分类器的前向与损失 | [16.5](https://d2l.ai/chapter_natural-language-processing-applications/natural-language-inference-attention.html) |
| 104 | 为 BERT 添加句子分类头；为 BERT 添加词元分类头 | [16.6](https://d2l.ai/chapter_natural-language-processing-applications/finetuning-bert.html) |
| 105 | 微调一个小型自然语言推断基线；分析泛化结果与错误类型 | [16.7](https://d2l.ai/chapter_natural-language-processing-applications/natural-language-inference-bert.html) |
| 106 | 自然语言处理应用复习：检索概念、调试代码与小测；小项目一：确定任务、数据划分与评估指标 | [16](https://d2l.ai/chapter_natural-language-processing-applications/index.html) / [5.7](https://d2l.ai/chapter_multilayer-perceptrons/kaggle-house-price.html) / [14.13](https://d2l.ai/chapter_computer-vision/kaggle-cifar10.html) |
| 107 | 小项目二：运行最小基线并保存实验记录；小项目三：只改变一个因素并比较验证结果 | [5.7](https://d2l.ai/chapter_multilayer-perceptrons/kaggle-house-price.html) / [14.13](https://d2l.ai/chapter_computer-vision/kaggle-cifar10.html) |
| 108 | 小项目四：检查错误样本并完成简短报告；写出状态、动作、奖励与转移 | [5.7](https://d2l.ai/chapter_multilayer-perceptrons/kaggle-house-price.html) / [14.13](https://d2l.ai/chapter_computer-vision/kaggle-cifar10.html) / [17.1](https://d2l.ai/chapter_reinforcement-learning/mdp.html) |
| 109 | 计算策略的折扣回报；手算贝尔曼更新 | [17.1](https://d2l.ai/chapter_reinforcement-learning/mdp.html) / [17.2](https://d2l.ai/chapter_reinforcement-learning/value-iter.html) |
| 110 | 在小网格上实现价值迭代；手算 Q 学习与探索策略 | [17.2](https://d2l.ai/chapter_reinforcement-learning/value-iter.html) / [17.3](https://d2l.ai/chapter_reinforcement-learning/qlearning.html) |
| 111 | 在小环境中更新 Q 表；强化学习复习：检索概念、调试代码与小测 | [17.3](https://d2l.ai/chapter_reinforcement-learning/qlearning.html) / [17](https://d2l.ai/chapter_reinforcement-learning/index.html) |
| 112 | 从贝叶斯回归理解函数分布；构造核矩阵与先验样本 | [18.1](https://d2l.ai/chapter_gaussian-processes/gp-intro.html) / [18.2](https://d2l.ai/chapter_gaussian-processes/gp-priors.html) |
| 113 | 观察核参数如何改变函数；计算高斯过程后验均值 | [18.2](https://d2l.ai/chapter_gaussian-processes/gp-priors.html) / [18.3](https://d2l.ai/chapter_gaussian-processes/gp-inference.html) |
| 114 | 解释预测不确定性与噪声；高斯过程复习：检索概念、调试代码与小测 | [18.3](https://d2l.ai/chapter_gaussian-processes/gp-inference.html) / [18](https://d2l.ai/chapter_gaussian-processes/index.html) |
| 115 | 区分模型参数与超参数；定义搜索空间、目标与预算 | [19.1](https://d2l.ai/chapter_hyperparameter-optimization/hyperopt-intro.html) / [19.2](https://d2l.ai/chapter_hyperparameter-optimization/hyperopt-api.html) |
| 116 | 模拟异步随机搜索的调度；手算逐次减半的资源分配 | [19.3](https://d2l.ai/chapter_hyperparameter-optimization/rs-async.html) / [19.4](https://d2l.ai/chapter_hyperparameter-optimization/sh-intro.html) |
| 117 | 模拟 ASHA 并检查早停偏差；超参数搜索复习：检索概念、调试代码与小测 | [19.5](https://d2l.ai/chapter_hyperparameter-optimization/sh-async.html) / [19](https://d2l.ai/chapter_hyperparameter-optimization/index.html) |
| 118 | 理解生成器与判别器的目标；交替更新一个微型 GAN | [20.1](https://d2l.ai/chapter_generative-adversarial-networks/gan.html) |
| 119 | 诊断模式坍塌和训练失衡；搭建 DCGAN 的上下采样网络 | [20.1](https://d2l.ai/chapter_generative-adversarial-networks/gan.html) / [20.2](https://d2l.ai/chapter_generative-adversarial-networks/dcgan.html) |
| 120 | 训练低分辨率生成示例；比较样本质量与损失曲线 | [20.2](https://d2l.ai/chapter_generative-adversarial-networks/dcgan.html) |
| 121 | 生成对抗网络复习：检索概念、调试代码与小测；区分显式反馈、隐式反馈与排序 | [20](https://d2l.ai/chapter_generative-adversarial-networks/index.html) / [21.1](https://d2l.ai/chapter_recommender-systems/recsys-intro.html) |
| 122 | 划分 MovieLens 并避免时间泄漏；手算矩阵分解的预测 | [21.2](https://d2l.ai/chapter_recommender-systems/movielens.html) / [21.3](https://d2l.ai/chapter_recommender-systems/mf.html) |
| 123 | 训练一个小型评分模型；用 AutoRec 重建评分并屏蔽缺失值 | [21.3](https://d2l.ai/chapter_recommender-systems/mf.html) / [21.4](https://d2l.ai/chapter_recommender-systems/autorec.html) |
| 124 | 构造成对排序与负采样；结合矩阵分解与 MLP 进行推荐 | [21.5](https://d2l.ai/chapter_recommender-systems/ranking.html) / [21.6](https://d2l.ai/chapter_recommender-systems/neumf.html) |
| 125 | 准备序列推荐样本并预测下一项；编码稀疏特征并建立点击率基线 | [21.7](https://d2l.ai/chapter_recommender-systems/seqrec.html) / [21.8](https://d2l.ai/chapter_recommender-systems/ctr.html) |
| 126 | 高效计算二阶特征交互；组合 DeepFM 并检查共享嵌入 | [21.9](https://d2l.ai/chapter_recommender-systems/fm.html) / [21.10](https://d2l.ai/chapter_recommender-systems/deepfm.html) |
| 127 | 推荐系统复习：检索概念、调试代码与小测；用几何图形理解投影与线性变换 | [21](https://d2l.ai/chapter_recommender-systems/index.html) / [22.1](https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/geometry-linear-algebraic-ops.html) |
| 128 | 计算特征值并解释主方向；用泰勒展开近似一个函数 | [22.2](https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/eigendecomposition.html) / [22.3](https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/single-variable-calculus.html) |
| 129 | 跟踪梯度、雅可比与海森矩阵；用积分联系概率密度与期望 | [22.4](https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/multivariable-calculus.html) / [22.5](https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/integral-calculus.html) |
| 130 | 计算随机变量变换后的分布；从似然推导常用训练损失 | [22.6](https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/random-variables.html) / [22.7](https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/maximum-likelihood.html) |
| 131 | 比较常用分布及其参数；实现一个朴素贝叶斯小分类器 | [22.8](https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/distributions.html) / [22.9](https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/naive-bayes.html) |
| 132 | 用采样解释估计误差与置信区间；手算熵、交叉熵与 KL 散度 | [22.10](https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/statistics.html) / [22.11](https://d2l.ai/chapter_appendix-mathematics-for-deep-learning/information-theory.html) |
| 133 | 阅读 SageMaker 的训练流程与资源配置；阅读 EC2 的实例、存储与训练流程 | [23.2](https://d2l.ai/chapter_appendix-tools-for-deep-learning/sagemaker.html) / [23.3](https://d2l.ai/chapter_appendix-tools-for-deep-learning/aws.html) |
| 134 | 在 Colab 中检查运行时与文件持久性；根据模型需求估算显存和计算资源 | [23.4](https://d2l.ai/chapter_appendix-tools-for-deep-learning/colab.html) / [23.5](https://d2l.ai/chapter_appendix-tools-for-deep-learning/selecting-servers-gpus.html) |
| 135 | 复现问题并准备可读的改进补丁；阅读并拆解一个 d2l 工具函数 | [23.6](https://d2l.ai/chapter_appendix-tools-for-deep-learning/contributing.html) / [23.7](https://d2l.ai/chapter_appendix-tools-for-deep-learning/utils.html) |
| 136 | 定位 d2l API 与对应源码；整理个人实验模板与后续学习清单 | [23.8](https://d2l.ai/chapter_appendix-tools-for-deep-learning/d2l.html) / [23.7](https://d2l.ai/chapter_appendix-tools-for-deep-learning/utils.html) |
