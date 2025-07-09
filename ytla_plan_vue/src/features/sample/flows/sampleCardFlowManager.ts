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

export const sampleCardEditorFlowManager = new SampleCardEditorFlowManager()
sampleCardEditorFlowManager.initialStep = markRaw(defineAsyncComponent(() => import('@/features/sample/components/cards/SampleCardSelector.vue')))
sampleCardEditorFlowManager.registerFlow('sample1', [
  markRaw(defineAsyncComponent(() => import('@/features/sample/components/cards/sample1/Sample1Flow.vue')))
])
sampleCardEditorFlowManager.registerFlow('sample2', [
  markRaw(defineAsyncComponent(() => import('@/features/sample/components/cards/sample2/Sample2Flow.vue')))
])
sampleCardEditorFlowManager.registerFlow('sample3', [
  markRaw(defineAsyncComponent(() => import('@/features/sample/components/cards/sample3/Sample3Flow_1.vue'))),
  markRaw(defineAsyncComponent(() => import('@/features/sample/components/cards/sample3/Sample3Flow_2.vue'))),
  markRaw(defineAsyncComponent(() => import('@/features/sample/components/cards/sample3/Sample3Flow_3.vue')))
])
