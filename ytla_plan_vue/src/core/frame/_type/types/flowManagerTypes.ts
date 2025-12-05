import type { Component } from 'vue'

declare module '@/core/frame/_type/types/flowManagerTypes.ts' {
  interface CardEditorFlowManager {
    initialStep: Component | null
  }
  interface ModuleFlowManager {
    initialStep: Component | null
  }
}

export interface CardEditorFlowManager {
  initialStep: Component | null
  registerFlow(cardSubType: string, steps: Component[]): void
  getSteps(cardSubType: string): Component[]
}

export interface ModuleFlowManager {
  initialStep: Component | null
  registerFlow(flowName: string, steps: Component[]): void
  getSteps(flowName: string): Component[]
}


export interface FlowStep {
  component: Component
}

export interface FlowManagerFactory {
  createCardEditorManager(): CardEditorFlowManager
  createModuleManager(): ModuleFlowManager
}
