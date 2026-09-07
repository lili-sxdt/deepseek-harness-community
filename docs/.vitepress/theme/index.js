import DefaultTheme from 'vitepress/theme'
import HomePage from './components/HomePage.vue'
import LessonCards from './components/LessonCards.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('HomePage', HomePage)
    app.component('LessonCards', LessonCards)
  }
}
