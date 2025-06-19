import type { Component } from 'vue'
import type { CardType } from '@/core/cards/types/cardTypes.ts'

export interface CardRegistry<T extends string = string> {
  components: Record<T, Component>
  getCardProps: (card: any) => Record<string, any>
}

const registryStore = new Map<string, CardRegistry>()

export const createCardRegistry = <T extends string>(
  namespace: string,
  config: CardRegistry<T>
): CardRegistry<T> => {
  registryStore.set(namespace, config)
  return config
}

export const getCardRegistry = (namespace: CardType): CardRegistry | undefined => {
  return registryStore.get(namespace)
}
