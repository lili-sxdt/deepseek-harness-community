import { defineConfig } from 'vitepress'

// 每课一个 section，下面挂 2 级子页（二级侧栏）
// 名字统一 4 字基准：开课导览 · 知识点…… · 动手实战 · 出师检验
const learnSidebar = [
  {
    text: '认知上手',
    collapsed: false,
    items: [
      { text: '开课导览', link: '/learn/level-1/' },
      { text: '认识助手', link: '/learn/level-1/what-is-assistant' },
      { text: '快速装通', link: '/learn/level-1/install-and-run' },
      { text: '动手实战', link: '/learn/level-1/hands-on' },
      { text: '出师检验', link: '/learn/level-1/checkpoint' }
    ]
  },
  {
    text: '概念运用',
    collapsed: false,
    items: [
      { text: '开课导览', link: '/learn/level-2/' },
      { text: '架构总览', link: '/learn/level-2/architecture' },
      { text: '概念精讲', link: '/learn/level-2/concepts' },
      { text: '选型决策', link: '/learn/level-2/choose' },
      { text: '动手实战', link: '/learn/level-2/hands-on' },
      { text: '出师检验', link: '/learn/level-2/checkpoint' }
    ]
  },
  {
    text: '应用构建',
    collapsed: false,
    items: [
      { text: '开课导览', link: '/learn/level-3/' },
      { text: '构建总览', link: '/learn/level-3/overview' },
      { text: '编写技能', link: '/learn/level-3/skill' },
      { text: '流程编排', link: '/learn/level-3/pipeline' },
      { text: '动手实战', link: '/learn/level-3/hands-on' },
      { text: '出师检验', link: '/learn/level-3/checkpoint' }
    ]
  },
  {
    text: '框架扩展',
    collapsed: false,
    items: [
      { text: '开课导览', link: '/learn/level-4/' },
      { text: '扩展总览', link: '/learn/level-4/overview' },
      { text: '插件开发', link: '/learn/level-4/plugin' },
      { text: '架构解读', link: '/learn/level-4/structure' },
      { text: '毕业项目', link: '/learn/level-4/project' },
      { text: '出师检验', link: '/learn/level-4/checkpoint' }
    ]
  }
]

const versionSidebar = [
  {
    text: '版本与更新',
    items: [
      { text: '版本列表', link: '/version-status' }
    ]
  }
]

export default defineConfig({
  title: 'DSH中文社区',
  description: '从入门到精通：四堂课带你从会用 DSH，到把它调教成自己工作的一部分。',
  base: '/deepseek-harness-community/',
  lang: 'zh-CN',
  lastUpdated: true,

  head: [
    ['link', { rel: 'icon', href: '/deepseek-harness-community/favicon.svg' }],
    ['style', ':root{--vp-c-brand-1:#4a6fa5;--vp-c-brand-2:#3f5f8f;--vp-c-brand-3:#35507a;}']
  ],

  themeConfig: {
    logo: '/logo.svg',
    nav: [
      { text: '首页', link: '/' },
      { text: '认知上手', link: '/learn/level-1/' },
      { text: '概念运用', link: '/learn/level-2/' },
      { text: '应用构建', link: '/learn/level-3/' },
      { text: '框架扩展', link: '/learn/level-4/' },
      { text: '版本', link: '/version-status' }
    ],
    sidebar: {
      '/learn/': learnSidebar,
      '/version-status': versionSidebar
    },
    search: { provider: 'local' },
    outline: { level: [2, 3] },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/lili-sxdt/deepseek-harness-community' }
    ],
    footer: {
      message: '社区第三方站点，非 DeepSeek 官方，仅供学习研究使用。具体内容以官方与版本列表为准。',
      copyright: 'DSH中文社区'
    }
  }
})
