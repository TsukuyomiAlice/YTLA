<template>
  <div class="controller-container">
    <side-card-filter :filter-value="filterValue" :handle-filter-input="handleFilterInput" :clear-filter="clearFilter" />

    <div class="button-group">
      <h3 class="controller-title">+</h3>
      <button-add
        v-for="cardTypeInfo in cardTypeButtons"
        :key="cardTypeInfo.type"
        :icon="cardTypeInfo.icon"
        :title="cardTypeInfo.title"
        :is-active="activeCardType === cardTypeInfo.type && editorState.visible"
        @click="toggleCreation(cardTypeInfo.type)"
      />
      <side-card-editor v-if="editorState.visible" :card-container="{ cards }" />
    </div>
  </div>
</template>

<script setup lang="ts">
import SideCardFilter from '@/core/classic/cards/sideCardFilter/layouts/SideCardFilter.vue'
import ButtonAdd from '@/core/classic/cards/sideCardController/ui/ButtonAdd.vue'
import SideCardEditor from '@/core/classic/cards/sideCardEditor/layouts/SideCardEditor.vue'

import { useSideCardController } from '@/core/classic/cards/sideCardController/composables/useSideCardController.ts'

const {
  filterValue, handleFilterInput, clearFilter,
  cards, editorState, activeCardType, cardTypeButtons,
  toggleCreation
} = useSideCardController()
</script>

<style scoped lang="scss">
@use '../styles/side-card-controller';
</style>
