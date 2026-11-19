# 动手学深度学习 每日 40 分钟

基于 D2L 教材、官方源码和 UC Berkeley STAT 157 的中文自学课程，共 136 节。每节包括阅读、PyTorch 实验、作业、参考答案和课件。

学习时间为每天 20:00（Asia/Taipei，UTC+8），每节约 40 分钟：阅读 10 分钟、代码练习 20 分钟、作业及核对 10 分钟。完整路线约 4.5 个月。

## 纯本地实践

所有核心实验在学习者自己的电脑上完成：本地 Python、Jupyter、PyTorch，CPU 小规模示例为基线，本机 CUDA 或 Apple MPS 为可选加速。第 133–134 节已改为本地环境复现、数据与检查点管理、训练恢复、Jupyter 和硬件预算；多设备训练使用单机模拟。无需 Colab、SageMaker、EC2、云账号或付费算力。每日资料生成与推送继续由 Work 云端任务负责。

## 从这里开始

- [完整课程目录](CURRICULUM.md)
- [可下载或在本地浏览的学习计划](study-plan.html)
- [课程数据](curriculum.json)
- [学习与交付进度](progress.json)
- [每节交付规范](docs/teaching-spec.md)
- [来源与许可说明](docs/source-notices.md)

## 当前状态

ChatGPT Work 云端已交付至第 003/136 节。已推送 3 节，已确认完成 0 节；下一节为 004。代码、Notebook 顺序执行与课件打印验证范围见 [第 003 节验证记录](lessons/003/validation.json)。

- [第 003 节笔记](lessons/003/notes.html)
- [第 003 节六页课件](lessons/003/slides.html)
- [第 002 节笔记](lessons/002/notes.html)
- [第 002 节六页课件](lessons/002/slides.html)
- [第 001 节笔记](lessons/001/notes.html)
- [第 001 节六页课件](lessons/001/slides.html)

HTML 可下载到同一目录后用本机浏览器打开，课件支持浏览器打印。

## 每节学习包

每次在 `lessons/NNN/` 保存 `notes.html`、`lesson.py`、`lesson.ipynb`、`homework.txt`、`answers.html` 和 `slides.html`。答案与作业分开，课件为 5–7 页可浏览、可打印的 HTML。学习包完成检查后，以一次提交保存全部文件和进度。

已推送与已确认完成分开记录。完成进度由学习者的反馈或作业更新。个人原始反馈及运行凭据不写入公开仓库。

## 三项主要参考

1. [Dive into Deep Learning](https://d2l.ai/)：内容范围与章节编号。
2. [d2l-ai/d2l-en](https://github.com/d2l-ai/d2l-en)：代码、依赖与辅助函数。
3. [UC Berkeley STAT 157 2019 春季课表](https://courses.d2l.ai/berkeley-stat-157/syllabus.html)：教学组织、讲义、视频与作业参考。

[中文教材](https://zh.d2l.ai/)辅助理解。历史课程中的 MXNet 示例如经改编，会注明与 PyTorch 实现的差异。自编参考答案不代表大学课程的官方标准答案。
