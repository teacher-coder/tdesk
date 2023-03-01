<template>
  <div>
    <section>
      <div class="pb-6">
        <div class="title is-2">
          반복적으로 만들고 있는 <br />
          활동지나 학습자료가 있나요?
        </div>
        <p class="title is-2 has-text-info my-6">저희가 대신 만들어드릴게요!</p>

        <div class="container px-5">
          <textarea
            class="textarea"
            rows="2"
            placeholder="이런 걸 만들어주면 좋겠어요."
          ></textarea>
          <div>
            <button @click="$router.push('/worksheet')">
              <span> <i class="fas fa-plus"></i> </span><span>남기기</span>
            </button>
          </div>
        </div>
      </div>
      <div class="grid gap-4 grid-cols-3">
        <suggestion-tile
          v-for="(suggestion, index) in suggestions"
          :key="index"
          :idx="index + 1"
          :text="suggestion"
          :color="colors[index % 5]"
        >
        </suggestion-tile>
      </div>
    </section>
  </div>
</template>

<script>
import SuggestionTile from '@/components/SuggestionTile.vue'

export default {
  data() {
    return {
      suggestions: [
        '벌꿀 땅따먹기 활동지를 만들어 주세요!',
        '잘 사용하고 있습니다. 건의사항은 아니고요~ 항상 힘내세요.^^',
        '영어 단어 깜빡이를 만들어 주세요~',
        '기존 낱말 찾기에서 보통 난이도가 너무 어려운 것 같아요. 조금 더 쉽게 부탁드려요~',
        '제시어가 추가된 빙고판을 만들어 주세요.',
        '활동지나 학습자료는 아니지만 자리 구성을 아이들 모르게 원하는대로 앉히는 기능 있을까요?',
      ],
      colors: ['#FFE4E4', '#FFF7E1', '#E7FFE1', '#E1EBFF', '#F7E1FF'],
    }
  },
  components: {
    SuggestionTile,
  },
}
</script>
