import type { BaseCard, CardSubType, CardType } from '@/core/cards/types/cardTypes.ts'

export type RelaxCardType = 'relax';
export type RelaxCardSubType = | 'wordle' | 'beeper' | 'crasher';

export interface BaseRelaxCard extends BaseCard {
  card_id: number;
  name: string;
  tags: string;
  description: string;
  card_type: RelaxCardType;
  card_sub_type: RelaxCardSubType;
  icon_path?: string;
  background_path?: string;
  delete_flag: string;
  active_flag: string;
}

export interface WordleCardData extends BaseRelaxCard {
}
