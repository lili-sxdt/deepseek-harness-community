# 快速上手

> 从零跑到你的第一个 DeepSeek Harness 任务。**以官方为准**，此处仅给指引。

## 1. 安装

DeepSeek Harness 提供源码与桌面壳等安装方式，具体以[官方仓库](https://github.com/deepseek-ai/DeepSeek-Harness)为准。通常：

```bash
# 示例（请按官方 README 的最新命令执行）
git clone https://github.com/deepseek-ai/DeepSeek-Harness.git
cd DeepSeek-Harness
# 按官方指引安装依赖并启动
```

!!! warning "别照抄"
    安装命令与依赖会随版本变化。**始终以官方 README 为准**，本站不完整复述易变细节。

## 2. 跑通第一个插件

- 用一个最小的「hello-world 插件」验证插件体系工作正常。
- 插件是 DSH 的核心扩展单元，接口约定详见[进阶开发](advanced.md)。

## 3. 跑通第一个 Agent 任务

- 给一条简单指令，看 DSH 如何**调度子代理**完成。
- 观察它使用了哪些工具 / Skill，以及**工作区与回滚**如何记录。

## 4. 官方入口

- 官方仓库：<https://github.com/deepseek-ai/DeepSeek-Harness>
- 官方文档与示例：以仓库 README / docs 为准

!!! note "下一步"
    - 想理解内部原理 → 看[架构](architecture.md)
    - 想扩展（子代理 / 工作流 / 多模型）→ 看[进阶开发](advanced.md)
    - 想查概念 → 看[术语表](glossary.md)
