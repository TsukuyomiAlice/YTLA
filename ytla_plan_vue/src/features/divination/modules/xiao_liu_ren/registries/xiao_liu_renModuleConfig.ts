import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'
import { xiao_liu_renModuleFlowManager } from '@/features/divination/modules/xiao_liu_ren/flows/xiao_liu_renFlowManager'

export const xiao_liu_renModuleConfig = <ModuleRegistry> {
  moduleType: 'divination',
  moduleSubType: 'xiao_liu_ren',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() => 
    import('@/features/divination/modules/xiao_liu_ren/components/Xiao_liu_renMain.vue')
  ),
  subComponent: defineAsyncComponent(() => 
    import('@/features/divination/modules/xiao_liu_ren/components/Xiao_liu_renSub.vue')
  ),
  displayMode: 7,
  flowManager: xiao_liu_renModuleFlowManager
}
