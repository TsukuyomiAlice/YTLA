import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { feature_viewerModuleFlowManager } from '@/features/feature_maker/modules/feature_viewer/flows/feature_viewerFlowManager.ts'
createModuleFlowRegistry('feature_viewer', feature_viewerModuleFlowManager)
import { feature_viewerModuleConfig } from '@/features/feature_maker/modules/feature_viewer/registries/feature_viewerModuleConfig.ts'
createModuleRegistry('feature_viewer', feature_viewerModuleConfig)

