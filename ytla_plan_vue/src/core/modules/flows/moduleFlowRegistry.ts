import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'
import type { ModuleSubType } from '@/core/modules/types/moduleTypes.ts'

const flowModuleManagers = new Map<ModuleSubType, ModuleFlowManager>()

export function createModuleFlowRegistry (
  moduleSubType: ModuleSubType,
  manager: ModuleFlowManager
) {
  flowModuleManagers.set(moduleSubType, manager)
}

export function getModuleFlowManager(moduleSubType: ModuleSubType): ModuleFlowManager | undefined {
  return flowModuleManagers.get(moduleSubType)
}

export function getDefaultModuleFlowManager(): ModuleFlowManager {
  return <ModuleFlowManager>flowModuleManagers.values().next().value
}
