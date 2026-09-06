# 最小示例

> 用最简单配置，跑通一次模型调用 + 一次简单评测。**以官方为准，这里给方向。**

## 前提

- 已安装 harness（见[概念总览](/guide/intro)里的部署指引，或直接复制[部署模板](/templates/)）。
- 有一个可用的模型接口（本地 Ollama / vLLM，或某家 OpenAI 兼容接口）。

## 最小 config.yaml

从[模板库](/templates/)复制 `minimal.config.yaml`，改三处即可：

```yaml
# 最小可运行配置示例
model:
  provider: openai_compatible   # 用 OpenAI 兼容接口
  base_url: http://127.0.0.1:8000/v1   # 你的本地模型端点
  api_key: ${API_KEY}                 # 用环境变量，别写死

eval:
  dataset: ./datasets/sample.jsonl     # 评测集
  metric: text_match                   # 一个最简单的评分
```

> ⚠️ **密钥一律用环境变量**（如 `${API_KEY}`），**绝不写进 config 文件**——这既安全也是规范。

## 跑起来

```bash
# 一键启动（若用 docker-compose 模板）
docker compose -f templates/deploy/docker-compose.yml up -d

# 跑一次评测
harness run --config config.yaml
```

## 你会看到什么

- 模型被调用、逐条评测
- 结果写入输出目录（json / csv）
- 面板 / 日志显示每条得分

## 出问题了？

- 模型连不上 → 看[故障排查](/troubleshoot/common-issues)
- 结果看不懂 → 用[脚本](/templates/)解析导出

## 下一步

- 想加场景 → [模板库](/templates/)里有很多现成配置可抄
- 想懂每个字段 → [配置参考](/config/config-yaml)
