# FAQ

> 常见疑问，按「关系 / 使用 / 排坑」归类。具体以官方为准。

## 关系类

**Q：DeepSeek-Harness 和 Codex / Claude Code 什么关系？**
A：它们可被 DeepSeek-Harness **收编为子代理**，统一调度——这是它相对独立的定位。详见[概念总览](/guide/intro)。

**Q：是官方项目吗？**
A：框架是 DeepSeek 开源的，但**本站是社区第三方**，非官方、不代表官方立场。

**Q：适合谁用？**
A：本地/服务器做评测的开发者、研究 Agent 多智能体的、要二次扩展的、遇到报错找方案的。见[首页](/)。

## 使用类

**Q：本地私有模型怎么接入？**
A：通过**模型适配器**（Ollama / vLLM / OpenAI 兼容等），改 config 的 `provider` / `base_url`。见[配置参考](/config/config-yaml)。

**Q：怎么快速跑通一次？**
A：最小 config + 一个数据集，跑 `harness run`。见[最小示例](/guide/minimal-demo)。

**Q：要什么环境？**
A：需要 python / node / docker 等（具体以官方为准）。见[概念总览](/guide/intro)。

## 排坑类

**Q：模型连不上 / 超时 / 鉴权错？**
A：先看[故障排查](/troubleshoot/common-issues)。

**Q：升级后配置不兼容？**
A：看[版本列表](/version-status)的迁移说明；**升级前先备份**旧配置。

**Q：密钥放在哪？**
A：**一律用环境变量**（`${API_KEY}`），别写进配置文件。见[最佳实践](/best-practices)。
