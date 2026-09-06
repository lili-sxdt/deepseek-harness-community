# 进阶实践

> 一句话：学会基础后，用 **Skill / Workflow / Subagent / 自定义 Agent** 搭可复用的东西。它们都是"**一切皆插件**"的体现。具体语法以官方为准。

## 先懂插件：一切皆插件

DeepSeek-Harness 的核心理念是**一切皆插件**——模型、工具、技能、子代理、提示词都是可插拔单元。下面这几种能力就是"插件"的不同体现。详见[插件（Plugin）](/guide/plugin)。

## 这几种能力是什么

| 能力 | 一句话 | 你用它做什么 |
| --- | --- | --- |
| **插件 Plugin** | 一切皆插件的总理念 | 把 Agent 拆成可插拔的零件 |
| **Skill** | 可插拔的"能力包/技能"（按需加载） | 把某种"怎么做"封装成技能，随时调用 |
| **Workflow** | 编排方式（扇出 / 并行 / 流水线） | 让一次任务由多个步骤/代理组合完成 |
| **Subagent** | 子代理（可把 Codex / Claude Code 收编） | 把外部 Agent 变成自己的"手下"统一调度 |
| **自定义 Agent & 预设** | 预制角色 / 自定义预设 | 定义"某类任务由某角色来做"，或做成可复用的预设 |

## 从哪个开始

- 想懂核心理念 → [插件（Plugin）](/guide/plugin)
- 想"复用某个做法" → [Skill](/guide/skill)
- 想"把多步任务编排起来" → [Workflow](/guide/workflow)
- 想"让别的 Agent 给我打工" → [Subagent](/guide/subagent)
- 想"定义专属角色 / 预设" → [自定义 Agent & 预设](/guide/custom-agent)

## 通用建议

- 每种都配一个**最小示例 + 可复制模板**（见[模板库](/templates/)），先跑通再加复杂度。
- 组合起来用：比如「Skill × Workflow × Subagent」搭一个完整自动化。
- **密钥用环境变量**、**版本要核实**（见[最佳实践](/best-practices)）。

## 安装 / 配置（超链接到官方）

安装与 config 字段，官方文档最全；本站侧重"场景怎么用"。见[配置参考](/config/config-yaml)与官方 [deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)。
