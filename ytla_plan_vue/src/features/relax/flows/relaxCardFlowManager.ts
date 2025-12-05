import type { Component } from 'vue'
import { defineAsyncComponent, markRaw } from 'vue'
import type { CardEditorFlowManager } from '@/core/frame/_type/types/flowManagerTypes.ts'
import type { RelaxCardSubType } from '@/features/relax/types/relaxCardTypes'

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

relaxCardEditorFlowManager.initialStep = markRaw(defineAsyncComponent(() => import('@/features/relax/components/cards/RelaxCardSelector.vue')))

relaxCardEditorFlowManager.registerFlow('wordle', [
  markRaw(defineAsyncComponent(() => import('@/features/relax/components/cards/wordle/WordleFlow.vue')))
])

declare module '@/features/relax/flows/relaxCardFlowManager.ts' {
  export interface RelaxCardEditorFlowManager {
    getSteps(cardSubType: RelaxCardSubType): Component[]
  }
}
