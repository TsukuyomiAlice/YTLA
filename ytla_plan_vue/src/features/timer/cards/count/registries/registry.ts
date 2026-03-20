import CountCard from '../components/CountCard.vue'
import type { CountCardData } from '../definitions/cardDataType.ts'

export default {
  subType: 'count',
  component: CountCard,
  getSubTypeProps: (card: any) => {
    const countCard = card as CountCardData
    return {
      countMode: countCard.count_mode,
      countSingleLengthValue: countCard.count_single_length_value,
      countSingleLengthUnit: countCard.count_single_length_unit,
      startTime: countCard.start_time,
      endTime: countCard.end_time
    }
  }
}
