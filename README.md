# DeepSeek-Harness-Community

> ⚠️ **本项目为社区第三方文档 & 模板仓库，非 DeepSeek 官方项目，不代表官方立场**
> 同步上游：[deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)，文档验证版本见[版本状态](/version-status)。

[![Docs](https://img.shields.io/badge/Docs-GitHubPages-blue)](https://lili-sxdt.github.io/deepseek-harness-community/)

社区实战手册、配置模板库、排错知识库，弥补官方文档实战案例不足。
聚焦本地部署、多模型评测、Agent 编排、多卡服务器落地、二次开发。

## 📚 文档站点

👉 **https://lili-sxdt.github.io/deepseek-harness-community/**

## 📂 仓库结构

```
deepseek-harness-community/
├── docs/                # VitePress 文档源文件
├── templates/           # 可直接复用模板
│   ├── deploy/          # docker-compose 部署模板
│   ├── configs/         # harness config.yaml 各类场景配置
│   ├── datasets/        # 评测样例数据集
│   └── scripts/         # 结果解析、数据集转换辅助脚本（待补充）
├── scripts/             # 版本跟踪脚本（check_upstream.py）
├── state/               # 版本跟踪状态
└── .github/workflows/   # GitHub Pages 构建 + 版本跟踪
```

## ✨ 提供什么

- 完整中文实战文档：架构拆解、部署指南、配置字段详解
- 大量实战 yaml 模板：模型接入、Agent 多智能体、压测、评测任务
- 高频问题排查库，汇总上游 issue 踩坑经验
- 版本跟踪：自动检测上游新版本（半自动化）

## 🚀 快速开始

1. 阅读文档站[入门指南](/guide/intro)
2. 复制 `templates/configs/minimal.config.yaml` 最小配置跑通验证
3. 参考 `templates/deploy/docker-compose.yml` Docker 一键启动

## ⚠️ 重要提醒

1. 本仓库**不存储任何 API Key、模型权重**，密钥请使用环境变量注入
2. 上游迭代较快，文档标注已验证版本，高版本上游可能存在配置不兼容
3. 遇到问题优先查看[故障排查](/troubleshoot/common-issues)，欢迎到 Discussions 交流

## 🤝 贡献

欢迎提交：配置模板、排错案例、文档修正。
[提交到仓库](https://github.com/lili-sxdt/deepseek-harness-community)

## 🔗 相关项目

- 上游：[deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)
- Hermes-Agent
- vLLM / Ollama
