<template>
  <div>
    <div class="w-80 h-32" :style="{ 'background-color': color }">
      <p class="text-2xl font-bold">{{ idx }}번째 건의사항</p>
      {{ text }}
    </div>
  </div>
</template>
<script>
export default {
  props: {
    idx: Number,
    text: String,
    color: String,
  },
}
</script>
