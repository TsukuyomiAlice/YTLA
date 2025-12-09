<template>
  <aside class="sidebar right-sidebar">
    <div class="sidebar-header">
      <SideCardController />
      <SideCardEditor
        ref="cardEditorRef"
        @refresh="handleRefresh"
        :card-container="{ cards }"
      />
    </div>
    <div class="sidebar-body">
      <SideCardContainer />
    </div>
  </aside>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useCardStore } from '@/core/domain/area/cards/stores/cardStore.ts'
import SideCardController from '@/core/domain/area/cards/layouts/SideCardController.vue'
import SideCardContainer from '@/core/domain/area/cards/layouts/SideCardContainer.vue'
import SideCardEditor from '@/core/domain/area/cards/layouts/SideCardEditor.vue'

const cardStore = useCardStore()
const cards = computed(() => cardStore.cards)

const fetchCards = async () => {
  try {
    await cardStore.fetchCards()
  } catch (error) {
    console.error('获取卡片失败:', error)
  }
}

const handleRefresh = async () => {
  try {
    await fetchCards()
    console.log('卡片列表已刷新')
  } catch (error) {
    console.error('刷新卡片失败:', error)
  }
}
</script>

<style lang="scss" scoped>
@use '../../frame/styles/layout';
@use '../../frame/styles/layout-variables' as layout-variables;

@media (max-width: 768px) {
  .app-container {
    --left-width: #{layout-variables.$layout-mobile-left-width};
    --right-width: #{layout-variables.$layout-mobile-right-width};
  }

  .main-content {
    margin-left: 3.5rem;

    .app-container.swapped & {
      margin-right: 3.5rem;
    }
  }
}
</style>
