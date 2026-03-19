import type { TimerCardData } from '@/features/timer/cards/_type/definitions/cardDataType.ts'
import type { AlarmCardSubType } from './cardType.ts'

export interface AlarmCardData extends TimerCardData {
  card_sub_type: AlarmCardSubType;
  alarm_time: string;
  alarm_days: number[];
  start_time: string;
}
