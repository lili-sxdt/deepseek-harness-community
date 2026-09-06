# 目录结构

> 说明 harness 装了之后，哪些目录放什么，方便你不迷路。**以官方为准，路径可能随版本微调。**

## 一般目录布局

```
<你的项目>/
├─ config.yaml          # 主配置（模型、评测、Agent、存储）
├─ configs/             # （可选）拆分多份配置
├─ datasets/            # 评测数据集
├─ results/             # 评测结果输出
├─ logs/                # 运行日志
├─ cache/               # 中间缓存
└─ prompts/             # Agent prompt 模板
```

## 各目录职责

| 目录 | 放什么 | 常见问题 |
| --- | --- | --- |
| `configs/` | 配置 | 别把密钥写里，用环境变量 |
| `datasets/` | 评测数据 jsonl | 格式对齐模板，见[模板库](/templates/) |
| `results/` | 评测结果 | 输出 json/csv，可用脚本解析 |
| `logs/` | 运行日志 | 排查用，级别见配置 `log_level` |
| `cache/` | 缓存 | 可定期清理 |
| `prompts/` | Agent prompt | 多智能体任务用 |

## 说明

- **输出可配置**：`storage.out_dir` 可改结果目录（见[配置参考](/config/config-yaml)）。
- **日志可控**：`storage.log_level` 调日志详略。
- 目录路径若与实际不符，以你运行的 harness 版本为准（看[版本状态](/version-status)）。
