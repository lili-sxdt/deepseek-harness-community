---
title: 定位速查
---

# 定位速查：我能想到的，它接得住

> 你想做一件事，手边又记不清"去哪个文件、敲哪条命令"——来这里查。按"我想干嘛"找，一列查到：**目标 + 命令 + 背后模块**。

## 场景 / 定位

| 我想…… | 怎么办（文件 / 命令） | 背后模块 |
|---|---|---|
| 启动 DSH | `dsh web`（=`--profile web`） | `dsh` CLI |
| 启动其它 profile | `dsh --profile <name>` | `dsh` CLI |
| 换默认模型 | 改 `~/.dsh/settings.yaml` 的 `agent-default-model` | `dsh-settings` |
| 换默认角色 | 改 `~/.dsh/settings.yaml` 的 `agent-presets.default` | `dsh-agent-presets` |
| 加一个技能 | 建 `.dsh/skills/<名>/SKILL.md` | `dsh-skill` |
| 注册一个工具 | `ctx.tools.register(defineTool({...}))` | `dsh-tools` |
| 委托子代理 | `ctx.subagents` | `dsh-subagent` |
| 排一个工作流 | `ctx.workflowEngine` | `dsh-workflow` |
| 挂后台任务 | `ctx.jobs` | `dsh-jobs` |
| 接 MCP 工具 | `dsh-mcp-client` | `dsh-mcp-client` |
| 装一个插件 | `dsh plugin --profile <name> <pnpm args>` | `dsh` CLI |
| 看合并配置 | `dsh --dump-config` | `dsh` CLI |
| 改插件配置 | `cordis.patch.yml` | cordis patch |
| 看会话 | `~/.dsh/sessions/<工作区>/` | `dsh-session` |
| 存项目成果 | `projects/` | — |
| 放可复用脚本 | `research-assistant/scripts/` | — |

## 红线（务必记住）

1. **密钥**：`.credentials.yaml` 含密钥，**别外泄、别提交 git**。
2. **框架本体**：`node_modules/@deepseek-ai/*` 是系统引擎，**别改**，要扩展走 `ctx.*` 接缝。
3. **会话**：`.dsh/sessions/` 是过程记录，**别手动删**。

---

*配合 [文件系统](/deep-dive/filesystem) 看它对应到哪、[真实接口](/deep-dive/api) 看怎么写。*
