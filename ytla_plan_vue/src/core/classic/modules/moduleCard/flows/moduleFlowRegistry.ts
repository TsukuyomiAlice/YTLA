import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'
import type { ModuleSubType } from '@/core/classic/modules/moduleCard/definitions/moduleTypes.ts'

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
