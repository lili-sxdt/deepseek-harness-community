# DeepSeek-Harness-Community · DSH 学习站

> ⚠️ **社区第三方文档站，非 DeepSeek 官方项目，不代表官方立场。**
> 同步上游：[deepseek-harness](https://github.com/deepseek-ai/deepseek-harness).

[![Docs](https://img.shields.io/badge/Docs-GitHubPages-blue)](https://lili-sxdt.github.io/deepseek-harness-community/)

**定位**：把 DeepSeek Harness（DSH）翻译成中文**场景化教程**，用**一门课**带一个完全不懂的人，从入门走到精通。
**原则**：理解深入 · 动手简单 · 说人话（专业词配中文解释，不堆术语）。

## 📚 这是一门课，不是文档索引

用**四堂课**沿一条路走，每课有明确目标、能动手、能验收：

| 课 | 名字 | 你在哪 | 学完你会到哪 |
|---|---|---|---|
| ① | [认知上手](/learn/level-1/) | 完全没用过 | **会用**：装好、跑通、派件活 |
| ② | [概念运用](/learn/level-2/) | 会用但在懵 | **懂 + 会用对**：看懂名词、选对工具 |
| ③ | [应用构建](/learn/level-3/) | 想为工作做东西 | **用 DSH 做东西**：写 skill、串流程 |
| ④ | [框架扩展](/learn/level-4/) | 想调成合自己用 | **精通**：加一个新能力，为你的活服务 |

从 ① 走到 ④，就是完整走一遍**"从入门到精通"**。

## 📂 仓库结构

```
deepseek-harness-community/
├── docs/                # VitePress 文档源（首页 + 四课 + 版本）
│   ├── learn/           #   四个课，每课一个 section + 2 级子页
│   └── version-status.md#   版本列表（自动同步官方）
├── scripts/              # 版本跟踪脚本（check_upstream.py，自动更新版本页）
├── state/                # 版本跟踪状态
└── .github/workflows/   # GitHub Pages 构建 + 版本列表自动更新
```

## 📌 站规

1. **一门课**：只做"能带你走完整条路"的四课，不铺全、不做百科。
2. **不误导**：具体命令/字段标注版本与"以官方为准"；上游迭代快，别用旧内容套新版本。
3. **理解深入 · 动手简单**：理解挖到底，动手从最简能跑开始；全程说人话。

## 🚀 开始

1. 从[第一课 · 认知上手](/learn/level-1/)开始，一路走到底。
2. 想快速看最新版本 → [版本列表](/version-status)。

## ⚠️ 重要提醒

1. 本仓库**不存放任何 API Key、模型权重**，密钥用环境变量注入。
2. 上游迭代快，教程/示例标注版本；**以官方为准**。

## 🤝 贡献

欢迎提交你能实测跑通的**真实案例/课程练习**、中文术语修正、章节补充。
[仓库](https://github.com/lili-sxdt/deepseek-harness-community) · [Discussions](https://github.com/lili-sxdt/deepseek-harness-community/discussions)

## 🔗 相关项目

- 上游：[deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) · Hermes-Agent · vLLM / Ollama
