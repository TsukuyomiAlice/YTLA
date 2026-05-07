export enum SystemLevel {
  SYSTEM_ROOT = 'SYSTEM_ROOT',
  PLAN_DESKTOP = 'PLAN_DESKTOP',
  MODULE = 'MODULE'
}

export interface SystemConfig {
  id: string;
  name: string;
  systemModule: any;
  rootModule: any;
  desktopModule: any;
  rootPanel: any;
}

export interface SystemButtonConfig {
  buttonId: string;
  targetLevel: SystemLevel;
  component: any;
  label?: string;
  order?: number;
  visibleWhen?: (context: SystemContext) => boolean;
}

export interface SystemContext {
  currentPanel: any;
  currentModuleType?: string;
  activePlanId?: string;
}
