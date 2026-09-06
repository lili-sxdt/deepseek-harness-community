# 概念总览

> 用大白话讲清 DeepSeek-Harness 的核心组件。让你还没装就大概知道它怎么运转。

## 一句话

DeepSeek-Harness 是一套**把大模型评测、Agent 编排、结果采集串起来**的框架。你做的是"喂数据 → 调模型 → 拿结果"，它帮你把中间环节编排好。

## 核心组件（大白话）

| 组件 | 大白话职责 |
| --- | --- |
| **harness core** | 总调度：读配置、编排流程、串起所有环节 |
| **adapter** | 模型适配器：对接不同模型（DeepSeek / OpenAI / Ollama / vLLM / 通义 / Claude） |
| **runner** | 执行器：真正跑一条评测/任务 |
| **evaluator** | 评测器：按指标打分（文本 / 代码 / 多轮 Agent） |
| **agent runtime** | Agent 运行时：跑 Agent 工作流、工具调用、多智能体协作 |
| **storage** | 存储：结果落地（本地 json / sqlite / csv / parquet / 外部数据库） |

## 一次任务的流转

```
config.yaml ──► harness core ──► adapter(模型) ──► runner ──► evaluator ──► storage
                 │                                                        │
                 └────────── agent runtime（Agent 任务时启用）──────────────┘
```

简单说：**config 说了"用什么模型、跑什么、怎么评分"**，core 照着编排，结果进 storage。

## 关键点

- **配置驱动**：几乎全靠 `config.yaml` 描述，改配置即改行为。
- **可插拔**：换模型=换 adapter；换评分=换 evaluator；都能自定义。
- **数据落盘**：评测结果、日志、缓存、数据集都有固定目录（见[目录结构](/guide/dir-struct)）。

## 下一步

- 想跑通第一个 → [最小示例](/guide/minimal-demo)
- 想看懂配置 → [配置参考](/config/config-yaml)
- 想直接抄配置 → [模板库](/templates/)
