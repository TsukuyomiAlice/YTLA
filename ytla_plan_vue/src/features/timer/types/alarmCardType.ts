import type { BaseTimerCard } from '@/features/timer/types/baseTimerCardType.ts'

export interface AlarmCard extends BaseTimerCard {
  alarm_time: string;
  alarm_days: number[];
  start_time: string;
}
