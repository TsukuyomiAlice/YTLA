import type { Component } from 'vue'
import { defineAsyncComponent, markRaw } from 'vue'
import type { CardEditorFlowManager } from '@/core/classic/frame/main/types/flowManagerTypes.ts'
import type { RelaxCardSubType } from '@/features/relax/cards/_type/types/cardType.ts'

export class RelaxCardEditorFlowManager implements CardEditorFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null
  registerFlow(cardSubType: RelaxCardSubType, steps: Component[]) {
    this.flows.set(cardSubType, steps)
  }
  getSteps(cardSubType: RelaxCardSubType): Component[] {
    return this.flows.get(cardSubType) || []
  }
}

export const relaxCardEditorFlowManager = new RelaxCardEditorFlowManager()

relaxCardEditorFlowManager.initialStep = markRaw(defineAsyncComponent(() => import('@/features/relax/cards/_type/components/RelaxCardSelector.vue')))

relaxCardEditorFlowManager.registerFlow('wordle', [
  markRaw(defineAsyncComponent(() => import('@/features/relax/cards/wordle/components/WordleFlow.vue')))
])

declare module '@/features/relax/cards/_type/flows/relaxCardFlowManager.ts' {
  export interface RelaxCardEditorFlowManager {
    getSteps(cardSubType: RelaxCardSubType): Component[]
  }
}
