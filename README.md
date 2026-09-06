# dsh-website —— DeepSeek Harness 第三方参考站

> 第三方研究者整理的 **DeepSeek Harness 参考读物**（方便自查，也供他人参考）。
> 归档位置：`research-assistant/demo-foundation/`（系统演示 / 测试归档，非研究产物）。

## 这是一个可直接上线的静态站
技术栈：**MkDocs(Material) + GitHub Pages + GitHub Actions**，无后台、无服务器、无需额外凭据。
自动更新：每天检测 DSH 官方新版本 → 生成纯事实草稿 → 开 PR → 你审（补点评）→ 合并 → 自动上线。

## 🚀 上线：请看《上线引导》
- **`LAUNCH_GUIDE.md`** —— 从本地推到 GitHub、开 Pages、跑起自动更新的完整步骤。

## 💻 一键初始化
- Windows：目录里运行 `.\init_repo.ps1`
- macOS/Linux：运行 `bash init_repo.sh`
- 自动完成 `git init` → 首次提交 → 绑定远程 → 推送 main。
- 可直接给地址免提问：`.\init_repo.ps1 -RepoUrl "https://github.com/lili-sxdt/dsh-website.git"`。

## 目录
```
├─ mkdocs.yml                  站点配置（导航/主题/搜索/每页更新时间）
├─ init_repo.ps1 / .sh         一键本地初始化（git init + 提交 + 推送）
├─ LAUNCH_GUIDE.md             上线引导（先看这个）
├─ docs/launch-checklist.md    上线/维护检查单（首页可勾选）
├─ docs/                       网站内容（改这里 = 改网站）
│  ├─ index.md  快速上手  进阶开发  架构  术语表  FAQ  更新日志
│  └─ assets/dsh-architecture.png
├─ scripts/check_dsh_updates.py  自动检测更新脚本
├─ state/last_seen.json          更新状态（记住上次版本）
├─ tools/draw_architecture.py    架构图生成脚本（matplotlib）
├─ figures/ 、 slides/           设计源文件（架构图 SVG/PNG、内容原型 HTML）
└─ .github/workflows/            云端自动化（update.yml / publish.yml）
```

## 本地预览
```bash
pip install -r requirements.txt
mkdocs serve      # 打开 http://127.0.0.1:8000
```

## 内容更新（日常）
改 `docs/*.md` → `git push` → 自动上线。DSH 出新版只需审一个自动 PR。

> 相关：内容原型见 `slides/`；首页主视觉架构图见 `figures/`。
