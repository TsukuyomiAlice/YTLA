import CountdownCard from '../components/CountdownCard.vue'
import type { CountdownCardData } from '../definitions/cardDataType.ts'

export default {
  subType: 'countdown',
  component: CountdownCard,
  getSubTypeProps: (card: any) => {
    const countdownCard = card as CountdownCardData
    return {
      countdownMode: countdownCard.countdown_mode,
      countdownSingleMode: countdownCard.countdown_single_mode,
      countdownSingleLengthValue: countdownCard.countdown_single_length_value,
      countdownSingleLengthUnit: countdownCard.countdown_single_length_unit,
      countdownRepeatPeriodValue: countdownCard.countdown_repeat_period_value,
      countdownRepeatPeriodUnit: countdownCard.countdown_repeat_period_unit,
      startTime: countdownCard.start_time,
      endTime: countdownCard.end_time
    }
  }
}
