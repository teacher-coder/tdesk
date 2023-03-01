<template>
  <div class="flex flex-row">
    <worksheet-option
      v-for="(option, index) in optionList"
      :key="index"
      :isActive="option.isActive"
      :to="option.to"
    >
      {{ option.title }}
    </worksheet-option>
  </div>
  <br />
</template>

<script>
import WorksheetOption from './WorksheetOption.vue'
export default {
  props: {
    optionList: {
      type: Array,
      required: true,
    },
  },
  components: {
    WorksheetOption,
  },
}
</script>
