import type { Component } from 'vue'
import type { CardType } from '@/core/classic/cards/sideCard/definitions/cardType.ts'
import type { CardData } from '@/core/classic/cards/sideCard/definitions/cardDataType.ts'

export interface sideCardRegistry <T extends string = string> {
  components: Record<T, Component>
  getCardProps: (card: CardData) => Record<string, unknown>
}

const sideCardRegistryStore = new Map<string, sideCardRegistry>()

export const createCardRegistry = <T extends string>(
  namespace: string,
  config: sideCardRegistry<T>
): sideCardRegistry<T> => {
  sideCardRegistryStore.set(namespace, config)
  return config
}

export const getCardRegistry = (namespace: CardType): sideCardRegistry | undefined => {
  return sideCardRegistryStore.get(namespace)
}

export const getAllCardRegistries = (): Map<string, sideCardRegistry> => {
  return sideCardRegistryStore
}

export const clearAllCardRegistries = (): void => {
  sideCardRegistryStore.clear()
}
