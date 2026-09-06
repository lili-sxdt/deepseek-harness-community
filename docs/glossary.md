# 术语表

> 概念 ↔ 英文 ↔ 一句话解释 ↔ 相关章节。查得快，看得懂。

| 概念 | English | 一句话解释 | 相关章节 |
|---|---|---|---|
| 插件总线 | Plugin Bus | 让模型/工具/Skill/子代理都可插拔的统一机制 | [架构](architecture.md) |
| 一切皆插件 | Everything is a Plugin | DSH 的核心哲学：把 Agent 拆成可插拔零件 | [架构](architecture.md) |
| Skill | Skill | 按环节加载的能力包（SKILL.md） | [进阶开发](advanced.md) |
| 子代理 | Sub-Agent | 被统一调度、可收编（如 Claude Code / Codex）的 Agent | [进阶开发](advanced.md) |
| 工作流 | Workflow | 一对多扇出 / 并行 / 流水线的编排方式 | [进阶开发](advanced.md) |
| 编排器 | Orchestrator | 负责组装、调度、汇聚的 Agent 核心 | [架构](architecture.md) |
| 记忆 / 工作区 | Memory / Workspace | 上下文、状态记忆、持久化与回滚 | [架构](architecture.md) |
| 回滚 / 后悔机制 | Rollback | 允许回到之前状态，避免不可逆 | [架构](architecture.md) |
| 模型适配 | Model Adapter | 可插拔地接入不同 LLM 提供商 | [进阶开发](advanced.md) |
| Agent 预设 / 角色 | Agent Preset | 预定义的角色（如文献/分析/写作/审计） | [进阶开发](advanced.md) |
| 可复现 | Reproducible | 环境/数据/代码/种子可重跑出相同结果 | [进阶开发](advanced.md) |
| 审计 | Audit | 独立判断产物（PASS / CONDITIONAL / FAIL） | [进阶开发](advanced.md) |

!!! tip "使用建议"
    术语表是**快速索引**，点「相关章节」可跳到详细说明。新增概念时可在此加一行。
