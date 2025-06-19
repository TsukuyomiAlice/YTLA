import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class PropertyModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const propertyModuleFlowManager = new PropertyModuleFlowManager()

propertyModuleFlowManager.registerFlow('property-main-steps', [
  defineAsyncComponent(() => import('@/features/agile/components/modules/property/PropertyMain_00.vue')),
])

propertyModuleFlowManager.registerFlow('property-sub-steps', [
  defineAsyncComponent(() => import('@/features/agile/components/modules/property/PropertySub_00.vue')),
])

