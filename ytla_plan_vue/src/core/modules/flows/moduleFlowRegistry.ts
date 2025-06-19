import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'
import type { CardType } from '@/core/cards/types/cardTypes.ts'

const flowModuleManagers = new Map<CardType, ModuleFlowManager>()

export function registerModuleFlowManager(
  moduleType: string,
  manager: ModuleFlowManager
) {
  flowModuleManagers.set(moduleType, manager)
}

export function getModuleFlowManager(moduleType: string): ModuleFlowManager | undefined {
  return flowModuleManagers.get(moduleType)
}

export function getDefaultModuleFlowManager(): ModuleFlowManager {
  return <ModuleFlowManager>flowModuleManagers.values().next().value
}
