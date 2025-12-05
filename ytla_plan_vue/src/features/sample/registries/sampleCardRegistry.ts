import type { Component } from 'vue'
import type { CardRegistry } from '@/core/sideCards/_type/registries/cardRegistry.ts'
import type {
  SampleCardSubType,
  Sample1CardData,
  Sample2CardData,
  Sample3CardData
} from '@/features/sample/types/sampleCardTypes'
import Sample1Card from '@/features/sample/components/cards/sample1/Sample1Card.vue'
import Sample2Card from '@/features/sample/components/cards/sample2/Sample2Card.vue'
import Sample3Card from '@/features/sample/components/cards/sample3/Sample3Card.vue'
import SideCard from '@/core/sideCards/_type/components/SideCard.vue'

/**
 * 计时器卡片注册表（基于通用cardRegistry实现）
 * 注册到全局命名空间 'sample'
 */
export const sampleCardConfig = <CardRegistry> {
  // 1. 组件映射
  components: {
    default: SideCard as Component,
    sample1: Sample1Card as Component,
    sample2: Sample2Card as Component,
    sample3: Sample3Card as Component
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
    switch (card.card_sub_type as SampleCardSubType) {
      case 'sample1':
        const sample1Card = card as Sample1CardData
        return {
          ...baseProps,
          sampleData1: sample1Card.sample_data_1,
          sampleData2: sample1Card.sample_data_2,
          sampleData3: sample1Card.sample_data_3
        }

      case 'sample2':
        const sample2Card = card as Sample2CardData
        return {
          ...baseProps,
          sampleData1: sample2Card.sample_data_1,
          sampleData2: sample2Card.sample_data_2,
          sampleData3: sample2Card.sample_data_3
        }

      case 'sample3':
        const sample3Card = card as Sample3CardData
        return {
          ...baseProps,
          sampleData1: sample3Card.sample_data_1,
          sampleData2: sample3Card.sample_data_2,
          sampleData3: sample3Card.sample_data_3
        }

      default:
        return baseProps
    }
  }
}

// 4. 类型导出（供外部使用）
export type {
  SampleCardSubType,
  Sample1CardData,
  Sample2CardData,
  Sample3CardData
} from '@/features/sample/types/sampleCardTypes'
