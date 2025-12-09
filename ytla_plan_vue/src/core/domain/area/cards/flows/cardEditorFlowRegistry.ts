import type { CardEditorFlowManager } from '@/core/domain/area/frame/types/flowManagerTypes.ts'
import type { CardType } from '@/core/domain/area/cards/types/cardType.ts'

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
