import DefaultTheme from 'vitepress/theme'
import LessonCards from './components/LessonCards.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('LessonCards', LessonCards)
  }
}
