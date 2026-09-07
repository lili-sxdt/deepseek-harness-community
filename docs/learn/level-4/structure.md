---
title: 架构解读
---

# 架构解读：看懂 DSH 核心结构，知道该往哪儿加

> 前面你"加了一小块"。现在看懂它**整体怎么搭**，你就能清楚地"该往哪儿加、加在哪儿不会坏"。

## 📖 理解轨：DSH 这种"一切皆插件"的架构

DSH 的设计核心是"**一切皆插件**"——模型、工具、提示词、子代理，都能**拆成可插拔的零件**。

- **打个比方**：它像一套乐高——主体是固定的，你可以把不同的积木（模型、工具、智能体）插到对应接口上，随时换、随时加。
- **对你意味着**：你想加的东西，只要找到"它在哪个接口上"，插进去就行。

## 📖 真实接口：DSH 是靠"这些接缝"插东西的

> 以下名字**都来自这套 DSH 的真源码**（我读的是 `@deepseek-ai/dsh` 各包的中文说明文档）。DSH 本质是 **cordis 插件容器**，agent 通过一个 **`ctx` 上下文**暴露下面这些**接缝服务（seams）**——你要"插"什么，就往对应的 `ctx.*` 里插：

| 接缝 | 真模块 | 你用它做什么 |
|---|---|---|
| `ctx.agents` | `dsh-agent` | 创建/恢复/查找 agent（`create`/`resume`/`get`/`list`）；`AgentHandle` 有 `followup`/`steer`/`inject`/`cancel`/`whenIdle`/`dispose` |
| `ctx.tools` | `dsh-tools` | **注册工具**（`defineTool`）、按 agent 限制（`restrict`）、加策略（`guard`） |
| `ctx.subagents` | `dsh-subagent` | 委托子代理（命名提供者注册） |
| `ctx.skills` | `dsh-skill` | **技能注册表/提供方**（`register`/`registerProvider`） |
| `ctx.workflowEngine` | `dsh-workflow` | 工作流引擎（一次扇出很多再收回） |
| `ctx.jobs` | `dsh-jobs` | 后台任务（长任务/取消/完成通知） |
| `ctx.llm` | `dsh-llm` | 模型服务接口（换/接模型，provider-neutral） |
| `ctx.session` | `dsh-session` | 事件源会话存储 |
| Hooks | `dsh-hook-protocol` | Claude Code / Codex 钩子（匹配、编解码、合并） |
| MCP | `dsh-mcp-client` | 接 MCP 服务器，把它们发现的工具注册进 `ctx.tools` |

> 一句话：**教程里的 skill / workflow / subagent / tool / 换模型，在真源码里都是这些 `ctx.*` 接缝。** 想加新能力，就往对应接缝注册。

## 📖 真实环节：agent 运行 + 工具执行管道

一次运行，走的是**事件管道**：

**① Agent 循环（`dsh-agent-loop`）与 `agent/*` 事件**
- `agent/pre-step`——决定"放行/拒绝"这一步，可替换进入的消息
- `agent/request-error`——模型请求失败时重试
- `agent/turn-stopping`——一轮结束前运行（可用 `steer` 保持打开）
- `agent/status` / `created` / `disposed`——驱动 UI 与协调状态
- `agent/inbox/*`——收件箱逐消息同步

**② 工具执行管道（`dsh-tools`）**
```
tools/pre-execute  (允许 / 拒绝 / 询问)
        │
   ctx.tools.guard(单调守卫, 一票否决)
        │
   tools/execute    (环绕分发: 超时/重试/包装)
        │
   tools/post-execute (检查/替换结果)
        │
   finalizeContent    (工具定义持有的内容终结)
        │
   tools/result       (观测最终结果)
```
> 取消是**协作式**的：每个工具主体都拿到 `exec.signal`，必须观测它，超时/取消/未知工具会变成结构化错误（`TOOL_TIMEOUT`/`ABORTED`/`UNKNOWN_TOOL`），不会炸掉整个轮次。

## 🛠 写一个"真工具"（照着抄就能跑）

工具作者用 `ctx.tools.register(defineTool({...}))` 注册一个**类型化工具**（下面的例子来自真源码文档）：

```ts
import { readFile } from 'node:fs/promises'
import { defineTool } from '@deepseek-ai/dsh-tools'

ctx.tools.register(defineTool({
  name: 'read_file',                     // 模型看得到的工具名
  description: 'Read a file from disk.', // 描述
  parameters: {                          // 参数 schema（模型校验后才会执行）
    path:   { type: 'string', required: true, description: 'Absolute file path' },
    offset: { type: 'number' },
    limit:  { type: 'number' },
  },
  output: {                              // 规范输出声明
    schema: { type: 'string' },
    render: (_args, value) => [{ type: 'text', text: value }],
  },
  async execute(args, exec) {            // 只返回上面声明的 JSON 值
    return readFile(args.path, { encoding: 'utf8', signal: exec.signal })
  },
}))
```

> 你只要**改名字、描述、参数、execute 里真正干的事**，就是一个你自己的工具。注册后它的 schema 会自动进提示词，模型就能调它了。

## 🛠 一个"真插件"是怎么加载的

DSH 通过 `dsh` 启动器加载一堆插件（组合包），你要**加插件/改配置**走这几条：

| 你想做 | 命令 / 机制 |
|---|---|
| 启动某个 profile | `dsh --profile <name>`（`dsh web` = `--profile web`） |
| 加/装插件 | `dsh plugin --profile <name> <pnpm args>`（转到 profile 目录用 pnpm 装） |
| 看合并后的配置树 | `dsh --dump-config` / `--dump-default-config` |
| 改插件配置 | `cordis.patch.yml`（用户覆盖层，叠加在 `dsh.profile.bundles` 的 patch 之上） |

> profile 目录里有 `dsh.profile`（清单，含 `bundles` 顺序）和 `cordis.patch.yml`（你的覆盖配置）。**"一切皆插件"在这里是字面的**——每个 `@deepseek-ai/dsh-*` 都是一个 cordis 插件。

## 📌 以源码与官方为准

上面每一行都**来自这套 DSH 的真源码文档**（我读的是机器上的 `@deepseek-ai/dsh` 各包 `README.zh.md`，版本 `0.1.2-rc.1`）。但**确切的事件名、API 签名随版本变**——做开发前，请以这套装的**真源码**和你能访问到的**官方开发文档**为准（本页是把"概念图"换成了"真源码能对上"的版本）。

接着走 → **毕业项目**（收官：把你自己工作的需要做成一个真能力）。
