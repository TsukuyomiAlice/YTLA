import type { CardData } from '@/core/classic/cards/sideCard/definitions/cardDataType.ts'
import type { SampleCardType, SampleCardSubType } from './cardType.ts'

export interface SampleCardData extends CardData {
  card_id: number;
  name: string;
  tags: string;
  description: string;
  card_type: SampleCardType;
  card_sub_type: SampleCardSubType;
  icon_path?: string;
  background_path?: string;
  delete_flag: string;
  active_flag: string;
}
