import { createCardEditorFlowRegistry } from '@/core/sideCards/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/sideCards/registries/cardRegistry.ts'
import { createModuleFlowRegistry } from '@/core/modules/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'

// cards


// modules

import { ratingModuleFlowManager } from '@/features/language/flows/ratingFlowManager'
createModuleFlowRegistry('rating', ratingModuleFlowManager)
import { ratingModuleConfig } from '@/features/language/registries/ratingModuleConfig.ts'
createModuleRegistry('rating', ratingModuleConfig)

import { dictionaryModuleFlowManager } from '@/features/language/flows/dictionaryFlowManager'
createModuleFlowRegistry('dictionary', dictionaryModuleFlowManager)
import { dictionaryModuleConfig } from '@/features/language/registries/dictionaryModuleConfig.ts'
createModuleRegistry('dictionary', dictionaryModuleConfig)

import { assessmentModuleFlowManager } from '@/features/language/flows/assessmentFlowManager'
createModuleFlowRegistry('assessment', assessmentModuleFlowManager)
import { assessmentModuleConfig } from '@/features/language/registries/assessmentModuleConfig.ts'
createModuleRegistry('assessment', assessmentModuleConfig)

import { vocabularyModuleFlowManager } from '@/features/language/flows/vocabularyFlowManager'
createModuleFlowRegistry('vocabulary', vocabularyModuleFlowManager)
import { vocabularyModuleConfig } from '@/features/language/registries/vocabularyModuleConfig.ts'
createModuleRegistry('vocabulary', vocabularyModuleConfig)

import { readingsModuleFlowManager } from '@/features/language/flows/readingsFlowManager'
createModuleFlowRegistry('readings', readingsModuleFlowManager)
import { readingsModuleConfig } from '@/features/language/registries/readingsModuleConfig.ts'
createModuleRegistry('readings', readingsModuleConfig)

import { learningModuleFlowManager } from '@/features/language/flows/learningFlowManager'
createModuleFlowRegistry('learning', learningModuleFlowManager)
import { learningModuleConfig } from '@/features/language/registries/learningModuleConfig.ts'
createModuleRegistry('learning', learningModuleConfig)
