# -*- coding: utf-8 -*-
"""check_dsh_updates.py —— 自动检测 DeepSeek Harness 官方新版本，生成更新日志纯事实草稿。

设计要点：
- 只抓"版本 / 日期 / 官方 release 说明"，生成【纯事实】草稿行；
  "值得关注点"列留待研究者审阅时判断补充（第三方视角，不自动）。
- 幂等：已记录过的版本不会重复插入。
- 通过 GitHub Actions 定时调用；检测到新版本就改文件 → 工作流自动开 PR → 人审 → 合并上线。

用法：
    python scripts/check_dsh_updates.py              # 联网，默认 dry-run（只打印，不写入）
    python scripts/check_dsh_updates.py --apply      # 联网并写入 changelog + 更新状态
    python scripts/check_dsh_updates.py --sample     # 用内置示例数据（无网络），本地验证
    python scripts/check_dsh_updates.py --sample --apply
"""
import argparse
import datetime
import json
import os
import re
import sys

REPO = "deepseek-ai/DeepSeek-Harness"
API = "https://api.github.com/repos/{0}/releases?per_page=10".format(REPO)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # 仓库根
STATE = os.path.join(ROOT, "state", "last_seen.json")
CHANGELOG = os.path.join(ROOT, "docs", "changelog.md")
MARKER = "<!-- AUTO-INSERT-HERE -->"

# 示例数据：仅用于 --sample 本地验证（非真实发布内容）
SAMPLE_RELEASES = [
    {"tag_name": "0.1.0-rc.6", "published_at": "2026-09-02T10:00:00Z",
     "name": "v0.1.0-rc.6", "body": "新增多模态能力；改进子代理调度；修复若干问题。"},
    {"tag_name": "0.1.0-rc.5", "published_at": "2026-08-20T10:00:00Z",
     "name": "v0.1.0-rc.5", "body": "优化插件系统；完善 Windows 运行时。"},
]


def load_state():
    if os.path.exists(STATE):
        # 用 utf-8-sig：既能读无 BOM，也能自动剔除有 BOM 的文件（防 Windows BOM 坑）
        with open(STATE, encoding="utf-8-sig") as f:
            return json.load(f)
    return {"latest_tag": None, "seen_tags": []}


def save_state(state):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    with open(STATE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def fmt_date(iso):
    try:
        d = datetime.datetime.fromisoformat(str(iso).replace("Z", "+00:00"))
        return d.strftime("%Y-%m-%d")
    except Exception:
        return str(iso)[:10]


def escape_cell(text):
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def make_row(rel):
    tag = rel.get("tag_name", "?")
    date = fmt_date(rel.get("published_at", ""))
    body = escape_cell(rel.get("body", ""))[:80]      # 截断官方说明，避免撑爆表格
    return "| {0} | {1} | {2} | （待研究者补充） |".format(tag, date, body)


def insert_rows(changelog_path, rows):
    """把新行插到 MARKER 之后（最新在上）。幂等：同 tag 已存在则跳过。"""
    with open(changelog_path, encoding="utf-8") as f:
        text = f.read()
    existing = set(re.findall(r"^\|\s*([^\s|]+)\s*\|", text, re.M))
    new_rows = [r for r in rows
                if re.match(r"^\|\s*([^\s|]+)\s*\|", r).group(1) not in existing]
    if not new_rows:
        return False, text
    lines = text.splitlines()
    idx = next((i for i, l in enumerate(lines) if MARKER in l), None)
    if idx is None:
        raise RuntimeError("changelog 缺少插入标记：{0}".format(MARKER))
    lines[idx + 1:idx + 1] = new_rows + [""]          # 插在标记下一行之前
    return True, "\n".join(lines)


def get_releases(sample):
    """获取 DSH 官方全部 release 版本（分页拉取，不再只取最近 10 个）。"""
    if sample:
        return SAMPLE_RELEASES
    import requests
    releases = []
    page = 1
    while True:
        url = "https://api.github.com/repos/{0}/releases?per_page=100&page={1}".format(REPO, page)
        try:
            r = requests.get(url, timeout=25, headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "dsh-researcher",
            })
            r.raise_for_status()
        except Exception as e:
            # 抓取失败视为无更新（no-op），避免 workflow 因此失败
            print("[no-op] 抓取 release 失败：{0}".format(e))
            return []
        data = r.json()
        if not isinstance(data, list) or not data:
            break
        releases.extend(data)
        if len(data) < 100:
            break
        page += 1
    if not releases:
        print("[no-op] 未获取到 release 数据")
        return []
    return releases


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="写入 changelog 与状态（缺省 dry-run 只打印）")
    ap.add_argument("--sample", action="store_true", help="用内置示例数据本地验证（无网络）")
    args = ap.parse_args()

    releases = get_releases(args.sample)
    if not releases:
        return 0

    state = load_state()
    seen = set(state.get("seen_tags", []))
    new = [rel for rel in releases if rel.get("tag_name") not in seen]
    latest = releases[0].get("tag_name", "?")

    if not new:
        print("[no-op] 无新版本（当前最新 {0}）".format(latest))
        return 0

    print("[detect] 发现 {0} 个新版本：{1}".format(len(new), ", ".join(r["tag_name"] for r in new)))
    rows = [make_row(rel) for rel in new]

    if not args.apply:
        print("[dry-run] 将插入以下行（未写入）：")
        for r in rows:
            print("   ", r)
        print("[dry-run] 加 --apply 才会真正写入。")
        return 0

    changed, new_text = insert_rows(CHANGELOG, rows)
    if not changed:
        print("[no-op] 新版本已在 changelog 中，跳过写入")
    else:
        with open(CHANGELOG, "w", encoding="utf-8") as f:
            f.write(new_text)
        state["latest_tag"] = latest
        state["seen_tags"] = sorted(seen | {r["tag_name"] for r in new})
        save_state(state)
        print("[write] 已插入 {0} 行到 changelog；state.latest_tag={1}".format(len(rows), latest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
