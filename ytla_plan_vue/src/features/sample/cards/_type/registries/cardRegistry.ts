import type { Component } from 'vue'
import type { CardRegistry } from '@/core/classic/cards/sideCard/registries/cardRegistry.ts'
import Sample1Card from '@/features/sample/cards/sample1/components/Sample1Card.vue'
import Sample2Card from '@/features/sample/cards/sample2/components/Sample2Card.vue'
import Sample3Card from '@/features/sample/cards/sample3/components/Sample3Card.vue'
import SideCard from '@/core/classic/cards/sideCard/components/SideCard.vue'
import type { SampleCardSubType } from '@/features/sample/cards/_type/types/cardType.ts'
import type { SampleCardData } from '@/features/sample/cards/_type/types/cardDataType.ts'
import type { Sample1CardData } from '@/features/sample/cards/sample1/types/cardDataType.ts'
import type { Sample2CardData } from '@/features/sample/cards/sample2/types/cardDataType.ts'
import type { Sample3CardData } from '@/features/sample/cards/sample3/types/cardDataType.ts'

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
  getCardProps: (card: SampleCardData) => {
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
