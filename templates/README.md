# 模板库 Templates

> 可直接下载、复制修改。**每个模板标注：适用场景、修改要点、测过的版本。**

## 结构

```
templates/
├─ deploy/
│  └─ docker-compose.yml       Docker 一键部署
├─ configs/
│  └─ minimal.config.yaml      最小可运行配置
├─ datasets/                    评测样例数据（待补充）
└─ README.md
```

## 约定

1. **密钥一律用环境变量**（`${VAR}`），禁止明文写入配置文件。
2. 字段名随上游版本变化，以[版本状态](../docs/version-status.md)为准。
3. 每个模板的「测过版本」仅供参考，落前先自己验证。

## 回填

跑通某个场景后，**欢迎把你的可用配置/案例回填到本站**（提交 PR / Discussions），共建社区。
