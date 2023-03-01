<template>
  <div>
    <div class="font-bold text-3xl mb-5">
      01 찾을 낱말 <span class="text-primary">(모두 안채워도 괜찮아요!)</span>
    </div>

    <div class="flex flex-col">
      <!-- TODO fee validate -> 한글이랑 영어만 되도록 하기 -->
      <table>
        <tr>
          <td-input
            v-for="index in 5"
            :key="index"
            @input-text-changed="textInputChanged(index - 1, $event)"
            :idx="index"
          >
          </td-input>
        </tr>
        <tr>
          <td-input
            v-for="index in 5"
            :key="index"
            @input-text-changed="textInputChanged(index + 4, $event)"
            :idx="index + 5"
          >
          </td-input>
        </tr>
        <tr>
          <td-input
            v-for="index in 5"
            :key="index"
            @input-text-changed="textInputChanged(index + 9, $event)"
            :idx="index + 10"
          >
          </td-input>
        </tr>
      </table>
    </div>
    <div class="font-bold text-3xl mt-10">02 문제 옵션</div>
    <br />
    <div class="grid lg:grid-cols-2 md:grid-cols-1 gap-4 justify-between">
      <slot></slot>
    </div>
    <br />
    <br />
    <br />
    <button
      class="bg-primary text-white rounded-lg w-full py-7"
      @click="download"
    >
      <icon-download class="mr-4 align-middle inline-block"></icon-download>
      <span class="font-bold text-5xl align-middle inline-block"
        >활동지(한글 파일) 다운로드</span
      >
    </button>
  </div>
</template>

<script>
import IconDownload from '@/components/icons/IconDownload.vue'
import TdInput from '@/components/TdInput.vue'

export default {
  data() {
    return {
      listOfText: ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    }
  },
  props: {
    lang: { type: String, required: true },
    download: { type: Function, required: true },
  },
  methods: {
    textInputChanged(idx, text) {
      this.listOfText[idx] = text
      this.$emit('tableInputChanged', this.listOfText)
    },
  },
  components: {
    IconDownload,
    TdInput,
  },
  emits: ['tableInputChanged'],
}
</script>
<style scoped>
table,
th,
td {
  border: 1px solid black;
}
</style>
