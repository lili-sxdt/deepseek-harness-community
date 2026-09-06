---
layout: home

hero:
  name: DSH中文社区
  text: 驾驭深度智能，释放无限可能
  tagline: 中文场景化实践 · 模板优先 · 由易到难
  image:
    src: /logo.svg
    alt: DeepSeek Harness 中文社区
  actions:
    - theme: brand
      text: 先看入门指南
      link: /guide/intro
    - theme: alt
      text: 从第一个模板开始
      link: /templates/
---

::: warning 声明
本站为**社区第三方站点**，非 DeepSeek 官方，仅供学习研究使用。具体命令/字段以官方为准。
:::

## 它是什么

**DeepSeek Harness** 是一个用于运行和管理 DeepSeek 模型的轻量化框架。它负责把模型、提示词、工具调用和任务流程连接起来，让开发者能够更方便地构建自动化问答、代码生成、智能代理等应用。

> 它最大的特色是**一切皆插件**：模型、工具、提示词、子代理都能插拔；也**可通过适配器接入多种模型**（本地 Ollama / vLLM、OpenAI 兼容等）。见[进阶实践](/guide/advanced)。

## 不同用户，看这里

| 你的情况 | 去哪 |
| --- | --- |
| 完全不了解 | [入门指南](/guide/intro) —— 是什么、怎么装、跑通第一个 |
| 第一次使用 | [最小示例](/guide/minimal-demo) —— 5 分钟跑通 |
| 已经在用 | [进阶实践](/guide/advanced) —— Skill / Workflow / Subagent / 自定义 Agent |
| 正在开发扩展 | [模板中心](/templates/) · [帮助中心](/help) |

## 版本与更新

| 当前 | 说明 |
| --- | --- |
| ✅ 验证版本 | 见[版本列表](/version-status)（每天自动同步官方） |
| 📦 npm | `@deepseek-ai/dsh` |

> 上游迭代快，**以"版本列表"标注为准**，别拿旧配置套新代码。

## 它擅长啥、不擅长啥

- **擅长**：多模型评测、Agent 编排、压测、把 Codex/Claude 收编成子代理。
- **不是**：替你干活的"聊天助手"；也不是官方文档的替代。
