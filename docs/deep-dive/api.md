---
title: 真实接口
---

# 真实接口：DSH 怎么"插"东西（来自真源码）

> 这里的内容**直接对应真源码**（机器上这套 `@deepseek-ai/dsh` 各包的中文说明文档，版本 `0.1.2-rc.1`）。标了"以源码/官方为准"的地方，做开发前请再核对。

## 一、接缝（seams）——你往哪儿插

DSH 是 **cordis 插件容器**，agent 通过一个 **`ctx` 上下文**暴露这些接缝：

| 接缝 | 真模块 | 你用它做什么 |
|---|---|---|
| `ctx.agents` | `dsh-agent` | 创建/恢复/查找 agent（`create`/`resume`/`get`/`list`）；`AgentHandle` 有 `followup`/`steer`/`inject`/`cancel`/`whenIdle`/`dispose` |
| `ctx.tools` | `dsh-tools` | 注册工具（`defineTool`）、按 agent 限制（`restrict`）、加策略（`guard`） |
| `ctx.subagents` | `dsh-subagent` | 委托子代理（命名提供者注册） |
| `ctx.skills` | `dsh-skill` | 技能注册表/提供方（`register`/`registerProvider`） |
| `ctx.workflowEngine` | `dsh-workflow` | 工作流引擎（一次扇出很多再收回） |
| `ctx.jobs` | `dsh-jobs` | 后台任务（长任务/取消/完成通知） |
| `ctx.llm` | `dsh-llm` | 模型服务接口（换/接模型，provider-neutral） |
| `ctx.session` | `dsh-session` | 事件源会话存储 |
| Hooks | `dsh-hook-protocol` | Claude Code / Codex 钩子（匹配、编解码、合并） |
| MCP | `dsh-mcp-client` | 接 MCP 服务器，把发现的工具注册进 `ctx.tools` |

## 二、真实环节（agent 运行 + 工具执行管道）

**① Agent 循环（`dsh-agent-loop`）与 `agent/*` 事件**
- `agent/pre-step`——决定"放行 / 拒绝"这一步，可替换进入的消息
- `agent/request-error`——模型请求失败时重试
- `agent/turn-stopping`——一轮结束前运行（可用 `steer` 保持打开）
- `agent/status` / `created` / `disposed`——驱动 UI 与协调状态
- `agent/inbox/*`——收件箱逐消息同步

**② 工具执行管道（`dsh-tools`）**
```
tools/pre-execute   (允许 / 拒绝 / 询问)
   │
ctx.tools.guard     (单调守卫，一票否决)
   │
tools/execute       (环绕分发：超时/重试/包装)
   │
tools/post-execute  (检查 / 替换结果)
   │
finalizeContent     (工具定义持有的内容终结)
   │
tools/result        (观测最终结果)
```
> 取消是**协作式**：每个工具主体拿到 `exec.signal` 并必须观测它；超时/取消/未知工具变成结构化错误（`TOOL_TIMEOUT`/`ABORTED`/`UNKNOWN_TOOL`），不会炸掉整个轮次。

## 三、写一个"真工具"（照着能跑）

```ts
import { readFile } from 'node:fs/promises'
import { defineTool } from '@deepseek-ai/dsh-tools'

ctx.tools.register(defineTool({
  name: 'read_file',                     // 模型看得到的工具名
  description: 'Read a file from disk.', // 描述
  parameters: {                          // 参数 schema（执行前校验）
    path:   { type: 'string', required: true, description: 'Absolute file path' },
    offset: { type: 'number' },
    limit:  { type: 'number' },
  },
  output: {
    schema: { type: 'string' },
    render: (_args, value) => [{ type: 'text', text: value }],
  },
  async execute(args, exec) {
    return readFile(args.path, { encoding: 'utf8', signal: exec.signal })
  },
}))
```

> 你只要**改名字、描述、参数、`execute` 里真正干的事**，就是一个你自己的工具。注册后 schema 自动进提示词，模型就能调它。

## 四、一个"真插件"怎么加载

| 你想做 | 命令 / 机制 |
|---|---|
| 启动某个 profile | `dsh --profile <name>`（`dsh web` = `--profile web`） |
| 加/装插件 | `dsh plugin --profile <name> <pnpm args>` |
| 看合并后的配置树 | `dsh --dump-config` / `--dump-default-config` |
| 改插件配置 | `cordis.patch.yml`（用户覆盖层，叠加在 `dsh.profile.bundles` 的 patch 上） |

> profile 目录里有 `dsh.profile`（清单，含 `bundles` 顺序）和 `cordis.patch.yml`（你的覆盖）。

## 五、以源码与官方为准

上面每一行都来自真源码文档（`@deepseek-ai/dsh` 各包 `README.zh.md`，版本 `0.1.2-rc.1`）。**确切的事件名、API 签名随版本变**——做开发前，请以你这套装的**真源码**与你能访问到的**官方开发文档**为准。

---

*看完接口，想"想做 X 去哪个文件/命令"，见 [定位速查](/deep-dive/route)；要整体感先看 [文件系统](/deep-dive/filesystem)。*
