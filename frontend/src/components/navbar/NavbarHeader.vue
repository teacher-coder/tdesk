<template>
  <ul class="">
    <nav class="flex justify-between align-middle">
      <router-link to="/" class="my-auto">
        <img src="@/assets/brand-cropped.svg" width="180" />
      </router-link>
      <div class="flex justify-end">
        <navbar-item to="about">소개</navbar-item>
        <navbar-item to="worksheet">활동지 만들기</navbar-item>
        <navbar-item to="suggestion">건의사항</navbar-item>
      </div>
    </nav>
  </ul>
</template>

<script>
import NavbarItem from '@/components/navbar/NavbarItem.vue'
export default { components: { NavbarItem } }
</script>
