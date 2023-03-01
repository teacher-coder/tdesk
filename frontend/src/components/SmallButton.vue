<template>
  <div>
    <div
      class="flex flex-row justify-between border-solid border-2 border-black cursor-pointer rounded-6xl py-1 px-4 font-bold"
      :class="{ 'text-primary': selected, 'border-primary': selected }"
    >
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    selected: Boolean,
  },
}
</script>
