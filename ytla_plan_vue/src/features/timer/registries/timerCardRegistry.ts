import { createCardRegistry } from '@/core/cards/registries/cardRegistry.ts'
import type { Component } from 'vue'
import type {
  TimerCardSubType,
  AlarmCardData,
  CountCardData,
  CountdownCardData
} from '@/features/timer/types/timerCardTypes'
import AlarmCard from '@/features/timer/components/cards/AlarmCard.vue'
import CountCard from '@/features/timer/components/cards/CountCard.vue'
import CountdownCard from '@/features/timer/components/cards/CountdownCard.vue'
import SideCard from '@/core/cards/components/SideCard.vue'

/**
 * 计时器卡片注册表（基于通用cardRegistry实现）
 * 注册到全局命名空间 'timer'
 */
export const timerCardRegistry = createCardRegistry('timer', {
  // 1. 组件映射
  components: {
    default: SideCard as Component,
    alarm: AlarmCard as Component,
    count: CountCard as Component,
    countdown: CountdownCard as Component
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
    switch (card.card_sub_type as TimerCardSubType) {
      case 'alarm':
        const alarmCard = card as AlarmCardData
        return {
          ...baseProps,
          alarmTime: alarmCard.alarm_time,
          alarmDays: alarmCard.alarm_days,
          startTime: alarmCard.start_time
        }

      case 'count':
        const countCard = card as CountCardData
        return {
          ...baseProps,
          countMode: countCard.count_mode,
          countSingleLengthValue: countCard.count_single_length_value,
          countSingleLengthUnit: countCard.count_single_length_unit,
          startTime: countCard.start_time,
          endTime: countCard.end_time
        }

      case 'countdown':
        const countdownCard = card as CountdownCardData
        return {
          ...baseProps,
          countdownMode: countdownCard.countdown_mode,
          countdownSingleMode: countdownCard.countdown_single_mode,
          countdownSingleLengthValue: countdownCard.countdown_single_length_value,
          countdownSingleLengthUnit: countdownCard.countdown_single_length_unit,
          countdownRepeatPeriodValue: countdownCard.countdown_repeat_period_value,
          countdownRepeatPeriodUnit: countdownCard.countdown_repeat_period_unit,
          startTime: countdownCard.start_time,
          endTime: countdownCard.end_time
        }

      default:
        return baseProps
    }
  }
})

// 4. 类型导出（供外部使用）
export type {
  TimerCardSubType,
  AlarmCardData,
  CountCardData,
  CountdownCardData
} from '@/features/timer/types/timerCardTypes'
