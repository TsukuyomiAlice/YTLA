import type { Component } from 'vue'
import { defineAsyncComponent, markRaw } from 'vue'
import type { CardEditorFlowManager } from '@/core/frame/types/flowManagerTypes.ts'
import type { SampleCardSubType } from '@/features/sample/types/sampleCardTypes'

export class SampleCardEditorFlowManager implements CardEditorFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null
  registerFlow(cardSubType: SampleCardSubType, steps: Component[]) {
    this.flows.set(cardSubType, steps)
  }
  getSteps(cardSubType: SampleCardSubType): Component[] {
    return this.flows.get(cardSubType) || []
  }
}

declare module '@/features/sample/flows/sampleCardFlowManager.ts' {
  export interface SampleCardEditorFlowManager {
    getSteps(cardSubType: SampleCardSubType): Component[]
  }
}

export const sampleCardEditorFlowManager = new SampleCardEditorFlowManager()
sampleCardEditorFlowManager.initialStep = markRaw(defineAsyncComponent(() => import('@/features/sample/flows/SampleFlowSelector.vue')))
sampleCardEditorFlowManager.registerFlow('sample1', [
  markRaw(defineAsyncComponent(() => import('@/features/sample/flows/SampleFlowForSample1.vue')))
])
sampleCardEditorFlowManager.registerFlow('sample2', [
  markRaw(defineAsyncComponent(() => import('@/features/sample/flows/SampleFlowForSample2.vue')))
])
sampleCardEditorFlowManager.registerFlow('sample3', [
  markRaw(defineAsyncComponent(() => import('@/features/sample/flows/SampleFlowForSample3_1.vue'))),
  markRaw(defineAsyncComponent(() => import('@/features/sample/flows/SampleFlowForSample3_2.vue'))),
  markRaw(defineAsyncComponent(() => import('@/features/sample/flows/SampleFlowForSample3_3.vue')))
])
