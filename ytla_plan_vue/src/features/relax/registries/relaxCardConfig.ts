import type { Component } from 'vue'
import type { CardRegistry } from '@/core/sideCards/_type/registries/cardRegistry.ts'
import type { RelaxCardSubType, WordleCardData } from '@/features/relax/types/relaxCardTypes'
import WordleCard from '@/features/relax/components/cards/wordle/WordleCard.vue'
import SideCard from '@/core/sideCards/_type/components/SideCard.vue'

/**
 * 计时器卡片注册表（基于通用cardRegistry实现）
 * 注册到全局命名空间 'relax'
 */
export const relaxCardConfig = <CardRegistry> {
  // 1. 组件映射
  components: {
    default: SideCard as Component,
    wordle: WordleCard as Component,
  },

  // 2. 属性生成器（保持原有类型安全逻辑）
  getCardProps: (card: any) => {
    const baseProps = {
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

    // 3. 子类型特定属性（类型收窄）
    switch (card.card_sub_type as RelaxCardSubType) {

      case 'wordle':
        return card as WordleCardData

      default:
        return baseProps
    }
  }
}

// 4. 类型导出（供外部使用）
export type {
  RelaxCardSubType,
  WordleCardData,
} from '@/features/relax/types/relaxCardTypes'
