<template>
  <div>
    <!-- TODO change outline color on hover -->
    <div
      class="border-solid border-4 rounded-5xl text-center py-4 w-48 mr-5 font-bold text-2xl"
      :class="[
        isActive ? 'border-secondary' : 'border-gray-600',
        isActive ? 'text-secondary' : 'text-gray-600',
        { 'hover:cursor-pointer': !isActive },
      ]"
      @click.prevent="isActive ? null : $router.push({ name: to })"
    >
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WorksheetOption',
  props: { isActive: Boolean, to: String },
}
</script>
