# DeepSeek-Harness-Community · DSH 实践站

> ⚠️ **社区第三方文档 & 模板仓库，非 DeepSeek 官方项目，不代表官方立场。**
> 同步上游：[deepseek-harness](https://github.com/deepseek-ai/deepseek-harness).

[![Docs](https://img.shields.io/badge/Docs-GitHubPages-blue)](https://lili-sxdt.github.io/deepseek-harness-community/)

**定位**：把官方能力翻译成中文场景化教程与**经过验证的模板**，让不同水平用户都能**立刻行动**。
**原则**：小而美 · 不误导 · 模板优先。只做精选，不做配置字段百科 / 命令大全 / 大论坛——这些交给官方文档。

## 📚 站点（5 入口）

- **首页**：任务路由（不了解 / 首次 / 在用 / 做扩展）+ 热门模板 + 主按钮「从第一个模板开始」
- **入门**：它是什么 + 最简安装 + 5 分钟跑通第一个示例
- **进阶实践**：Skill · Workflow · Subagent · 自定义 Agent
- **模板库**：精选模板（标 版本/用途/难度/验证状态）
- **帮助与贡献**：FAQ · 故障排查 · 版本 · 贡献

👉 **https://lili-sxdt.github.io/deepseek-harness-community/**

## 📂 仓库结构

```
deepseek-harness-community/
├── docs/                # VitePress 文档源文件
├── templates/           # 可直接复用模板（标版本/验证状态，未实测不上）
├── scripts/             # 版本跟踪脚本（check_upstream.py，自动更新版本页）
├── state/               # 版本跟踪状态
└── .github/workflows/   # GitHub Pages 构建 + 版本列表自动更新
```

## 📌 站规

1. **小而美**：只做"能立刻行动"的精选，不铺全。
2. **不误导**：每个模板/教程标注版本与验证状态；没实测就写「未实测 · 以官方为准」。
3. **模板优先**：核心价值是"经过验证、可直接复用的模板"。

## 🚀 快速开始

1. 看[入门](/guide/intro)：它是什么 + 最简安装 + 5 分钟跑通。
2. 复制 `templates/configs/minimal.config.yaml` 或 `templates/deploy/docker-compose.yml` 跑通。
3. 想深入 → [进阶实践](/guide/advanced)。

## ⚠️ 重要提醒

1. 本仓库**不存放任何 API Key、模型权重**，密钥用环境变量注入。
2. 上游迭代快，模板/教程标注版本；**以官方为准**。

## 🤝 贡献

欢迎提交实测跑通的模板（按[贡献指南](/contributing)填全元数据）、排错案例、文档修正。
[仓库](https://github.com/lili-sxdt/deepseek-harness-community) · [Discussions](https://github.com/lili-sxdt/deepseek-harness-community/discussions)

## 🔗 相关项目

- 上游：[deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) · Hermes-Agent · vLLM / Ollama
