import type { CardData } from '@/core/classic/cards/sideCard/definitions/cardDataType.ts'
import type { RelaxCardType, RelaxCardSubType } from '@/features/relax/cards/_type/definitions/cardType.ts'

export interface RelaxCardData extends CardData {
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
