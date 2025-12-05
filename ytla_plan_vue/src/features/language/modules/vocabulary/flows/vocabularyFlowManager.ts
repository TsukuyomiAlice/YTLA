import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/_type/types/flowManagerTypes.ts'

export class VocabularyModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const vocabularyModuleFlowManager = new VocabularyModuleFlowManager()

vocabularyModuleFlowManager.registerFlow('vocabulary-main-steps', [
  defineAsyncComponent(() => import('@/features/language/modules/vocabulary/components/VocabularyMain_00.vue')),
  defineAsyncComponent(() => import('@/features/language/modules/vocabulary/components/VocabularyMain_01.vue')),
])

vocabularyModuleFlowManager.registerFlow('vocabulary-sub-steps', [
  defineAsyncComponent(() => import('@/features/language/modules/vocabulary/components/VocabularySub_00.vue')),
])

