# config.yaml 配置参考

> 这是本站差异化核心：官方配置示例偏少，这里补全**带注释的实战配置**。**以官方字段为准**，字段名可能有版本差异，务必对照[版本状态](/version-status)。

## 字段总览

```yaml
# model：模型接入
model:
  provider: openai_compatible   # deepseek / openai_compatible / ollama / vllm / qwen / claude
  base_url: http://127.0.0.1:8000/v1
  api_key: ${API_KEY}           # 环境变量注入，绝不写死
  model: your-model-name
  # 进阶：并发、batch、上下文窗口、速率限制、重试、超时（见「性能调优」）

# eval：评测任务
eval:
  dataset: ./datasets/sample.jsonl
  metric: text_match            # 文本 / 代码 / 多轮 Agent 自定义
  # 自定义评测集：见 templates/datasets

# agent：Agent 工作流（多智能体任务启用）
agent:
  prompt: ./prompts/main.md
  tools: [search, code_exec]   # 工具调用
  loop: {max_iter: 5}          # 循环上限，防卡死
  # 分支/条件：if/else 编排

# storage：结果存储
storage:
  backend: json                # json / sqlite / csv / parquet / 外部数据库
  out_dir: ./results
  log_level: info
  telemetry: false             # 隐私：关遥测，很多用户关注
```

## 常见配置片段

- **接入本地模型**：[模板]多模型适配器
- **跑自定义问答评测集**：数据集模板 + 评分
- **多 Agent 协作**：agent 工作流模板
- **压测**：调并发/batch/超时参数

> 完整带注释模板见[模板库](/templates/)。

## 注意

- **字段随版本演进**：升级 harness 后配置可能不兼容，看[迁移说明](/troubleshoot/common-issues)。
- **密钥用环境变量**：惯例 `${VAR}` 或读取 shell 环境变量，别明文写。

## 下一步

- 直接抄配置 → [模板库](/templates/)
- 某个字段跑不通 → [故障排查](/troubleshoot/common-issues)
