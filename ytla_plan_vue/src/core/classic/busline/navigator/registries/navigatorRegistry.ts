import { planManageSystemConfig } from '@/features/planManage/config/systemConfig'
import { initSystem, registerSystemButton, getSystemConfig } from './systemNavigatorRegistry'
import { SystemLevel, type SystemContext } from '../definitions/systemTypes'
import ReturnToPlanButton from '@/features/planManage/modules/_type/ui/ReturnToPlanButton.vue'
import ReturnToPlanDashboardButton from '@/features/planManage/modules/_type/ui/ReturnToPlanDashboardButton.vue'

initSystem(planManageSystemConfig)

registerSystemButton({
  buttonId: 'ReturnToSystemRoot',
  targetLevel: SystemLevel.SYSTEM_ROOT,
  component: ReturnToPlanButton,
  order: 1,
  visibleWhen: (context: SystemContext) => {
    const config = getSystemConfig()
    if (!config) return false
    return context.currentPanel !== config.rootPanel
  }
})

registerSystemButton({
  buttonId: 'ReturnToPlanDesktop',
  targetLevel: SystemLevel.PLAN_DESKTOP,
  component: ReturnToPlanDashboardButton,
  order: 2,
  visibleWhen: (context: SystemContext) => {
    const config = getSystemConfig()
    if (!config) return false
    return context.currentPanel !== config.rootPanel && 
           context.currentPanel.startsWith('plan_') && 
           context.currentModuleType !== config.desktopModule
  }
})
