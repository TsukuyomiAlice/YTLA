import { createModuleFlowRegistry } from '@/core/domain/area/modules/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'

import { timeModuleFlowManager } from '@/features/basic/modules/time/flows/timeFlowManager.ts'
createModuleFlowRegistry('time', timeModuleFlowManager)
import { timeModuleConfig } from '@/features/basic/modules/time/registries/timeModuleConfig.ts'
createModuleRegistry('time', timeModuleConfig)

import { spaceModuleFlowManager } from '@/features/basic/modules/space/flows/spaceFlowManager.ts'
createModuleFlowRegistry('space', spaceModuleFlowManager)
import { spaceModuleConfig } from '@/features/basic/modules/space/registries/spaceModuleConfig.ts'
createModuleRegistry('space', spaceModuleConfig)

import { definitionModuleFlowManager } from '@/features/basic/modules/definition/flows/definitionFlowManager.ts'
createModuleFlowRegistry('definition', definitionModuleFlowManager)
import { definitionModuleConfig } from '@/features/basic/modules/definition/registries/definitionModuleConfig.ts'
createModuleRegistry('definition', definitionModuleConfig)

import { relationModuleFlowManager } from '@/features/basic/modules/relation/flows/relationFlowManager.ts'
createModuleFlowRegistry('relation', relationModuleFlowManager)
import { relationModuleConfig } from '@/features/basic/modules/relation/registries/relationModuleConfig.ts'
createModuleRegistry('relation', relationModuleConfig)

import { interactionModuleFlowManager } from '@/features/basic/modules/interaction/flows/interactionFlowManager.ts'
createModuleFlowRegistry('interaction', interactionModuleFlowManager)
import { interactionModuleConfig } from '@/features/basic/modules/interaction/registries/interactionModuleConfig.ts'
createModuleRegistry('interaction', interactionModuleConfig)
