import type { RelaxCardData } from '@/features/relax/cards/_type/definitions/cardDataType.ts'
import type { WordleCardSubType } from './cardType.ts'

export interface WordleCardData extends RelaxCardData {
  card_sub_type: WordleCardSubType;
}
