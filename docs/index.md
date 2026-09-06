---
layout: home

hero:
  name: DSH 实践站
  text: 把 DeepSeek-Harness 变成你能立刻行动的路径
  tagline: 中文场景化实践 · 模板优先 · 由易到难
  image:
    src: /logo.svg
    alt: DSH 实践站
  actions:
    - theme: brand
      text: 先看入门指南
      link: /guide/intro
    - theme: alt
      text: 从第一个模板开始
      link: /templates/
---

::: warning 声明
本站为**社区第三方站点**，非 DeepSeek 官方，仅供学习研究使用。上游：[deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)。具体命令/字段以官方为准。
:::

## 🧭 新手指引：第一次进来，按这条走

> 别慌，按顺序来，3 步就有成就感。

1. **花 3 分钟看[入门指南](/guide/intro)** —— 它是什么、怎么装、5 分钟跑通第一个示例
2. **复制[模板](/templates/)跑通一次** —— 最小配置 + Docker 一键启动，先跑起来
3. **卡住看[帮助中心](/help)** —— FAQ、故障排查，别自己硬扛

## 热门模板

复制就能改、拿来跑。**只放"标了验证状态"的模板，没实测不虚标。**

| 模板 | 用途 | 怎么用 |
| --- | --- | --- |
| 最小配置 | 测一个模型（一次调用+一次评测） | 复制 → 改模型名/地址/数据集 → 跑 |
| Docker 一键部署 | 本地/服务器一条命令起 | 复制 → 改端口/挂载/模型端点 → `up -d` |

> 两个模板均标「**未实测 · 以官方为准**」（结构正确，但尚未帮你验证跑通）。等你实测后再升级"✅ 已验证"。

## 按你现在要做什么进入

| 你的情况 | 去 |
| --- | --- |
| 完全不了解 | [入门指南](/guide/intro) |
| 第一次使用 | [最小示例](/guide/minimal-demo) |
| 已经在用 | [进阶实践](/guide/advanced) |
| 正在开发扩展 | [模板中心](/templates/) · [帮助中心](/help) |

## 用它做什么、不做什么

- **擅长**：多模型评测、Agent 编排、压测、把 Codex/Claude 收编成子代理。
- **不是**：替你干活的"聊天助手"；也不是官方文档的替代品。
