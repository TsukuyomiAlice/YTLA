<template>
  <div class="controller-container">

    <side-card-filter :filter-value="filterValue" :handle-filter-input="handleFilterInput" :clear-filter="clearFilter" />

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

      <side-card-editor v-if="editorState.visible" :card-container="{ cards }" />

    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import SideCardFilter from '@/core/classic/cards/sideCardFilter/layouts/SideCardFilter.vue'
import { useSideCardController } from '@/core/classic/cards/sideCardController/composables/useSideCardController.ts'
const { filterValue, handleFilterInput, clearFilter } = useSideCardController()

import { useCardStore } from '@/core/classic/cards/sideCard/stores/cardStore.ts'
import { useSideCardEditor } from '@/core/classic/cards/sideCardEditor/composables/useSideCardEditor.ts'
import SideCardEditor from '@/core/classic/cards/sideCardEditor/layouts/SideCardEditor.vue'

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

</script>

<style lang="scss" scoped>
@use '../styles/side-card-controller';
</style>
