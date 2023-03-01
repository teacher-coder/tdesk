<template>
  <div>
    <worksheet-option-list :optionList="optionList"></worksheet-option-list>
    <div class="flex flex-row justify-between">
      <worksheet-card
        :worksheet="worksheet"
        v-for="(worksheet, index) in worksheetData"
        :key="index"
      ></worksheet-card>
    </div>
  </div>
</template>

<script>
import WorksheetCard from '@/components/worksheet/WorksheetCard.vue'
import WorksheetOptionList from '@/components/worksheet/WorksheetOptionList.vue'

export default {
  data() {
    return {
      optionList: [{ title: '활동지 만들기', isActive: true, to: 'worksheet' }],

      worksheetData: [
        {
          filename: 'wordsearch_image.png',
          liked: true,
          isReady: true,
          title: '낱말 찾기',
          description: '주어진 낱말에서 학습할 낱말 찾기',
          heartNum: 10,
          route: 'wordsearch',
        },
        {
          filename: 'wordsearch_image.png',
          liked: true,
          isReady: false,
          title: '말판 놀이',
          description: '주사위를 굴러 먼저 도착하기',
          heartNum: 7,
          route: 'board',
        },
        {
          filename: 'wordsearch_image.png',
          liked: true,
          isReady: false,
          title: '도블',
          description: '같은 것 먼저 외치기',
          heartNum: 20,
          route: 'dobble',
        },
      ],
    }
  },

  components: { WorksheetCard, WorksheetOptionList },
}
</script>
