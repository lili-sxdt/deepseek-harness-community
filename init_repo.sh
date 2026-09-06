#!/usr/bin/env bash
# ============================================================
#  init_repo.sh —— 一键本地初始化 + 绑定 + 推送 GitHub（macOS/Linux 版）
#
#  与 init_repo.ps1 等效，供 macOS / Linux 使用。
#  用法：在「仓库根目录（含 mkdocs.yml）」运行
#         bash init_repo.sh                              # 交互式，问 GitHub 地址
#         bash init_repo.sh "https://github.com/lili-sxdt/dsh-website.git"   # 直接给地址
#
#  提示：若直接执行（./init_repo.sh）先 chmod +x init_repo.sh
# ============================================================
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

# 0) 确认在仓库根目录（含 mkdocs.yml）
if [ ! -f "$ROOT/mkdocs.yml" ]; then
  echo "请在仓库根目录（含 mkdocs.yml）运行。当前：$ROOT" >&2
  exit 1
fi

# 1) 检查 git
if ! command -v git >/dev/null 2>&1; then
  echo "未找到 git，请先安装 Git。" >&2
  exit 1
fi

# 2) git 身份（首次提交需要）
NAME="$(git config --get user.name || true)"
EMAIL="$(git config --get user.email || true)"
if [ -z "$NAME" ] || [ -z "$EMAIL" ]; then
  read -rp "git 用户名: " NAME
  read -rp "git 邮箱: " EMAIL
  git config --global user.name "$NAME"
  git config --global user.email "$EMAIL"
fi

# 3) 初始化仓库
if [ ! -d "$ROOT/.git" ]; then
  echo "初始化 git 仓库..."
  git init
  git config core.longpaths true
else
  echo "已存在 git 仓库，跳过 init。"
fi

# 4) 主分支命名
git branch -M main

# 5) 需要 GitHub 仓库地址
REPO_URL="${1:-}"
if [ -z "$REPO_URL" ]; then
  read -rp "GitHub 仓库地址（直接回车跳过，默认 lili-sxdt/dsh-website）: https://github.com/lili-sxdt/dsh-website.git -> " REPO_URL
fi

# 6) 绑定远程
if [ -n "$REPO_URL" ]; then
  if git remote get-url origin >/dev/null 2>&1; then
    echo "origin 已绑定：$(git remote get-url origin)"
    read -rp "是否重设为 $REPO_URL ? [y/N] " ans
    case "$ans" in
      [yY]*) git remote set-url origin "$REPO_URL" && echo "已重置 origin -> $REPO_URL" ;;
    esac
  else
    git remote add origin "$REPO_URL"
    echo "已绑定 origin -> $REPO_URL"
  fi
fi

# 7) 首次提交（有提交则跳过）
if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
  git add -A
  git commit -m "init: DSH 参考站 + 自动更新流水线"
  echo "已创建首次提交。"
else
  echo "已有提交，跳过首次提交。"
fi

# 8) 推送
if [ -n "$REPO_URL" ]; then
  git push -u origin main
  echo "已推送 main 到远程。"
else
  echo "未提供仓库地址，跳过推送。"
fi

# 9) 下一步提示
cat <<'EOF'

OK，接下来请做这三件事：
  1) 回填 site_url：打开 mkdocs.yml，改成你的 GitHub Pages 地址。
  2) 开 Pages：仓库 Settings -> Pages -> Source 选 gh-pages 分支。
  3) 手动触发一次「自动检测更新」，确认自动更新能出 PR。
（完整步骤见 LAUNCH_GUIDE.md）
EOF
