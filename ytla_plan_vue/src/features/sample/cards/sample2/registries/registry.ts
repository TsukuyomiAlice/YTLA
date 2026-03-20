import Sample2Card from '../components/Sample2Card.vue'
import type { Sample2CardData } from '../definitions/cardDataType.ts'

export default {
  subType: 'sample2',
  component: Sample2Card,
  getSubTypeProps: (card: any) => {
    const sample2Card = card as Sample2CardData
    return {
      sampleData1: sample2Card.sample_data_1,
      sampleData2: sample2Card.sample_data_2,
      sampleData3: sample2Card.sample_data_3
    }
  }
}
