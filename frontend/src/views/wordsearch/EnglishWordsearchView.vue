<template>
  <worksheet-option-list :optionList="optionList"></worksheet-option-list>

  <wordsearch-template
    lang="en"
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
      optionName="대소문자 선택"
      :optionList="['소문자', '대문자']"
      :valueList="[false, true]"
      @button-selected-event="selectIsUpper"
    ></option-selection>
    <option-selection
      optionName="철자 순서 섞기 (Scramble)"
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
      isUpper: false,
      listOfText: [],
    }
  },
  methods: {
    selectLevel(level) {
      this.level = level
    },
    selectIsUpper(isUpper) {
      this.isUpper = isUpper
    },
    selectIsScramble(isScramble) {
      this.isScramble = isScramble
    },
    tableInputChanged(listOfText) {
      this.listOfText = listOfText
    },
    download() {
      // TODO 다운로드 받는 기능
      console.log('download')
      console.log(this.level)
      console.log(this.isUpper)
      console.log(this.isScramble)
      console.log(this.listOfText)
    },
  },
  components: {
    WorksheetOptionList,
    WordsearchTemplate,
    OptionSelection,
  },
}
</script>
