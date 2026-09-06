# -*- coding: utf-8 -*-
"""check_upstream.py —— 检测 DeepSeek-Harness 上游新版本，写入版本状态表（docs/version-status.md）。

- 只写入「版本号 + 待验证」事实草稿；「本站验证状态 / 迁移说明」由维护者人工填写。
- 幂等：已记录过的版本不会重复插入。
- 由 GitHub Actions 定时调用；检测到新版本就开 PR 待审核。

用法：
    python scripts/check_upstream.py --sample         # 本地用示例数据（无网络）
    python scripts/check_upstream.py --sample --apply
    python scripts/check_upstream.py --apply          # 联网+写入
"""
import argparse
import datetime
import json
import os
import re
import sys

REPO = "deepseek-ai/deepseek-harness"

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
STATE = os.path.join(ROOT, "state", "last_seen.json")
VSTATUS = os.path.join(ROOT, "docs", "version-status.md")
MARKER = "<!-- AUTO-INSERT-HERE -->"

SAMPLE = [
    {"tag_name": "dsh-v0.1.3-alpha.1", "published_at": "2026-09-04T10:00:00Z"},
    {"tag_name": "dsh-v0.1.2-alpha.5", "published_at": "2026-08-30T10:00:00Z"},
]


def load_state():
    if os.path.exists(STATE):
        with open(STATE, encoding="utf-8-sig") as f:   # 容忍 BOM
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


def make_row(rel):
    tag = rel.get("tag_name", "?")
    link = "https://github.com/{0}/releases/tag/{1}".format(REPO, tag)
    return "| [{0}]({1}) | ⬜ 待验证 | （待补充迁移说明） |".format(tag, link)


def insert_rows(path, rows):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    existing = set(re.findall(r"^\|\s*\[([^\]]+)\]", text, re.M))
    new_rows = [r for r in rows
                if re.match(r"^\|\s*\[([^\]]+)\]", r).group(1) not in existing]
    if not new_rows:
        return False, text
    lines = text.splitlines()
    idx = next((i for i, l in enumerate(lines) if MARKER in l), None)
    if idx is None:
        raise RuntimeError("version-status.md 缺少插入标记：{0}".format(MARKER))
    lines[idx + 1:idx + 1] = new_rows + [""]
    return True, "\n".join(lines)


def get_releases(sample):
    if sample:
        return SAMPLE
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
            print("[no-op] 抓取上游失败：{0}".format(e))
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
    ap.add_argument("--apply", action="store_true", help="写入版本状态表（缺省 dry-run）")
    ap.add_argument("--sample", action="store_true", help="用内置示例数据本地验证")
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
        print("[dry-run] 将插入：")
        for r in rows:
            print("   ", r)
        print("[dry-run] 加 --apply 才会写入。")
        return 0

    changed, new_text = insert_rows(VSTATUS, rows)
    if not changed:
        print("[no-op] 新版本已在表中，跳过")
    else:
        with open(VSTATUS, "w", encoding="utf-8") as f:
            f.write(new_text)
        state["latest_tag"] = latest
        state["seen_tags"] = sorted(seen | {r["tag_name"] for r in new})
        save_state(state)
        print("[write] 已插入 {0} 行；latest={1}".format(len(rows), latest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
