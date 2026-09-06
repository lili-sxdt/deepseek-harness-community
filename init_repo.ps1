# ============================================================
#  init_repo.ps1 —— 一键本地初始化 + 绑定 + 推送 GitHub
#
#  用法（在仓库根目录，含 mkdocs.yml）：
#    .\init_repo.ps1                              # 回车即用默认仓库 lili-sxdt/dsh-website
#    .\init_repo.ps1 -RepoUrl "https://..."       # 直接给地址
#    .\init_repo.ps1 -SkipPush                    # 只初始化不推送
#
#  说明：新仓库没有提交时，git 会报 "unknown revision HEAD"，属正常，
#        脚本已按退出码判断，不会因此中断。
# ============================================================
[CmdletBinding()]
param(
    [string]$RepoUrl,            # 可选，直接给 https://github.com/lili-sxdt/dsh-website.git
    [string]$Remote = "origin",
    [switch]$SkipPush            # 可选，只初始化不推送
)

# 关键：设为 Continue，避免 git 在"空仓库无提交"时的正常报错中断脚本
$ErrorActionPreference = "Continue"

$root = (Resolve-Path .).Path
if (-not (Test-Path (Join-Path $root "mkdocs.yml"))) {
    Write-Warning "请在仓库根目录（含 mkdocs.yml）运行本脚本。当前：$root"
    exit 1
}

# 1) 检查 git
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "未找到 git。请先安装 Git 并加入 PATH。"
    exit 1
}

# 2) git 身份（首次提交需要）
$name = (git config --get user.name)
$email = (git config --get user.email)
if (-not $name -or -not $email) {
    Write-Host "首次使用，请先配置 git 身份（用于提交）：" -ForegroundColor Cyan
    $name = Read-Host "  git 用户名"
    $email = Read-Host "  git 邮箱"
    git config --global user.name $name
    git config --global user.email $email
}

# 3) 初始化仓库
if (-not (Test-Path (Join-Path $root ".git"))) {
    Write-Host "初始化 git 仓库..." -ForegroundColor Cyan
    git init
    git config core.longpaths true
} else {
    Write-Host "已存在 git 仓库，跳过 init。" -ForegroundColor Yellow
}

# 4) 主分支命名为 main
git branch -M main

# 5) 仓库地址：回车 = 默认仓库 lili-sxdt/dsh-website
$defaultRepo = "https://github.com/lili-sxdt/dsh-website.git"
if (-not $RepoUrl) {
    $RepoUrl = Read-Host "  GitHub 仓库地址（回车=默认 $defaultRepo）"
}
if (-not $RepoUrl) { $RepoUrl = $defaultRepo }

# 6) 绑定远程
$cur = (git remote get-url $Remote 2>$null)
if ($cur) {
    Write-Host "  $Remote 已绑定：$cur" -ForegroundColor Yellow
    if ((Read-Host "  是否重设为 $RepoUrl ? [y/N]") -match "^[yY]") {
        git remote set-url $Remote $RepoUrl
        Write-Host "  已重置 $Remote -> $RepoUrl" -ForegroundColor Green
    }
} else {
    git remote add $Remote $RepoUrl
    Write-Host "  已绑定 $Remote -> $RepoUrl" -ForegroundColor Green
}

# 7) 首次提交（用退出码判断是否有提交；空仓库无提交时 git 报错属正常，不影响）
git rev-parse --verify HEAD 2>$null | Out-Null
$hasCommit = ($LASTEXITCODE -eq 0)
if (-not $hasCommit) {
    git add -A
    git commit -m "init: DSH 参考站 + 自动更新流水线"
    Write-Host "已创建首次提交。" -ForegroundColor Green
} else {
    Write-Host "已有提交，跳过首次提交。" -ForegroundColor Yellow
}

# 8) 推送 main
if (-not $SkipPush) {
    git push -u origin main
    Write-Host "已推送 main 到远程。" -ForegroundColor Green
}

# 9) 下一步提示
Write-Host ""
Write-Host "OK，上线还差这一步（其余已就绪）：" -ForegroundColor Green
Write-Host "  1) 在 GitHub 仓库 Settings -> Pages -> Source 选 gh-pages 分支"
Write-Host "  2) 等 1-2 分钟，打开 https://lili-sxdt.github.io/dsh-website/ 确认上线"
Write-Host ""
Write-Host "（完整步骤见 LAUNCH_GUIDE.md）" -ForegroundColor Cyan
