import { createModuleFlowRegistry } from '@/core/domain/area/modules/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'// modules

import { sampleModuleFlowManager } from '@/features/sample/modules/_type/flows/sampleModuleFlowManager.ts'
createModuleFlowRegistry('sample', sampleModuleFlowManager)
import { sampleModuleConfig } from '@/features/sample/modules/sample/registries/sampleModuleConfig.ts'
createModuleRegistry('sample', sampleModuleConfig)
