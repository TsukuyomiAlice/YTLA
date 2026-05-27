import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class Feature_viewerModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const feature_viewerModuleFlowManager = new Feature_viewerModuleFlowManager()

feature_viewerModuleFlowManager.registerFlow('feature_viewer-main-steps', [
  defineAsyncComponent(() => import('@/features/feature_maker/modules/feature_viewer/components/Feature_viewerMain_00.vue')),
])

feature_viewerModuleFlowManager.registerFlow('feature_viewer-sub-steps', [
  defineAsyncComponent(() => import('@/features/feature_maker/modules/feature_viewer/components/Feature_viewerSub_00.vue')),
])
