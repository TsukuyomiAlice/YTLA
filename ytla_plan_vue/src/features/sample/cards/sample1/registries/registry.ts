import Sample1Card from '../components/Sample1Card.vue'
import type { Sample1CardData } from '../definitions/cardDataType.ts'

export default {
  subType: 'sample1',
  component: Sample1Card,
  getSubTypeProps: (card: any) => {
    const sample1Card = card as Sample1CardData
    return {
      sampleData1: sample1Card.sample_data_1,
      sampleData2: sample1Card.sample_data_2,
      sampleData3: sample1Card.sample_data_3
    }
  }
}
