# -*- coding: utf-8 -*-
"""DSH (DeepSeek Harness) 架构图 —— matplotlib 原生渲染，输出 SVG + PNG。

分层 Agent 架构 + 「一切皆插件」视觉元素。坐标单位=画布像素。
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# 中文承载字体（Windows 微软雅黑优先，多兜底）；SVG 文字转路径，避免豆腐字
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "Noto Sans SC",
                                   "SimHei", "DejaVu Sans"]
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["svg.fonttype"] = "path"

# ---------------- 调色板（Flat-icon 风格，白底，技术蓝主色）----------------
BG         = "#ffffff"
TITLE      = "#0f172a"
SUB        = "#64748b"
LAYER_BG   = "#f8fafc"
LAYER_EDGE = "#cbd5e1"
NODE_FILL  = "#ffffff"
NODE_EDGE  = "#cbd5e1"
NODE_TX    = "#0f172a"
NODE_TXS   = "#64748b"
LBL_TX     = "#475569"

# 语义色
ACCENT_FILL = "#eef2ff"   # 核心（Agent 核心）
ACCENT_EDGE = "#4d6bfe"
INPUT_FILL  = "#fffbeb"   # 输入层（暖黄）
INPUT_EDGE  = "#f59e0b"
SUBAG_FILL  = "#ecfdf5"   # 子代理（青绿）
SUBAG_EDGE  = "#10b981"
TOOL_FILL   = "#f5f3ff"   # 工具/模型（紫）
TOOL_EDGE   = "#8b5cf6"
MEM_FILL    = "#f0f9ff"   # 记忆/工作区（天蓝）
MEM_EDGE    = "#0284c7"

ARR_MAIN    = "#4d6bfe"   # 主执行流
ARR_MEM     = "#0ea5e9"   # 记忆读/写
ARR_PLUG    = "#f59e0b"   # 插件总线


# ---------------- 画布 ----------------
W, H = 1240, 1010
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H)
ax.set_aspect("equal"); ax.axis("off")
fig.patch.set_facecolor(BG)


# ---------------- 辅助函数 ----------------
def node(cx, cy, w, h, title, subtitle=None, fill=NODE_FILL, edge=NODE_EDGE,
         lw=1.6, tfs=13, sfs=9.5, tcol=NODE_TX):
    box = FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                         boxstyle="round,pad=0,rounding_size=9",
                         linewidth=lw, edgecolor=edge, facecolor=fill,
                         mutation_scale=1, zorder=3)
    ax.add_patch(box)
    if subtitle:
        ax.text(cx, cy + h * 0.10, title, ha="center", va="center",
                fontsize=tfs, fontweight="bold", color=tcol, zorder=4)
        ax.text(cx, cy - h * 0.26, subtitle, ha="center", va="center",
                fontsize=sfs, color=NODE_TXS, zorder=4)
    else:
        ax.text(cx, cy, title, ha="center", va="center",
                fontsize=tfs, fontweight="bold", color=tcol, zorder=4)


def layer(x, yb, w, h, label):
    box = FancyBboxPatch((x, yb), w, h,
                         boxstyle="round,pad=0,rounding_size=12",
                         linewidth=1.4, edgecolor=LAYER_EDGE, facecolor=LAYER_BG,
                         linestyle=(0, (5, 3)), mutation_scale=1, zorder=1)
    ax.add_patch(box)
    ax.text(x + 12, yb + h - 15, label, ha="left", va="center",
            fontsize=12, fontweight="bold", color=LBL_TX, zorder=2)


def arrow(p0, p1, color=ARR_MAIN, lw=1.9, style="-|>", ls="solid", rad=0.0,
          ms=15):
    a = FancyArrowPatch(p0, p1, arrowstyle=style, mutation_scale=ms,
                        lw=lw, color=color, linestyle=ls, zorder=5,
                        connectionstyle="arc3,rad=%.3f" % rad,
                        shrinkA=4, shrinkB=4)
    ax.add_patch(a)
    return a


def alabel(mid, text, color=ARR_MAIN, fs=10.5):
    ax.text(mid[0], mid[1], text, ha="center", va="center", fontsize=fs,
            color=color, fontweight="bold", zorder=6,
            bbox=dict(boxstyle="round,pad=0.22", fc="white", ec="none", alpha=0.96))


# ---------------- 标题 ----------------
ax.text(W / 2 - 60, H - 22, "DeepSeek Harness · 一体化 Agent 运行 / 开发框架",
        ha="center", va="center", fontsize=21, fontweight="bold", color=TITLE, zorder=4)
ax.text(W / 2 - 60, H - 52,
        "Everything is a Plugin —— 模型 · 工具 · Skill · 子代理 皆可插拔，像搭积木一样组装 Agent",
        ha="center", va="center", fontsize=11.5, color=SUB, zorder=4)

# 「一切皆插件」徽标（右上角）
plug = FancyBboxPatch((W - 250, H - 82), 218, 40,
                      boxstyle="round,pad=0,rounding_size=20",
                      linewidth=1.6, edgecolor=ARR_PLUG, facecolor=INPUT_FILL,
                      mutation_scale=1, zorder=4)
ax.add_patch(plug)
ax.text(W - 141, H - 62, "★ 一切皆插件", ha="center", va="center",
        fontsize=13, fontweight="bold", color="#b45309", zorder=5)


# ---------------- 主列分层 ----------------
MX, MW = 40, 780            # 主列 x / 宽

# ① 输入层
layer(MX, 850, MW, 112, "① 输入层 · Input")
node(175, 902, 190, 58, "用户 / 开发者", "User", fill=INPUT_FILL, edge=INPUT_EDGE, lw=1.8, tfs=13.5)
node(430, 902, 190, 58, "CLI · 命令行", "terminal", fill=INPUT_FILL, edge=INPUT_EDGE, lw=1.8)
node(665, 902, 150, 58, "Web GUI", "浏览器", fill=INPUT_FILL, edge=INPUT_EDGE, lw=1.8)

# ② Agent 核心
layer(MX, 640, MW, 160, "② Agent 核心 · Orchestrator")
node(185, 720, 200, 86, "编排 / 推理循环", "reasoning loop", fill=ACCENT_FILL, edge=ACCENT_EDGE, lw=2.4, tfs=13.5)
node(430, 720, 160, 64, "规划器", "planner", fill=ACCENT_FILL, edge=ACCENT_EDGE, lw=2.0)
node(630, 720, 150, 64, "任务调度", "dispatch", fill=ACCENT_FILL, edge=ACCENT_EDGE, lw=2.0)

# ③ 子代理层
layer(MX, 450, MW, 112, "③ 子代理层 · Sub-Agents　（可收编外部 Agent）")
node(175, 502, 190, 58, "Claude Code", "子代理", fill=SUBAG_FILL, edge=SUBAG_EDGE, lw=1.8, tfs=13)
node(430, 502, 190, 58, "Codex", "子代理", fill=SUBAG_FILL, edge=SUBAG_EDGE, lw=1.8)
node(665, 502, 160, 58, "Skill 代理", "自定义", fill=SUBAG_FILL, edge=SUBAG_EDGE, lw=1.8)

# ④ 工具 & 模型层
layer(MX, 270, MW, 112, "④ 工具 & 模型层 · Tools & Models　（可插拔）")
node(175, 322, 190, 58, "多模型适配", "flexible LLM", fill=TOOL_FILL, edge=TOOL_EDGE, lw=1.8)
node(430, 322, 190, 58, "工具调用", "APIs · 搜索 · 代码", fill=TOOL_FILL, edge=TOOL_EDGE, lw=1.8)
node(665, 322, 160, 58, "Skills", ".dsh/skills", fill=TOOL_FILL, edge=TOOL_EDGE, lw=1.8)


# ---------------- 侧列：记忆 & 工作区 ----------------
REM_X, REM_W = 860, 320
layer(REM_X, 450, REM_W, 322, "⑤ 记忆 & 工作区")
node(REM_X + REM_W / 2, 730, 250, 64, "上下文窗口", "短期 · context", fill=MEM_FILL, edge=MEM_EDGE, lw=1.8, tfs=12.5)
node(REM_X + REM_W / 2, 640, 250, 64, "状态记忆 · 研究日志", "state_memory", fill=MEM_FILL, edge=MEM_EDGE, lw=1.8, tfs=12.5)
node(REM_X + REM_W / 2, 550, 250, 64, "持久化 · 工作区", "git · 回滚 / 后悔机制", fill=MEM_FILL, edge=MEM_EDGE, lw=1.8, tfs=12.5)


# ---------------- 箭头 ----------------
# ①→② 任务/指令
arrow((430, 848), (430, 806)); alabel((430, 828), "触发 / 指令", ARR_MAIN)
# ②→③ 分派（两条向外）
arrow((300, 632), (225, 566)); alabel((240, 600), "分派", ARR_MAIN)
arrow((560, 632), (625, 566))
# ②→④ 工具调用（走 子代理节点之间间隙，避让 Codex）
arrow((535, 634), (535, 390))
arrow((551, 390), (551, 634), color=ARR_MAIN, ls="dashed")
alabel((543, 616), "工具调用 · 多模型", ARR_MAIN)
# ②↔⑤ 记忆 读/写
arrow((770, 700), (852, 700), color=ARR_MEM, style="<|-|>", ls="dashed")
alabel((812, 682), "读 / 写", ARR_MEM, fs=10)
# （响应/产物 回传用户：由图例「插件/回传」与工具回传虚线表达，避免左缘拥挤）


# ---------------- 图例 ----------------
ly = 200
ax.text(60, ly + 55, "图例 Legend", fontsize=12.5, fontweight="bold", color=LBL_TX)
arrow((70, ly + 25), (150, ly + 25), color=ARR_MAIN); alabel((160, ly + 25), "任务 / 执行流", "#334155", 10)
arrow((70, ly - 10), (150, ly - 10), color=ARR_MEM, style="<|-|>", ls="dashed"); alabel((160, ly - 10), "记忆 读 / 写", "#334155", 10)
arrow((70, ly - 45), (150, ly - 45), color=ARR_PLUG, style="-|>", ls="dashed"); alabel((160, ly - 45), "插件 / 回传", "#334155", 10)

# 底部一句话
ax.text(60, 120, "核心思路：把 Agent 拆成可插拔的零件（模型 · 工具 · Skill · 子代理），由统一的编排循环组装、调度、记忆与回滚。",
        fontsize=11, color=SUB, va="center", zorder=4)


# ---------------- 导出 ----------------
out = r"D:\DSH\research-assistant\demo-foundation\dsh-website\figures\dsh-architecture"
fig.savefig(out + ".svg", format="svg", bbox_inches="tight", pad_inches=0.05)
fig.savefig(out + ".png", format="png", dpi=200, bbox_inches="tight", pad_inches=0.05)
print("[OK] saved:", out + ".svg", "and", out + ".png")
