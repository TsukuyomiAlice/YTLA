import { createCardEditorFlowRegistry } from '@/core/sideCards/_type/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/sideCards/_type/registries/cardRegistry.ts'
import { createModuleFlowRegistry } from '@/core/modules/_type/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'

// cards


// modules

import { ratingModuleFlowManager } from '@/features/language/modules/rating/flows/ratingFlowManager.ts'
createModuleFlowRegistry('rating', ratingModuleFlowManager)
import { ratingModuleConfig } from '@/features/language/modules/rating/registries/ratingModuleConfig.ts'
createModuleRegistry('rating', ratingModuleConfig)

import { dictionaryModuleFlowManager } from '@/features/language/modules/dictionary/flows/dictionaryFlowManager.ts'
createModuleFlowRegistry('dictionary', dictionaryModuleFlowManager)
import { dictionaryModuleConfig } from '@/features/language/modules/dictionary/registries/dictionaryModuleConfig.ts'
createModuleRegistry('dictionary', dictionaryModuleConfig)

import { assessmentModuleFlowManager } from '@/features/language/modules/assessment/flows/assessmentFlowManager.ts'
createModuleFlowRegistry('assessment', assessmentModuleFlowManager)
import { assessmentModuleConfig } from '@/features/language/modules/assessment/registries/assessmentModuleConfig.ts'
createModuleRegistry('assessment', assessmentModuleConfig)

import { vocabularyModuleFlowManager } from '@/features/language/modules/vocabulary/flows/vocabularyFlowManager.ts'
createModuleFlowRegistry('vocabulary', vocabularyModuleFlowManager)
import { vocabularyModuleConfig } from '@/features/language/modules/vocabulary/registries/vocabularyModuleConfig.ts'
createModuleRegistry('vocabulary', vocabularyModuleConfig)

import { readingsModuleFlowManager } from '@/features/language/modules/readings/flows/readingsFlowManager.ts'
createModuleFlowRegistry('readings', readingsModuleFlowManager)
import { readingsModuleConfig } from '@/features/language/modules/readings/registries/readingsModuleConfig.ts'
createModuleRegistry('readings', readingsModuleConfig)

import { learningModuleFlowManager } from '@/features/language/modules/learning/flows/learningFlowManager.ts'
createModuleFlowRegistry('learning', learningModuleFlowManager)
import { learningModuleConfig } from '@/features/language/modules/learning/registries/learningModuleConfig.ts'
createModuleRegistry('learning', learningModuleConfig)
