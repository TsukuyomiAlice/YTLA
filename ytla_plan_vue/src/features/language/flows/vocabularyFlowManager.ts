import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

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
  defineAsyncComponent(() => import('@/features/language/components/modules/vocabulary/VocabularyMain_00.vue')),
  defineAsyncComponent(() => import('@/features/language/components/modules/vocabulary/VocabularyMain_01.vue')),
])

vocabularyModuleFlowManager.registerFlow('vocabulary-sub-steps', [
  defineAsyncComponent(() => import('@/features/language/components/modules/vocabulary/VocabularySub_00.vue')),
])

