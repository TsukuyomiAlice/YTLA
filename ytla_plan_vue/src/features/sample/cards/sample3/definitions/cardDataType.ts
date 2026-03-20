import type { SampleCardData } from '@/features/sample/cards/_type/definitions/cardDataType.ts'
import type { Sample3CardSubType } from './cardType.ts'

export interface Sample3CardData extends SampleCardData {
  card_sub_type: Sample3CardSubType;
  sample_data_1: string;
  sample_data_2: string;
  sample_data_3: string;
}
