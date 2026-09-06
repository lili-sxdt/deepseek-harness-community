import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "DeepSeek-Harness-Community",
  description: "DeepSeek-Harness 第三方社区文档、模板库",
  // base 必须与 GitHub 仓库名逐字一致（普通 ASCII 连字符）
  base: '/deepseek-harness-community/',
  lang: 'zh-CN',
  lastUpdated: true,

  head: [
    // favicon 在 head 里是原始 <link>，VitePress 不会自动加 base，这里写完整路径
    ['link', { rel: 'icon', href: '/deepseek-harness-community/favicon.svg' }]
  ],

  themeConfig: {
    // logo 用不带 base 的路径，VitePress 会自动接上 base（放进 docs/public/ 保证能被访问）
    logo: '/logo.svg',
    nav: [
      { text: '指南', link: '/guide/intro' },
      { text: '配置参考', link: '/config/config-yaml' },
      { text: '模板库', link: '/templates/' },
      { text: '故障排查', link: '/troubleshoot/common-issues' },
      { text: '版本跟踪', link: '/version-status' },
      { text: 'GitHub', link: 'https://github.com/lili-sxdt/deepseek-harness-community' }
    ],
    sidebar: {
      '/guide/': [
        {
          text: '入门指南',
          items: [
            { text: '概念总览', link: '/guide/intro' },
            { text: '最小示例', link: '/guide/minimal-demo' }
          ]
        }
      ],
      '/config/': [
        {
          text: '配置参考',
          items: [
            { text: 'config.yaml 总览', link: '/config/config-yaml' }
          ]
        }
      ],
      '/templates/': [
        { text: '模板库', link: '/templates/' }
      ],
      '/troubleshoot/': [
        {
          text: '故障排查',
          items: [
            { text: '常见问题', link: '/troubleshoot/common-issues' }
          ]
        }
      ]
    },
    search: { provider: 'local' },
    outline: { level: [2, 3] },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/lili-sxdt/deepseek-harness-community' }
    ],
    footer: {
      message: '社区第三方站点，非 DeepSeek 官方，仅供学习研究使用。',
      copyright: 'DeepSeek-Harness-Community'
    }
  }
})
