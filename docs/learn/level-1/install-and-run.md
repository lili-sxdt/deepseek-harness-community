---
title: 快速装通
---

# 快速装通：把它装好、跑起来

> 这一页是**手把手**。你不用懂原理，照着做就行。每一步我都写了"做成什么样算对""卡住了怎么办"。

## 开始前，先准备两样东西

1. 一台能联网的电脑（Windows / macOS / Linux 都行）。
2. 装了 **Docker**（下面最省心的一条路用它）。没装 Docker 的话，先去装一个 Docker Desktop。

> ⚠️ 说明：DeepSeek Harness（下称 DSH）迭代很快，**具体字段、版本以[版本列表](/version-status)和我们标"以官方为准"的地方为准**。这里教你的是**最主流、最省心的一条路**，你先把它跑通，别的以后再说。

## 第 1 步：把 DSH 下载到本机

打开终端（Windows 是 PowerShell，mac 是"终端"），进入你想放代码的文件夹，然后**复制这条命令**回车：

```
git clone https://github.com/deepseek-ai/deepseek-harness
```

✅ **做对了的样子**：屏幕上出现一行行下载进度，最后回到命令行，并多出一个 `deepseek-harness` 文件夹。

❌ **卡住了**：提示 `git not found` → 说明你电脑没装 git，先装一个（或改用 Docker 直接拉镜像，见下面「救急」）。

## 第 2 步：进入这个文件夹

```
cd deepseek-harness
```

✅ **做对了的样子**：命令行前面的路径变成了 `...deepseek-harness`。

## 第 3 步：用 Docker 一键起

```
docker compose up -d
```

✅ **做对了的样子**：它开始拉取镜像、创建容器，最后显示一串服务的名字，并回到命令行。

❌ **卡住了**：提示 `docker not found` → Docker 没装或没启动，先打开 Docker Desktop 等它跑起来再试。

## 第 4 步：确认它真的起来了

```
docker compose ps
```

✅ **做对了的样子**：列出一排服务，状态是 `running`（正在跑）。**看到 running，就说明装通了。**

## 记住这一个词：以官方为准

装通只是第一步。DSH 的配置项、命令名会随版本变化，**你以后遇到"怎么配"的问题，答案在[版本页](/version-status)和官方仓库里，别背旧命令。**

## 救急（卡住了看这里）

| 你看到 | 大概率是 | 一句话解法 |
|---|---|---|
| `git not found` | 没装 git | 装个 git 再重跑第 1 步 |
| `docker not found` | Docker 没装/没启动 | 打开 Docker Desktop，等它 ready 再跑 |
| 下到一半断了 | 网络问题 | 重跑那条命令（会断点续传） |
| `docker compose` 不认 | compose 版本太旧 | 升级 Docker Desktop 到最新 |
| 起完 `ps` 却是 `exited` | 有服务没起来 | 跑 `docker compose logs` 看哪个崩了，多半是缺配置，捡[版本页]对照 |

## 走完全程，你做了什么？

- ✅ 下载了 DSH、用 Docker 起了服务、确认它能跑。
- 这就是"安装 + 跑通"——你离"会用"只差**真的派一件活**了。

接着走 → **动手实战**（派一件真实小活）。
