import type { Component } from 'vue'
import type { CardType } from '@/core/sideCards/types/cardTypes.ts'

export interface CardRegistry <T extends string = string> {
  components: Record<T, Component>
  getCardProps: (card: any) => Record<string, any>
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
