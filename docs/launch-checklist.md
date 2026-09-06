# 上线检查单

> 给站点维护者用的上线 / 维护清点清单（可逐项勾选）。完整步骤见仓库根的 [上线引导](LAUNCH_GUIDE.md)。

## 一次性：初始化与上线

- [ ] 在 GitHub 建好一个**空的**仓库（不勾选 README / .gitignore）
- [ ] 在仓库根目录运行 `.\init_repo.ps1`（Windows）或 `bash init_repo.sh`（macOS/Linux），完成 init + 首次提交 + 绑定远程 + 推送
- [ ] 回填 `mkdocs.yml` 的 `site_url` 为你的 GitHub Pages 地址（`https://lili-sxdt.github.io/dsh-website/`）
- [ ] 仓库开启 Pages：Settings → Pages → Source 选 **`gh-pages`** 分支
- [ ] 能看到站点首页正常打开（含架构图、中文不乱码）
- [ ] 手动触发一次「自动检测更新」工作流，确认它**开出一个 PR**

## 自动更新：PR 审核（每次有新版本）

- [ ] 核对版本号 / 日期 / 官方说明是否正确
- [ ] 补充「值得关注点」一列（第三方视角，需人工判断）
- [ ] 确认无误后合并（合并后自动构建并上线）
- [ ] 若不采用，关闭 PR（下次会重新检测）

## 日常维护：内容更新

- [ ] 改 `docs/*.md` 后 `git push`，确认自动上线
- [ ] 每季度扫一遍「快速上手 / 进阶 / FAQ」是否落后
- [ ] 每半年复核「架构 / 术语表」（看页脚最后更新日期）
- [ ] 更新日志由自动流水线维护，无需手改

## 故障排查

- [ ] 站点没上线 → 看 Actions 是否跑绿；确认 Pages 分支是 `gh-pages`
- [ ] 更新日志没自动生成 → 手动触发一次；确认 `update.yml` 有 push/pull-requests 权限
- [ ] 每页日期显示"构建日" → 说明用了网页上传无 git 历史，改用 git push
