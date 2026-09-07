---
title: 文件系统
---

# 文件系统：DSH 是怎么组织数据的

> 这条路给了"想真正搞懂 DSH"的人。目录不只是"东西放哪"，更回答三件事：**为什么这么分、一次任务流经哪些文件、我想改 X 去哪。**

## 三层总览（先有全景）

```
① 配置区    ~/.dsh                ← 你的偏好（设置/角色/会话/凭证）
② 工作区    <workspace>（D:\DSH）  ← 你干活（项目/技能/工作协议）
③ 框架本体  desktop-shell/.../node_modules/@deepseek-ai  ← 系统引擎（别动）
```

## 第一问：为什么这么分？

- **配置区**：你的**全局偏好**，与具体项目无关（换任何项目都生效）。
- **工作区**：你**具体干活**的地方（研究协议、技能、项目成果）。
- **框架本体**：系统的**引擎**（223 个插件包），只可扩展、不可改。

> 原则：**"配置不混进项目、系统资产不复用进产物、引擎不让你改。"** 所以想改"个人设置"去配置区、想存"我的成果"去项目、碰引擎走"接缝"。

## 第二问：一次任务流经哪些文件？（动态视角，最值钱）

```
启动（dsh --profile web）
  → 读 settings.yaml        （默认模型 / 默认角色预设）
  → 读 profile（dsh.profile bundles + cordis.patch.yml）
  → 读 AGENTS.md            （工作协议，每次自动加载）
  → 按需读 .dsh/skills/*/SKILL.md （作业手册，做对应事才翻开）
  → 干活 → 写 sessions/<工作区>/session-<id>/  （每一步都记）
  → 交付 → 写 projects/ 或你指定的地方
```

## 第三问：我想改/想看 X，去哪个文件（导航索引）

| 我想…… | 去哪个文件 | 背后模块 |
|---|---|---|
| 换默认模型/主题 | `~/.dsh/settings.yaml` | `dsh-settings` |
| 换默认角色 | `~/.dsh/agent-presets` | `dsh-agent-presets` |
| 看会话 | `~/.dsh/sessions/<工作区>/session-<id>/` | `dsh-session` |
| 加一个技能 | 工作区 `.dsh/skills/<名>/SKILL.md` | `dsh-skill` + `dsh-skill-filesystem` |
| 注册一个工具 | `ctx.tools.register(defineTool(...))` | `dsh-tools` |
| 装一个插件 | `dsh plugin --profile <name> <pnpm args>` | `dsh` CLI |
| 存项目成果 | `projects/` | — |
| 放可复用脚本/文档 | `research-assistant/` | — |

## 系统对象卡（比"D 文件在哪"更本质）

把文件系统看成"**系统对象的投影**"——每个对象：谁读写、存哪、什么格式、动它后果：

| 系统对象 | 谁读写 | 存在哪 | 背后模块 | 动它后果 |
|---|---|---|---|---|
| 设置 | 你 / `dsh-settings` | `settings.yaml` | `dsh-settings` | 换默认模型 |
| 角色预设 | 你 / `dsh-agent-presets` | `.dsh/agent-presets` | `dsh-agent-presets` | 换默认角色 |
| 会话 | 系统 / `dsh-session` | `.dsh/sessions/.../session-<id>/` | `dsh-session` | 删 = 丢历史 |
| 技能 | 提供方 / `dsh-skill` | `.dsh/skills/<名>/SKILL.md` | `dsh-skill` | 加作业手册 |
| 工具 | 作者注册 / `dsh-tools` | `ctx.tools.register(defineTool)` | `dsh-tools` | 模型多本事 |
| 凭证 | 环境变量注入 | `.credentials.yaml` | `dsh-credentials` | 别外泄 |
| 工作协议 | 你 | `AGENTS.md` | `dsh-agent-instructions` | 每次自动生效 |
| 项目产物 | 你 | `projects/` | — | 你的成果 |

> 一句话：**读懂文件系统 = 懂"系统有哪些对象、各自谁读写、存哪、动了会怎样"。**

## 动手：看一次真的

挑一个照着看（都是这台机器上真实存在的）：
1. `C:\Users\11935\.dsh\settings.yaml` —— 看默认模型、默认角色。
2. `D:\DSH\.dsh\skills\data-analysis\SKILL.md`（任一技能）—— 看作业手册开头。
3. `C:\Users\11935\.dsh\sessions\--D-DSH--\session-<id>\` —— 看一次会话怎么被记。

---

*看完有了整体感，就去 [真实接口](/deep-dive/api) 看"怎么按真接口写东西"；或 [定位速查](/deep-dive/route) 想快速找到动哪儿。*
