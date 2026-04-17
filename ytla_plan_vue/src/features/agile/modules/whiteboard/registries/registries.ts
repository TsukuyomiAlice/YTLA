import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { whiteboardModuleFlowManager } from '@/features/agile/modules/whiteboard/flows/whiteboardModuleFlowManager.ts'
createModuleFlowRegistry('whiteboard', whiteboardModuleFlowManager)
import { whiteboardModuleConfig } from '@/features/agile/modules/whiteboard/registries/whiteboardModuleConfig.ts'
createModuleRegistry('whiteboard', whiteboardModuleConfig)
