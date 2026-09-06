---
layout: home

hero:
  name: DeepSeek-Harness-Community
  text: 社区实战文档与模板库
  tagline: 第三方非官方｜部署 · 评测 · Agent编排 · 排错
  image:
    src: /logo.svg
    alt: DeepSeek-Harness-Community
  actions:
    - theme: brand
      text: 📖 快速开始
      link: /guide/intro
    - theme: alt
      text: 📂 模板库
      link: /templates/
    - theme: alt
      text: ⚠️ 故障排查
      link: /troubleshoot/common-issues

features:
  - icon: 🚀
    title: 多方式部署指南
    details: 源码、Docker Compose、多GPU服务器部署，含RTX Pro多卡落地经验
  - icon: ⚙️
    title: 完备配置参考
    details: 大量实战 config.yaml 模板；多模型适配器、Agent工作流、压测参数详解
  - icon: 🤖
    title: Agent & 多智能体实战
    details: Hermes-Agent 对接、工具调用、分支循环编排、自定义工具开发示例
  - icon: 📊
    title: 评测与数据集
    details: 自定义评测集导入、结果导出、后处理脚本，可复现实验配置规范
  - icon: 🛠️
    title: 二次开发
    details: 新增适配器、自定义评测指标、调用 Harness REST API
  - icon: 🩹
    title: 踩坑知识库
    details: 依赖报错、OOM、超时、版本迁移坑点汇总，高频错误速查
---

::: warning 声明
本站为**社区第三方站点**，不属于 DeepSeek 官方，仅供学习研究使用。
上游项目：[deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)，文档验证版本见[版本状态](/version-status)。
:::

## 什么是 DeepSeek-Harness-Community

官方文档偏向接口说明，缺少落地实战案例。本站点目标：降低上手门槛，沉淀社区实战经验：

- 零基础跑通 harness
- 本地私有模型接入评测流水线
- 搭建 Agent 多智能体实验
- 服务器多卡环境稳定运行
- 快速定位报错，减少调试时间

## 适合人群

- 在本地/服务器做大模型评测的开发者
- 研究 Agent、多智能体工作流
- 需要二次扩展 harness 能力
- 遇到各种部署配置报错查找解决方案

## 快速路径

1. 📖 [概念总览](/guide/intro) —— 先搞懂核心组件
2. 🔧 [最小示例](/guide/minimal-demo) —— 跑通第一条任务
3. 📂 [模板库](/templates/) —— 复制现成配置直接改
4. 🩹 [故障排查](/troubleshoot/common-issues) —— 遇到报错优先看这里

## 版本状态

| Harness 版本 | 本站验证状态 | 迁移说明 |
| --- | --- | --- |
| 0.1.2-alpha | ✅ 已验证 | 当前主力版本 |
| 0.1.1 | ⚠️ 部分兼容 | 配置存在 breaking-change，见[迁移说明](/troubleshoot/common-issues) |

> 上游版本更新后会逐步验证并更新本站内容（由[自动更新流水线](/version-status)跟踪）。

## 参与社区

- 💬 [Discussions](https://github.com/lili-sxdt/deepseek-harness-community/discussions) 提问交流
- 📝 [仓库](https://github.com/lili-sxdt/deepseek-harness-community) 提交模板、案例、文档修改
