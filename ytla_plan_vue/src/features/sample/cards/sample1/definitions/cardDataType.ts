import type { SampleCardData } from '@/features/sample/cards/_type/definitions/cardDataType.ts'
import type { Sample1CardSubType } from './cardType.ts'

export interface Sample1CardData extends SampleCardData {
  card_sub_type: Sample1CardSubType;
  sample_data_1: string;
  sample_data_2: string;
  sample_data_3: string;
}
