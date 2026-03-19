import type { TimerCardData } from '@/features/timer/cards/_type/definitions/cardDataType.ts'
import type { CountCardSubType } from './cardType.ts'

export interface CountCardData extends TimerCardData {
  card_sub_type: CountCardSubType;
  count_mode: string;
  count_single_length_value: number;
  count_single_length_unit: string;
  start_time: string;
  end_time: string;
}
