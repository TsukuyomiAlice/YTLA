import type { TimerCardType, TimerCardSubType } from '@/features/timer/types/timerCardType.ts';
import type { SampleCardType, SampleCardSubType } from '@/features/sample/types/sampleCardTypes.ts';
import type { RelaxCardType, RelaxCardSubType } from '@/features/relax/types/relaxCardTypes.ts';

export type CardType = TimerCardType | SampleCardType | RelaxCardType | string;

export type CardSubType = TimerCardSubType | SampleCardSubType | RelaxCardSubType | string;
