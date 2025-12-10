import type { CardType, CardSubType } from './cardType.ts'

export interface CardData<T = never> {
  card_id: number;
  name: string;
  tags: string;
  card_type: CardType;
  card_sub_type: CardSubType;
  description: string;
  icon_path?: string;
  background_path?: string;
  delete_flag: string;
  active_flag: string;
  _type?: T;
}

export function parseTags(tagString: string): string[] {
  return tagString.split(',').map(t => t.trim()).filter(Boolean);
}
