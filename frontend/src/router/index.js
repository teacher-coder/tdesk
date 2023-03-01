import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // TODO 404 error page
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('@/views/AboutView.vue'),
    },
    {
      path: '/worksheet',
      component: () => import('@/views/WorksheetView.vue'),
      children: [
        {
          path: '',
          name: 'worksheet',
          component: () => import('@/views/WorksheetSelectionView.vue'),
        },
        {
          path: 'wordsearch',
          component: () => import('@/views/worksheet/WordsearchView.vue'),
          children: [
            {
              path: '',
              name: 'wordsearch',
              component: () =>
                import('@/components/wordsearch/LangSelection.vue'),
            },
            {
              path: 'kr',
              name: 'wordsearch_kr',
              component: () =>
                import('@/views/wordsearch/KoreanWordsearchView.vue'),
            },
            {
              path: 'en',
              name: 'wordsearch_en',
              component: () =>
                import('@/views/wordsearch/EnglishWordsearchView.vue'),
            },
          ],
        },
        {
          path: 'board',
          name: 'board',
          component: () => import('@/views/worksheet/BoardView.vue'),
        },
        {
          path: 'dobble',
          name: 'dobble',
          component: () => import('@/views/worksheet/DobbleView.vue'),
        },
      ],
    },

    {
      path: '/suggestion',
      name: 'suggestion',
      component: () => import('@/views/SuggestionView.vue'),
    },
  ],
})

export default router
