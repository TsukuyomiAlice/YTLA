import { createCardEditorFlowRegistry } from '@/core/sideCards/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/sideCards/registries/cardRegistry.ts'
import { createModuleFlowRegistry } from '@/core/modules/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'

// cards


// modules

import { welcomeModuleFlowManager } from '@/features/planManage/flows/welcomeModuleFlowManager.ts'
createModuleFlowRegistry('welcome', welcomeModuleFlowManager)
import { welcomeModuleConfig } from '@/features/planManage/registries/welcomeModuleConfig.ts'
createModuleRegistry('welcome', welcomeModuleConfig)

import { planManageModuleFlowManager } from '@/features/planManage/flows/planManageModuleFlowManager.ts'
createModuleFlowRegistry('planManage', planManageModuleFlowManager)
import { planManageModuleConfig } from '@/features/planManage/registries/planManageModuleConfig.ts'
createModuleRegistry('planManage', planManageModuleConfig)

import { planDashboardModuleFlowManager } from '@/features/planManage/flows/planDashboardModuleFlowManager.ts'
createModuleFlowRegistry('planDashboard', planDashboardModuleFlowManager)
import { planDashboardModuleConfig } from '@/features/planManage/registries/planDashboardModuleConfig.ts'
createModuleRegistry('planDashboard', planDashboardModuleConfig)

import { addModuleModuleFlowManager } from '@/features/planManage/flows/addModuleModuleFlowManager.ts'
createModuleFlowRegistry('addModule', addModuleModuleFlowManager)
import { addModuleModuleConfig } from '@/features/planManage/registries/addModuleModuleConfig.ts'
createModuleRegistry('addModule', addModuleModuleConfig)

import { settingsModuleFlowManager } from '@/features/planManage/flows/settingsFlowManager'
createModuleFlowRegistry('settings', settingsModuleFlowManager)
import { settingsModuleConfig } from '@/features/planManage/registries/settingsModuleConfig.ts'
createModuleRegistry('settings', settingsModuleConfig)
