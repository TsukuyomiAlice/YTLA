import type { BaseCard, CardSubType, CardType } from '@/core/sideCards/types/cardTypes.ts'

export type TimerCardType = 'timer';
export type TimerCardSubType = 'alarm' | 'count' | 'countdown' ;

export interface BaseTimerCard extends BaseCard {
  card_id: number;
  name: string;
  tags: string;
  description: string;
  card_type: CardType;
  card_sub_type: CardSubType;
  icon_path?: string;
  background_path?: string;
  delete_flag: string;
  active_flag: string;
}

export interface AlarmCardData extends BaseTimerCard {
  alarm_time: string;
  alarm_days: number[];
  start_time: string;
}

export interface CountCardData extends BaseTimerCard {
  count_mode: string;
  count_single_length_value: number;
  count_single_length_unit: string;
  start_time: string;
  end_time: string;
}

export interface CountdownCardData extends BaseTimerCard {
  countdown_mode: string;
  countdown_single_mode: string;
  countdown_single_length_value: number;
  countdown_single_length_unit: string;
  countdown_repeat_period_value: number;
  countdown_repeat_period_unit: string;
  start_time: string;
  end_time: string;
}
