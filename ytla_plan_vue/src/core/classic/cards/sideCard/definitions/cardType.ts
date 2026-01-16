import type { TimerCardType, TimerCardSubType } from '@/features/timer/cards/_type/definitions/cardType.ts';
import type { SampleCardType, SampleCardSubType } from '@/features/sample/cards/_type/definitions/cardType.ts';
import type { RelaxCardType, RelaxCardSubType } from '@/features/relax/cards/_type/definitions/cardType.ts';

export type CardType = TimerCardType | SampleCardType | RelaxCardType | string;

export type CardSubType = TimerCardSubType | SampleCardSubType | RelaxCardSubType | string;
