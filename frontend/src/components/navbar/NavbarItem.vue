<template>
  <div class="m-10">
    <router-link :to="{ name: to }" class="text-2xl text-light-grey font-bold">
      <slot></slot
    ></router-link>
  </div>
</template>

<script>
export default {
  props: { to: String },
}
</script>
