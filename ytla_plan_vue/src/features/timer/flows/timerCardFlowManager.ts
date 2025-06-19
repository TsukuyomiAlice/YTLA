import type { Component } from 'vue'
import { defineAsyncComponent, markRaw } from 'vue'
import type { CardEditorFlowManager } from '@/core/frame/types/flowManagerTypes.ts'
import type { TimerCardSubType } from '@/features/timer/types/timerCardTypes'

export class TimerCardEditorFlowManager implements CardEditorFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null
  registerFlow(cardSubType: TimerCardSubType, steps: Component[]) {
    this.flows.set(cardSubType, steps)
  }
  getSteps(cardSubType: TimerCardSubType): Component[] {
    return this.flows.get(cardSubType) || []
  }
}

declare module '@/features/timer/flows/timerCardFlowManager.ts' {
  export interface TimerCardEditorFlowManager {
    getSteps(cardSubType: TimerCardSubType): Component[]
  }
}

export const timerCardEditorFlowManager = new TimerCardEditorFlowManager()

timerCardEditorFlowManager.initialStep = markRaw(defineAsyncComponent(() => import('@/features/timer/flows/TimerFlowSelector.vue')))

timerCardEditorFlowManager.registerFlow('alarm', [
  markRaw(defineAsyncComponent(() => import('@/features/timer/flows/TimerFlowForAlarm.vue')))
])

timerCardEditorFlowManager.registerFlow('count', [
  markRaw(defineAsyncComponent(() => import('@/features/timer/flows/TimerFlowForCount.vue')))
])

timerCardEditorFlowManager.registerFlow('countdown', [
  markRaw(defineAsyncComponent(() => import('@/features/timer/flows/TimerFlowForCountdown.vue')))
])
