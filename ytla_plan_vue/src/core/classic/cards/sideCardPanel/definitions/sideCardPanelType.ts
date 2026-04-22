import type { CardData } from '@/core/classic/cards/sideCard/definitions/cardDataType'

export interface SideCardPanelProps {
}

export interface SideCardPanelEmits {
  (e: 'edit', cardId: number): void
  (e: 'deactivate', cardId: number): void
  (e: 'close', cardId: number): void
}

export interface ContainerMasonryGridProps {
  isMasonrySupported: boolean
}

export interface ContainerMasonryGridEmits {
}

