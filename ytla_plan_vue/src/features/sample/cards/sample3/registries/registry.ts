import Sample3Card from '../components/Sample3Card.vue'
import type { Sample3CardData } from '../definitions/cardDataType.ts'

export default {
  subType: 'sample3',
  component: Sample3Card,
  getSubTypeProps: (card: any) => {
    const sample3Card = card as Sample3CardData
    return {
      sampleData1: sample3Card.sample_data_1,
      sampleData2: sample3Card.sample_data_2,
      sampleData3: sample3Card.sample_data_3
    }
  }
}
