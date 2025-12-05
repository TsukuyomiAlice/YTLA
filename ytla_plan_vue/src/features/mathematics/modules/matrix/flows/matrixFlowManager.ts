import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/_type/types/flowManagerTypes.ts'

export class MatrixModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const matrixModuleFlowManager = new MatrixModuleFlowManager()

matrixModuleFlowManager.registerFlow('matrix-main-steps', [
  defineAsyncComponent(() => import('@/features/mathematics/modules/matrix/MatrixMain_00.vue')),
])

matrixModuleFlowManager.registerFlow('matrix-sub-steps', [
  defineAsyncComponent(() => import('@/features/mathematics/modules/matrix/MatrixSub_00.vue')),
])

