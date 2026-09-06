# 上线引导（Go-Live Guide）

> 把「第三方的 DSH 参考站」从本地推上云端并跑起自动更新。**按顺序做一遍即可。**
> 技术栈：**MkDocs(Material) + GitHub Pages + GitHub Actions**；无需后台、无需额外凭据。

## 这套结构长什么样

```
dsh-website/                ← 整个文件夹就是你的 GitHub 仓库根
├─ mkdocs.yml               站点配置（导航/主题/搜索/每页更新时间）
├─ docs/                    内容存放处（改这里 = 改网站）
│  ├─ index.md  快速上手  进阶开发  架构  术语表  FAQ  更新日志
│  └─ assets/dsh-architecture.png
├─ scripts/check_dsh_updates.py   自动检测更新脚本
├─ state/last_seen.json           状态文件（记住"上次版本"）
└─ .github/workflows/             云端自动化
   ├─ update.yml   定时检测新版本 → 开 PR 待你审
   └─ publish.yml  PR 合并 → 构建并上线
```

**一图看懂流水线**：
```
每天自动 ─► 检测官方新版本 ─► 生成"纯事实草稿" ─► 开 PR ─► 你审(补点评) ─► 合并 ─► 自动上线
```

---

## 一、一次性准备

- 一个 GitHub 账号。
- （可选，推荐）本机装好 Python 3.10+，用于**本地预览**（不装也行，云端会自己构建）。

---

## 二、把内容推上 GitHub（关键）

!!! warning "关键：一定要用 git，别用网页上传"
    「每页最后更新」来自 **git 提交历史**。如果用 GitHub 网页上传文件，没有历史，日期会变成"构建日"，参考站的"信息日期"就失效了。**请用下面的 git 方式推。**

**方式 A：一键脚本（推荐）。** 在 `dsh-website` 目录里运行：

```powershell
.\init_repo.ps1
```

它会自动：`git init` → 首次提交 → 绑定 `origin` → 推送 `main`。按提示填入你的 GitHub 仓库地址即可（也可用 `.\init_repo.ps1 -RepoUrl "https://github.com/lili-sxdt/dsh-website.git"` 免提问）。若只初始化不推送：`.\init_repo.ps1 -RepoUrl "..." -SkipPush`。

**方式 B：手动命令（备选）。** 若不想用脚本，手动执行：

```bash
git init
git add -A
git commit -m "init: DSH 参考站 + 自动更新流水线"
git branch -M main

# 在 GitHub 上新建一个空仓库（别勾选 README），拿到地址后：
git remote add origin https://github.com/lili-sxdt/dsh-website.git
git push -u origin main
```

> 推上去后，`publish.yml` 会**自动构建**并把站推到 `gh-pages` 分支。

---

## 三、开启 GitHub Pages（一次性）

1. 打开你的仓库 → **Settings → Pages**。
2. **Build and deployment → Source** 选 **Deploy from a branch**。
3. **Branch** 选 **`gh-pages`** → **`/ (root)`** → Save。
4. 稍等一两分钟，得到网址：`https://lili-sxdt.github.io/dsh-website/`。
5. 把这个网址回填进 `mkdocs.yml` 的 `site_url`（顺带把标题里的占位符也改成你的），再 push 一次。

首次若没自动部署，到 **Actions** 页手动触发一次 `构建并发布` 即可。

---

## 四、把「自动更新」跑起来（一次性）

- `update.yml` 默认**每天 09:00 UTC** 自动检查 DSH 官方新版本；检测到就生成草稿并**开一个 PR**。
- 第一次建议**手动触发一次**，看看流程：仓库 → **Actions → `自动检测更新` → Run workflow**。
- 如果本地用了 `--sample` 跑过，`state/last_seen.json` 会记录示例版本，不影响真实检测。

**人工审核（你的日常工作，每周 5 分钟）**：
1. 收到自动 PR「🤖 检测到 DSH 新版本，请审阅后合并」。
2. 核对版本号 / 日期 / 官方说明。
3. 补上「**值得关注点**」那列（这是第三方视角，需你判断）。
4. **合并** → 自动触发发布，直接上线。**不合并就关掉 PR**，下次会再检测。

!!! note "不想用自动更新？"
    删除 `.github/workflows/update.yml` 即可，改为手动维护 `docs/changelog.md`。其余不受影响。

---

## 五、日常怎么用（就两件事）

| 场景 | 你只需要 |
|---|---|
| DSH 出新版 | 审一个自动 PR（补点评 → 合并） |
| 改网站内容 | 改 `docs/*.md` → `git push` → 自动上线 |
| 改导航/主题 | 改 `mkdocs.yml` |

---

## 六、本地预览（推荐，改内容前先看效果）

在本机 `dsh-website` 目录：

```bash
pip install -r requirements.txt
mkdocs serve
```

浏览器打开 `http://127.0.0.1:8000`，实时预览、改即所见。满意后 push 上线。

---

## 七、常见问题排查

| 现象 | 处理 |
|---|---|
| 站点没上线/没更新 | 看 Actions 是否跑绿；确认 Pages 分支是 `gh-pages` |
| 更新日志没自动生成 | 手动触发一次 `自动检测更新`；确认 `update.yml` 权限已设 `contents/pull-requests: write` |
| 每页日期显示"构建日" | 说明用了网页上传无 git 历史 → 改用 git push |
| `mkdocs gh-deploy` 权限报错 | 确认仓库默认分支是 `main`，且 `publish.yml` 有 `permissions: contents: write` |
| 中文乱码 | 不会，全程 UTF-8；若控制台乱码只是显示问题 |

---

## 八、上线检查单

- [ ] `git push` 成功，Actions 两个工作流都配置好
- [ ] 起了 Pages，`gh-pages` 分支上线，URL 可访问
- [ ] 手动触发一次 `自动检测更新`，看到了 PR
- [ ] 本地 `mkdocs serve` 能跑、中文/图片正常
- [ ] `docs/changelog.md` 的插入标记 `<!-- AUTO-INSERT-HERE -->` 完好（自动追加依赖它）

---

## 九、维护节奏（省心版）

- **每周**：审一次自动更新 PR（唯一高频动作）。
- **每季度**：扫一遍「快速上手 / 进阶 / FAQ」是否落后。
- **每半年**：复核「架构 / 术语表」（页脚会显示最后更新日期，据此判断）。
