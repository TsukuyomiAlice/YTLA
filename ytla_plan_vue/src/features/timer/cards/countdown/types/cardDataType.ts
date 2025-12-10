import type { TimerCardData } from '@/features/timer/cards/_type/types/cardDataType.ts'

export interface CountdownCardData extends TimerCardData {
  countdown_mode: string;
  countdown_single_mode: string;
  countdown_single_length_value: number;
  countdown_single_length_unit: string;
  countdown_repeat_period_value: number;
  countdown_repeat_period_unit: string;
  start_time: string;
  end_time: string;
}
