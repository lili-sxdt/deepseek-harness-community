<template>
  <div class="hp-wrap">
    <div class="hp-brand">
      <h1 class="hp-title">DSH中文社区</h1>
      <p class="hp-sub">DeepSeek Harness</p>
      <p class="hp-sub2">从入门到精通</p>
      <div class="hp-actions">
        <a class="action primary" :href="withBase('/learn/level-1/')">从第一课开始</a>
        <a class="action ghost" :href="withBase('/version-status')">看最新版本</a>
      </div>
    </div>

    <div class="hp-cards">
      <a
        v-for="card in cards"
        :key="card.href"
        class="hp-card"
        :href="withBase(card.href)"
      >
        <strong>{{ card.name }}</strong>
        <em>{{ card.who }}</em>
        <span class="to">{{ card.to }}</span>
      </a>
    </div>
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

<style scoped>
.hp-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 56px;
  max-width: 1080px;
  margin: 0 auto;
  padding: 40px 32px;
  min-height: calc(100vh - var(--vp-nav-height) - 80px);
}

.hp-brand {
  flex: 1 1 320px;
  max-width: 440px;
}

.hp-title {
  font-size: 48px;
  line-height: 1.1;
  font-weight: 700;
  margin: 0 0 10px;
  background: linear-gradient(120deg, var(--vp-c-brand-1), var(--vp-c-brand-3));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.hp-sub {
  font-size: 22px;
  color: var(--vp-c-text-2);
  margin: 0;
}

.hp-sub2 {
  font-size: 20px;
  color: var(--vp-c-text-2);
  margin: 6px 0 0;
}

.hp-actions {
  display: flex;
  gap: 12px;
  margin-top: 30px;
  flex-wrap: wrap;
}

.action {
  padding: 10px 22px;
  border-radius: 8px;
  font-weight: 600;
  text-decoration: none;
  font-size: 15px;
}

.action.primary {
  background: var(--vp-c-brand-1);
  color: #fff;
}

.action.ghost {
  border: 1px solid var(--vp-c-divider);
  color: var(--vp-c-text-1);
}

.hp-cards {
  flex: 1 1 420px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  max-width: 560px;
}

.hp-card {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 24px 22px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 14px;
  text-decoration: none;
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg-soft);
  transition: border-color .2s, box-shadow .2s, transform .2s;
}

.hp-card:hover {
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 8px 20px rgba(0, 0, 0, .1);
  transform: translateY(-3px);
}

.hp-card strong {
  font-size: 21px;
  font-weight: 650;
}

.hp-card em {
  font-style: normal;
  font-size: 14px;
  color: var(--vp-c-text-2);
}

.hp-card .to {
  margin-top: 4px;
  font-size: 14px;
  color: var(--vp-c-brand-1);
}

@media (max-width: 820px) {
  .hp-wrap {
    flex-direction: column;
    align-items: flex-start;
    min-height: auto;
  }

  .hp-brand {
    max-width: none;
  }

  .hp-cards {
    max-width: none;
    width: 100%;
  }
}
</style>
