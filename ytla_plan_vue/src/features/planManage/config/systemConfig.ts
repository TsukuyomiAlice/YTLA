import type { SystemConfig } from '@/core/classic/busline/navigator/definitions/systemTypes';

export const planManageSystemConfig: SystemConfig = {
  id: 'planManageSystem',
  name: 'Plan Manage System',
  systemModule: 'planManage',
  rootModule: 'planManager',
  desktopModule: 'planDashboard',
  rootPanel: 'plan_manage'
};
