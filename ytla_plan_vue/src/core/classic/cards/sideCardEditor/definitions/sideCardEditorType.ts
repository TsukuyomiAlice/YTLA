import type { CardData } from '@/core/classic/cards/sideCard/definitions/cardDataType.ts'
import type { CardSubType, CardType } from '@/core/classic/cards/sideCard/definitions/cardType.ts'

export interface SideCardEditorProps {
  cardContainer: {
    cards: CardData[]
  }
}

export interface SideCardEditorFlowSelectorProps {
  cardSubTypes: Array<{
    value: CardSubType
    icon: string
    label: string
  }>
}

export interface SideCardEditorFlowSelectorEmits {
  (e: 'next', subType: CardSubType): void
  (e: 'cancelEdit'): void
}
