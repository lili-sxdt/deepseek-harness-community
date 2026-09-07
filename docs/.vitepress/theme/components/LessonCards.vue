<template>
  <div class="lesson-grid">
    <a
      v-for="card in cards"
      :key="card.href"
      class="lesson-card"
      :href="withBase(card.href)"
    >
      <strong>{{ card.name }}</strong>
      <em>{{ card.who }}</em>
      <span class="to">{{ card.to }}</span>
    </a>
  </div>
</template>

<script setup>
import { withBase } from 'vitepress'

const cards = [
  { name: '认知上手', who: '完全没用过', to: '学完 → 会用', href: '/learn/level-1/' },
  { name: '概念运用', who: '会用但在懵', to: '学完 → 懂 + 会用对', href: '/learn/level-2/' },
  { name: '应用构建', who: '想为工作做东西', to: '学完 → 用 DSH 做东西', href: '/learn/level-3/' },
  { name: '框架扩展', who: '想调成合自己用', to: '学完 → 精通', href: '/learn/level-4/' }
]
</script>
