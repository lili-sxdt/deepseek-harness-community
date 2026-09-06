# 模板中心

> 一句话：复制就能改的现成配置，拿来跑。只放"标了验证状态"的模板，没实测不虚标。

这里优先做**最简单、最常用**的 2 个模板。复制 → 改几处 → 跑，就能用起来。

## ① 最小配置（测一个模型）

- **用途**：一次模型调用 + 一次简单评测
- **文件**：`templates/configs/minimal.config.yaml`（[直接看](https://github.com/lili-sxdt/deepseek-harness-community/blob/main/templates/configs/minimal.config.yaml)）
- **怎么用（复制 → 改 → 跑）**：
  1. 复制到你的项目
  2. 改这三处：`model.provider`（deepseek/ollama/vllm…）、`model.base_url`（模型地址）、`eval.dataset`（你的题目）
  3. `harness run --config config.yaml` → 结果存 `./results`
- **验证状态**：⬜ 未实测 · 以官方为准（结构正确，尚未帮你验证跑通）

## ② Docker 一键部署（本地/服务器）

- **用途**：一条命令起
- **文件**：`templates/deploy/docker-compose.yml`（[直接看](https://github.com/lili-sxdt/deepseek-harness-community/blob/main/templates/deploy/docker-compose.yml)）
- **怎么用**：复制 → 改端口 / 挂载目录 / 模型端点 → `docker compose up -d`
- **验证状态**：⬜ 未实测 · 以官方为准

## 每个模板都会标什么

> 用途 / 难度 / **版本** / 依赖 / **复制→改** / 输入输出 / **已验证日期** / 风险。本站坚持：先实测、再标"✅ 已验证"，否则就诚实标"未实测"。

## 后续

- **脚本类**（解析结果、转数据集、画图）在补齐中。
- 等你/贡献者实测跑通更多场景 → 按元数据规范补上来（见[贡献指南](/contributing)）。
