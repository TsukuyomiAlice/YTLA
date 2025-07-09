import { createCardEditorFlowRegistry } from '@/core/sideCards/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/sideCards/registries/cardRegistry.ts'
import { createModuleFlowRegistry } from '@/core/modules/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'

// cards


// modules

import { timeModuleFlowManager } from '@/features/basic/flows/timeFlowManager'
createModuleFlowRegistry('time', timeModuleFlowManager)
import { timeModuleConfig } from '@/features/basic/registries/timeModuleConfig.ts'
createModuleRegistry('time', timeModuleConfig)

import { spaceModuleFlowManager } from '@/features/basic/flows/spaceFlowManager'
createModuleFlowRegistry('space', spaceModuleFlowManager)
import { spaceModuleConfig } from '@/features/basic/registries/spaceModuleConfig.ts'
createModuleRegistry('space', spaceModuleConfig)

import { definitionModuleFlowManager } from '@/features/basic/flows/definitionFlowManager'
createModuleFlowRegistry('definition', definitionModuleFlowManager)
import { definitionModuleConfig } from '@/features/basic/registries/definitionModuleConfig.ts'
createModuleRegistry('definition', definitionModuleConfig)

import { relationModuleFlowManager } from '@/features/basic/flows/relationFlowManager'
createModuleFlowRegistry('relation', relationModuleFlowManager)
import { relationModuleConfig } from '@/features/basic/registries/relationModuleConfig.ts'
createModuleRegistry('relation', relationModuleConfig)

import { interactionModuleFlowManager } from '@/features/basic/flows/interactionFlowManager'
createModuleFlowRegistry('interaction', interactionModuleFlowManager)
import { interactionModuleConfig } from '@/features/basic/registries/interactionModuleConfig.ts'
createModuleRegistry('interaction', interactionModuleConfig)
