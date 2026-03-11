<template>
  <ContainerMasonryGrid :is-masonry-supported="isMasonrySupported">
    <transition-group name="fade-scale">
      <component
        :is="getComponent(card)"
        v-for="card in orderedCards"
        :key="card.card_id"
        :card-id="card.card_id"
        :data-card-id="card.card_id"
        :order="cardOrder.indexOf(card.card_id)"
        v-bind="getCardProps(card)"
        @edit="handleEditCard"
        @deactivate="handleDeactivateCard"
        @close="handleCloseCard"
      />
    </transition-group>
  </ContainerMasonryGrid>
</template>

<script setup lang="ts">
import { nextTick, watch } from 'vue'
import { useSideCardPanel } from '@/core/classic/cards/sideCardPanel/composables/useSideCardPanel.ts'
import { useSideCardPanelLayout } from '@/core/classic/cards/sideCardPanel/composables/useSideCardPanelLayout.ts'
import { getCardRegistry } from '@/core/classic/cards/sideCard/factories/cardRegistry.ts'
import ContainerMasonryGrid from '@/core/classic/cards/sideCardPanel/ui/ContainerMasonryGrid.vue'
import type { CardData } from '@/core/classic/cards/sideCard/definitions/cardDataType.ts'

const {
  activeCards,
  handleEditCard,
  handleDeactivateCard,
  handleCloseCard
} = useSideCardPanel()

const {
  isMasonrySupported,
  orderedCards,
  debouncedUpdate,
  visibleCards,
  cardOrder
} = useSideCardPanelLayout()

const getComponent = (card: CardData) => {
  const registry = getCardRegistry(card.card_type)
  return registry?.components[card.card_sub_type]
}

const getCardProps = (card: CardData) => {
  const registry = getCardRegistry(card.card_type)
  return registry ? registry.getCardProps(card) : {}
}

watch(activeCards, () => {
  nextTick(() => {
    debouncedUpdate()
  })
}, { deep: true })

watch(visibleCards, () => {
  nextTick(debouncedUpdate)
}, { deep: true, immediate: true })
</script>

<style lang="scss" scoped>
@use '../styles/card-panel';
</style>
