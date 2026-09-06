# 入门指南

> 一句话：极端简单——它是什么、能干什么、5 分钟跑起来。具体命令以官方为准。

## 它是什么（大白话）

DeepSeek-Harness 是一个**开源工具**，能帮你做三件事：

- **测模型**：把同一个问题丢给好几个 AI 模型，看谁答得好、谁更值（评测）
- **让 AI 分工**：几个 AI 各干一块，拼成一个完整任务（多智能体）
- **测机器**：看你的服务器一次能跑多少、快不快（压测）

它最大的特点：**一切皆插件**——模型、工具、技能、子代理、提示词都能**拆成可插拔的零件**，想换就换、想加就加。

一句话：**它不是替你干活的"聊天助手"，而是让你"自己搭一个测 AI、编排 AI 的实验台"。** 你不用懂底层，**填一份配置**就能跑起来。

## 和常见的工具有啥区别

| | DeepSeek-Harness | Codex / Claude Code / 豆包 等 |
| --- | --- | --- |
| 它是 | **你搭的实验台**（测/比/编排） | **现成的助手**（帮你写/聊/做） |
| 你做什么 | 自己定任务、接模型、跑评测、编排智能体 | 直接让它干活 |
| 额外 | 还能把 Codex / Claude Code **收编成子代理** | — |

> 一句话：Codex / Claude Code / 豆包是"用助手"；DeepSeek-Harness 是"搭实验台"。后者能把前者收编。（WorkBuddy / 豆包 细节以官方为准）

## 最简安装（先跑起来）

> 最简单一条路：**Docker 一条命令起**，最省心（详见[进阶指南](/guide/advanced)讲源码/Docker/npm 的区别）。具体以官方为准。

```bash
git clone https://github.com/deepseek-ai/deepseek-harness
cd deepseek-harness
# 用仓库里的 docker-compose 一键起（或用官方安装方式）
docker compose up -d
```

## 5 分钟跑通第一个示例

1. 复制 `templates/configs/minimal.config.yaml`，把 `model` 名改成你的后端（Ollama / vLLM 等）。
2. 跑 `harness run --config config.yaml`。
3. 看结果输出（评测结果、日志）。

> 完整一步步见[最小示例](/guide/minimal-demo)；出问题看[故障排查](/troubleshoot/common-issues)。

## 下一步

- 想彻底搞懂**怎么装、怎么配** → [进阶指南](/guide/advanced)
