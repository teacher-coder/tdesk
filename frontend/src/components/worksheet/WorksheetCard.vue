<template>
  <div
    class="relative flex border-solid border-4 border-black rounded-2xl h-104"
    :class="{ 'cursor-pointer': isReady }"
    @click.prevent="isReady ? $router.push({ name: route }) : null"
  >
    <div
      v-if="!isReady"
      class="absolute z-10 rounded-xl flex justify-center items-center h-full w-full bg-overlay bg-opacity-80 text-black font-bold text-4xl"
    >
      업데이트 예정
    </div>
    <div class="pt-5 px-4 w-72 flex flex-col justify-start">
      <div class="border-solid border-2 rounded-2xl h-52 mb-4">image</div>
      <div class="text-left font-bold text-4xl mb-3">{{ title }}</div>
      <div class="text-left text-2xl">{{ description }}</div>
      <div class="flex-1"></div>
      <div class="place-self-end mb-4">
        <font-awesome-icon icon="fa-solid fa-heart" class="mr-1 fa-xl" />
        <!-- <font-awesome-icon icon="fa-regular fa-heart" /> -->
        <span> {{ heartNum }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    worksheet: Object,
  },
  data() {
    return {
      title: this.worksheet.title,
      description: this.worksheet.description,
      isReady: this.worksheet.isReady,
      liked: this.worksheet.liked,
      heartNum: this.worksheet.heartNum,
      filename: this.worksheet.filename,
      route: this.worksheet.route,
    }
  },
}
</script>
