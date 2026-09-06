# Subagent 子代理

> 把外部 Agent（如 Codex、Claude Code）**收编成自己的"子代理"**，统一调度、分工、汇总。**具体做法以官方为准。**

## 它解决什么

- 你已经习惯用 Codex / Claude Code 干活，但想让它们**听统一调度**、一起完成一个任务。
- 或者：你想让"一个主 Agent 指挥几个小 Agent"分工协作。

## 怎么用（最小思路）

1. 定义哪些外部 Agent 作为**子代理**（如 Codex、Claude Code、或自定义）。
2. 由**主 Agent**统一调度：分派任务 → 子代理各自做 → 回传结果 → 汇总。
3. 结果合并成一个输出。

> 🔴 **未实测**：收编方式、接口、调度约定**以官方为准**（这是 Harness 相对独特的定位——把外部 Agent 变子代理）。

## 什么时候用

- 想让不同 Agent 各干一块、协作完成一个复杂任务。
- 想统一调度你熟悉的 Codex / Claude Code。

## 下一步

- 和 Workflow 组合 → [Workflow](/guide/workflow)
- 想定义专属角色 → [自定义 Agent](/guide/custom-agent)
- 出问题 → [故障排查](/troubleshoot/common-issues)
