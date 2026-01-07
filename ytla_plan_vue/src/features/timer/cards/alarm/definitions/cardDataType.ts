import type { TimerCardData } from '@/features/timer/cards/_type/definitions/cardDataType.ts'

export interface AlarmCardData extends TimerCardData {
  alarm_time: string;
  alarm_days: number[];
  start_time: string;
}
