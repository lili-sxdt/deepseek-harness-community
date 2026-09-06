import { defineConfig } from 'vitepress'

// 「帮助中心」侧栏（多个路径共用）
const helpSidebar = [
  {
    text: '帮助中心',
    items: [
      { text: '帮助中心', link: '/help' },
      { text: 'FAQ', link: '/faq' },
      { text: '故障排查', link: '/troubleshoot/common-issues' },
      { text: '版本', link: '/version-status' },
      { text: '贡献指南', link: '/contributing' },
      { text: '最佳实践', link: '/best-practices' }
    ]
  }
]

export default defineConfig({
  title: "DSH 实践站",
  description: "DeepSeek-Harness 中文场景化实践站：把官方能力变成不同水平用户都能立刻行动的路径与模板。",
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
      { text: '社区首页', link: '/' },
      { text: '入门指南', link: '/guide/intro' },
      { text: '进阶实践', link: '/guide/advanced' },
      { text: '模板中心', link: '/templates/' },
      { text: '帮助中心', link: '/help' },
      { text: 'GitHub', link: 'https://github.com/lili-sxdt/deepseek-harness-community' }
    ],
    sidebar: {
      '/guide/': [
        {
          text: '入门指南',
          items: [
            { text: '入门指南', link: '/guide/intro' },
            { text: '最小示例', link: '/guide/minimal-demo' }
          ]
        },
        {
          text: '进阶实践',
          items: [
            { text: '概览', link: '/guide/advanced' },
            { text: '插件（Plugin）', link: '/guide/plugin' },
            { text: '技能（Skill）', link: '/guide/skill' },
            { text: '工作流（Workflow）', link: '/guide/workflow' },
            { text: '子代理（Subagent）', link: '/guide/subagent' },
            { text: '自定义 Agent & 预设', link: '/guide/custom-agent' }
          ]
        },
        {
          text: '参考',
          items: [
            { text: '配置参考', link: '/config/config-yaml' },
            { text: '目录结构', link: '/guide/dir-struct' }
          ]
        }
      ],
      '/config/': [
        {
          text: '参考',
          items: [
            { text: '配置参考', link: '/config/config-yaml' },
            { text: '目录结构', link: '/guide/dir-struct' }
          ]
        }
      ],
      '/templates/': [
        { text: '模板中心', link: '/templates/' }
      ],
      '/help/': helpSidebar,
      '/faq/': helpSidebar,
      '/troubleshoot/': helpSidebar,
      '/version-status/': helpSidebar,
      '/contributing/': helpSidebar,
      '/best-practices/': helpSidebar
    },
    search: { provider: 'local' },
    outline: { level: [2, 3] },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/lili-sxdt/deepseek-harness-community' }
    ],
    footer: {
      message: '社区第三方站点，非 DeepSeek 官方，仅供学习研究使用。',
      copyright: 'DSH 实践站 · DeepSeek-Harness-Community'
    }
  }
})
