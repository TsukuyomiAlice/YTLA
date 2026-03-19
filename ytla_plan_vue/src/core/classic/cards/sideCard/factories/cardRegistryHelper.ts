import type { Component } from 'vue'
import type { CardData } from '@/core/classic/cards/sideCard/definitions/cardDataType.ts'

export interface SubTypeRegistry {
  subType: string
  component: Component
  getSubTypeProps: (card: CardData) => Record<string, unknown>
}

export function extractBaseCardProps(card: CardData): Record<string, unknown> {
  return {
    cardId: card.card_id,
    name: card.name,
    cardType: card.card_sub_type,
    tags: card.tags,
    description: card.description,
    iconPath: card.icon_path,
    background: card.background_path,
    showClose: card.delete_flag === '0',
    isActive: card.active_flag === '1'
  }
}

export function buildCardRegistry(
  defaultComponent: Component,
  registryModules: Record<string, unknown>
): {
  components: Record<string, Component>
  getCardProps: (card: CardData) => Record<string, unknown>
} {
  const components: Record<string, Component> = { default: defaultComponent }
  const subTypePropsGetters: Record<string, (card: CardData) => Record<string, unknown>> = {}

  Object.values(registryModules).forEach((module: any) => {
    if (module.default) {
      const registry = module.default as SubTypeRegistry
      const subType = registry.subType
      if (subType && registry.component && registry.getSubTypeProps) {
        components[subType] = registry.component
        subTypePropsGetters[subType] = registry.getSubTypeProps
      }
    }
  })

  const getCardProps = (card: CardData): Record<string, unknown> => {
    const baseProps = extractBaseCardProps(card)
    const subType = card.card_sub_type
    const getSubTypeProps = subTypePropsGetters[subType]

    if (getSubTypeProps) {
      return {
        ...baseProps,
        ...getSubTypeProps(card)
      }
    }

    return baseProps
  }

  return {
    components,
    getCardProps
  }
}
