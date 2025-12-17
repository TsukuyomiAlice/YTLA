import type { Component } from 'vue'
import type { CardType } from '@/core/classic/cards/sideCard/types/cardType.ts'
import type { CardData } from '@/core/classic/cards/sideCard/types/cardDataType.ts'

export interface CardRegistry <T extends string = string> {
  components: Record<T, Component>
  getCardProps: (card: CardData) => Record<string, unknown>
}

const cardRegistryStore = new Map<string, CardRegistry>()

export const createCardRegistry = <T extends string>(
  namespace: string,
  config: CardRegistry<T>
): CardRegistry<T> => {
  cardRegistryStore.set(namespace, config)
  return config
}

export const getCardRegistry = (namespace: CardType): CardRegistry | undefined => {
  return cardRegistryStore.get(namespace)
}
