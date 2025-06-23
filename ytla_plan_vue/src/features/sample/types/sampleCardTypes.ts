import type { BaseCard, CardSubType, CardType } from '@/core/sideCards/types/cardTypes.ts'

export type SampleCardType = 'sample';
export type SampleCardSubType = 'sample1' | 'sample2' | 'sample3' ;

export interface BaseSampleCard extends BaseCard {
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

export interface Sample1CardData extends BaseSampleCard {
  sample_data_1: string;
  sample_data_2: string;
  sample_data_3: string;
}

export interface Sample2CardData extends BaseSampleCard {
  sample_data_1: string;
  sample_data_2: string;
  sample_data_3: string;
}

export interface Sample3CardData extends BaseSampleCard {
  sample_data_1: string;
  sample_data_2: string;
  sample_data_3: string;
}
