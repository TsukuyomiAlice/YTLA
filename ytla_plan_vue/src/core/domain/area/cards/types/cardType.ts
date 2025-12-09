import type { TimerCardType, TimerCardSubType } from '@/features/timer/cards/_type/types/timerCardType.ts';
import type { SampleCardType, SampleCardSubType } from '@/features/sample/cards/_type/types/sampleCardTypes.ts';
import type { RelaxCardType, RelaxCardSubType } from '@/features/relax/cards/_type/types/relaxCardTypes.ts';

export type CardType = TimerCardType | SampleCardType | RelaxCardType | string;

export type CardSubType = TimerCardSubType | SampleCardSubType | RelaxCardSubType | string;
