<template>
  <td class="relative hover:cursor-text" @click.prevent="$refs.text.focus()">
    <div class="absolute z-10 text-base font-bold ml-2">{{ idx }}</div>
    <div class="py-7 text-center">
      <input
        type="text"
        class="input"
        ref="text"
        v-model="inputText"
        @input="onDataChanged"
      />
    </div>
  </td>
</template>

<script>
export default {
  data() {
    return {
      inputText: '',
    }
  },
  props: {
    idx: Number,
  },
  methods: {
    onDataChanged() {
      this.$emit('inputTextChanged', this.inputText)
    },
  },
  emits: ['inputTextChanged'],
}
</script>
