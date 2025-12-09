import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/domain/area/frame/types/flowManagerTypes.ts'

export class SphereModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const sphereModuleFlowManager = new SphereModuleFlowManager()

sphereModuleFlowManager.registerFlow('sphere-main-steps', [
  defineAsyncComponent(() => import('@/features/mathematics/modules/sphere/components/SphereMain_00.vue')),
])

sphereModuleFlowManager.registerFlow('sphere-sub-steps', [
  defineAsyncComponent(() => import('@/features/mathematics/modules/sphere/components/SphereSub_00.vue')),
])

