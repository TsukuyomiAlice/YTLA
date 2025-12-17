import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/types/flowManagerTypes.ts'

export class MeetingsModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const meetingsModuleFlowManager = new MeetingsModuleFlowManager()

meetingsModuleFlowManager.registerFlow('meetings-main-steps', [
  defineAsyncComponent(() => import('@/features/agile/modules/meetings/components/MeetingsMain_00.vue')),
])

meetingsModuleFlowManager.registerFlow('meetings-sub-steps', [
  defineAsyncComponent(() => import('@/features/agile/modules/meetings/components/MeetingsSub_00.vue')),
])

