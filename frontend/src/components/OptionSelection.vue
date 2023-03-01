<template>
  <div>
    <div
      class="flex flex-row justify-between border-solid border-2 border-black rounded-4xl p-7"
    >
      <div class="font-bold text-2xl">
        {{ optionName }}
      </div>
      <div class="flex flex-row text-xl gap-2">
        <div v-for="(option, index) in optionList" :key="index">
          <small-button
            @click="selectButton(index)"
            :selected="selectedIdx === index"
          >
            {{ option }}</small-button
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SmallButton from '@/components/SmallButton.vue'

export default {
  data() {
    return {
      selectedIdx: 0,
    }
  },
  props: {
    optionName: String,
    optionList: Array,
    valueList: Array,
  },
  components: {
    SmallButton,
  },
  emits: ['buttonSelectedEvent'],
  methods: {
    selectButton(idx) {
      if (this.selectedIdx !== idx) {
        this.selectedIdx = idx
        this.$emit('buttonSelectedEvent', this.valueList[idx])
      }
    },
  },
}
</script>
