<template>
  <div class="controller-container">
    <!-- 筛选区域 -->
    <div class="filter-group">
      <input
        v-model="filterValue"
        type="text"
        placeholder="Filter by title or Card type"
        @input="handleFilterInput"
      >
      <button @click="clearFilter">Clear</button>
    </div>

    <!-- 按钮组 -->
    <div class="button-group">
      <h3 class="controller-title">+</h3>
      <button class="add-button" @click="toggleCreation('sample')" title="添加样例卡片">
        <span class="icon">📝</span>
      </button>
      <button class="add-button" @click="toggleCreation('timer')" title="添加计时卡片">
        <span class="icon">⏲️</span>
      </button>
      <button class="add-button" @click="toggleCreation('relax')" title="添加游戏卡片">
        <span class="icon">🎲</span>
      </button>

      <SideCardEditor
        v-if="editorState.visible"
        :card-container="{ cards }"
      />

    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { useCardStore } from '@/core/sideCards/_type/stores/cardStore.ts'
import { useSideCardEditor } from '@/core/sideCards/_type/composables/useSideCardEditor.ts'
import SideCardEditor from '@/core/sideCards/_type/layouts/SideCardEditor.vue'

const cardStore = useCardStore()
const cards = computed(() => cardStore.cards)
const { editorState, showCreation, closeEditor } = useSideCardEditor()
const activeCardType = ref<string | null>(null)

const toggleCreation = (cardType: string) => {
  if (activeCardType.value === cardType && editorState.value.visible) {
    closeEditor()
    activeCardType.value = null
  } else {
    showCreation(cardType as any)
    activeCardType.value = cardType
  }
}

const filterValue = ref('')

const handleFilterInput = () => {
  cardStore.updateFilter(filterValue.value)
}

const clearFilter = () => {
  filterValue.value = ''
  cardStore.updateFilter('')
}

</script>

<style lang="scss" scoped>
@use '../styles/card-controller-container';
</style>
