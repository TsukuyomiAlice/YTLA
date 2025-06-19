export interface Plan<T = never> {
  plan_id: number;
  name: string;
  tags: string;
  module_groups: string;
  description: string;
  icon_path?: string;
  background_path?: string;
  delete_flag: string;
  active_flag: string;
  _type?: T;
}

export type TagString = string;
export type TagArray = string[];

export function parseTags(tagString: TagString): TagArray {
  return tagString.split(',').map(t => t.trim()).filter(Boolean);
}


export type ModuleGroupString = string;
export type ModuleGroupArray = string[];

export function parseModuleGroups(moduleGroupString: ModuleGroupString): ModuleGroupArray {
  return moduleGroupString.split(',').map(t => t.trim()).filter(Boolean);
}
