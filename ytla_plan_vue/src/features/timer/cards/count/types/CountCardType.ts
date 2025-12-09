import type { BaseTimerCard } from '@/features/timer/cards/_type/types/baseTimerCardType.ts'

export interface CountCard extends BaseTimerCard {
  count_mode: string;
  count_single_length_value: number;
  count_single_length_unit: string;
  start_time: string;
  end_time: string;
}
