<template>
  <worksheet-option-list :optionList="optionList"></worksheet-option-list>

  <wordsearch-template
    lang="kr"
    @table-input-changed="tableInputChanged"
    :download="download"
  >
    <option-selection
      optionName="난이도"
      :optionList="['쉬움', '보통', '어려움']"
      :valueList="['EASY', 'NORMAL', 'DIFFICULT']"
      @button-selected-event="selectLevel"
    ></option-selection>
    <option-selection
      optionName="초성 힌트 제공"
      :optionList="['예', '아니오']"
      :valueList="[true, false]"
      @button-selected-event="selectIsScramble"
    ></option-selection>
  </wordsearch-template>
</template>

<script>
import WordsearchTemplate from '@/components/wordsearch/WordsearchTemplate.vue'
import WorksheetOptionList from '@/components/worksheet/WorksheetOptionList.vue'
import OptionSelection from '@/components/OptionSelection.vue'
import fetchWordsearch from '@/api/functions/wordsearch'

export default {
  data() {
    return {
      optionList: [
        { title: '활동지 만들기', isActive: false, to: 'worksheet' },
        {
          title: '언어 선택',
          isActive: false,
          to: 'wordsearch',
        },
        { title: '정보 입력', isActive: true },
      ],
      level: 'EASY',
      isScramble: true,
      listOfText: [],
    }
  },
  methods: {
    selectLevel(level) {
      this.level = level
    },
    selectIsScramble(isScramble) {
      this.isScramble = isScramble
    },
    tableInputChanged(listOfText) {
      this.listOfText = listOfText
    },
    async download() {
      // TODO 다운로드 받는 기능 - 필요한 data 담기
      console.log('download')
      console.log(this.level)
      console.log(this.isScramble)
      console.log(this.listOfText)
      const res = await fetchWordsearch({})
      console.log(res)
    },
  },
  components: {
    WorksheetOptionList,
    WordsearchTemplate,
    OptionSelection,
  },
}
</script>
