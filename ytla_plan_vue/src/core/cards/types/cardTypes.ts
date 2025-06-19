import type { TimerCardType, TimerCardSubType } from '@/features/timer/types/timerCardTypes.ts';
import type { SampleCardType, SampleCardSubType } from '@/features/sample/types/sampleCardTypes.ts';
import type { RelaxCardType, RelaxCardSubType } from '@/features/relax/types/relaxCardTypes.ts';

export type CardType = TimerCardType | SampleCardType | RelaxCardType | string;

export type CardSubType = TimerCardSubType | SampleCardSubType | RelaxCardSubType | string;


export interface BaseCard<T = never> {
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

export type TagString = string;
export type TagArray = string[];

export function parseTags(tagString: TagString): TagArray {
  return tagString.split(',').map(t => t.trim()).filter(Boolean);
}
