import type { CardEditorFlowManager } from '@/core/classic/frame/main/types/flowManagerTypes.ts'
import type { CardType } from '@/core/classic/cards/sideCard/types/cardType.ts'

const flowCardEditorManagers = new Map<CardType, CardEditorFlowManager>()

export function createCardEditorFlowRegistry(
  cardType: CardType,
  manager: CardEditorFlowManager
) {
  flowCardEditorManagers.set(cardType, manager)
}

export function getCardEditorFlowManager(cardType: CardType): CardEditorFlowManager | undefined {
  return flowCardEditorManagers.get(cardType)
}

export function getDefaultCardEditorFlowManager(): CardEditorFlowManager {
  return <CardEditorFlowManager>flowCardEditorManagers.values().next().value
}
