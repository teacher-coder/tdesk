<template>
  <worksheet-option-list :optionList="optionList"></worksheet-option-list>
  <div class="flex flex-row justify-between">
    <div
      class="flex bg-primary h-44 w-104 rounded-2xl cursor-pointer"
      @click="$router.push({ name: 'wordsearch_kr' })"
    >
      <div class="m-auto text-white font-bold text-5xl">한국어</div>
    </div>
    <div
      class="flex bg-primary h-44 w-104 rounded-2xl cursor-pointer"
      @click="$router.push({ name: 'wordsearch_en' })"
    >
      <div class="m-auto text-white font-bold text-5xl">English</div>
    </div>
  </div>
</template>

<script>
import WorksheetOptionList from '@/components/worksheet/WorksheetOptionList.vue'

export default {
  data() {
    return {
      optionList: [
        { title: '활동지 만들기', isActive: false, to: 'worksheet' },
        {
          title: '언어 선택',
          isActive: true,
          to: 'wordsearch',
        },
      ],
    }
  },
  components: { WorksheetOptionList },
}
</script>
