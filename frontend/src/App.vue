<script setup>
import { RouterView } from 'vue-router'
import NavbarHeader from '@/components/navbar/NavbarHeader.vue'
</script>

<template>
  <div class="mx-104 px-2">
    <navbar-header></navbar-header>
    <div class="px-8 py-14">
      <router-view />
    </div>
  </div>
</template>
<style>
/* TODO change underline color on selected */
.router-link-active {
  color: #000000 !important;
}
</style>
