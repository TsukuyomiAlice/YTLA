import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'
import { feature_viewerModuleFlowManager } from '@/features/feature_maker/modules/feature_viewer/flows/feature_viewerFlowManager'

export const feature_viewerModuleConfig = <ModuleRegistry> {
  moduleType: 'feature_maker',
  moduleSubType: 'feature_viewer',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() => 
    import('@/features/feature_maker/modules/feature_viewer/components/Feature_viewerMain.vue')
  ),
  subComponent: defineAsyncComponent(() => 
    import('@/features/feature_maker/modules/feature_viewer/components/Feature_viewerSub.vue')
  ),
  displayMode: 7,
  flowManager: feature_viewerModuleFlowManager
}
