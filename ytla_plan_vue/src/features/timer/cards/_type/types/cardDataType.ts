import type { CardData } from '@/core/domain/area/cards/types/cardDataType.ts'
import type { TimerCardType, TimerCardSubType  } from '@/features/timer/cards/_type/types/cardType.ts'

export interface TimerCardData extends CardData {
  card_id: number;
  name: string;
  tags: string;
  description: string;
  card_type: TimerCardType;
  card_sub_type: TimerCardSubType;
  icon_path?: string;
  background_path?: string;
  delete_flag: string;
  active_flag: string;
}
