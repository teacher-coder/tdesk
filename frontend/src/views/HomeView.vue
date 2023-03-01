<template>
  <div class="home">
    <section class="">
      <div class="container text-center">
        <div class="text-5xl font-bold">선생님은 쉽게, 아이들은 재밌게!</div>
        <div class="section my-10">
          <div class="text-2xl leading-9">
            <strong class="text-primary">교사의책상</strong>은 학습놀이에 필요한
            활동지를 쉽고 빠르게 만들어 주는 곳입니다.
            <p>그럼 저희와 함께 활동지를 만들러 가볼까요?</p>
          </div>
        </div>
        <div>
          <button
            class="bg-primary text-white rounded-lg py-3 px-6"
            @click="$router.push({ name: 'worksheet' })"
          >
            <icon-plus class="align-middle inline-block mr-3"></icon-plus>
            <span class="align-middle inline-block">활동지 만들기</span>
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import IconPlus from '../components/icons/IconPlus.vue'
export default { components: { IconPlus } }
</script>
