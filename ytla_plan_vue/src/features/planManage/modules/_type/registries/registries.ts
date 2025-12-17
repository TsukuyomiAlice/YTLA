import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'

import { welcomeModuleFlowManager } from '@/features/planManage/modules/welcome/flows/welcomeModuleFlowManager.ts'
createModuleFlowRegistry('welcome', welcomeModuleFlowManager)
import { welcomeModuleConfig } from '@/features/planManage/modules/welcome/registries/welcomeModuleConfig.ts'
createModuleRegistry('welcome', welcomeModuleConfig)

import { planManageModuleFlowManager } from '@/features/planManage/modules/planManager/flows/planManageModuleFlowManager.ts'
createModuleFlowRegistry('planManage', planManageModuleFlowManager)
import { planManageModuleConfig } from '@/features/planManage/modules/planManager/registries/planManageModuleConfig.ts'
createModuleRegistry('planManage', planManageModuleConfig)

import { planDashboardModuleFlowManager } from '@/features/planManage/modules/planDashboard/flows/planDashboardModuleFlowManager.ts'
createModuleFlowRegistry('planDashboard', planDashboardModuleFlowManager)
import { planDashboardModuleConfig } from '@/features/planManage/modules/planDashboard/registries/planDashboardModuleConfig.ts'
createModuleRegistry('planDashboard', planDashboardModuleConfig)

import { addModuleModuleFlowManager } from '@/features/planManage/modules/addModule/flows/addModuleModuleFlowManager.ts'
createModuleFlowRegistry('addModule', addModuleModuleFlowManager)
import { addModuleModuleConfig } from '@/features/planManage/modules/addModule/registries/addModuleModuleConfig.ts'
createModuleRegistry('addModule', addModuleModuleConfig)

import { settingsModuleFlowManager } from '@/features/planManage/modules/settings/flows/settingsFlowManager.ts'
createModuleFlowRegistry('settings', settingsModuleFlowManager)
import { settingsModuleConfig } from '@/features/planManage/modules/settings/registries/settingsModuleConfig.ts'
createModuleRegistry('settings', settingsModuleConfig)
