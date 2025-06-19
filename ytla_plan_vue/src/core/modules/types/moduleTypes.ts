export type ModuleType = string;

export type ModuleSubType = string;


export interface BaseModule<T = never> {
  module_id: number;
  belong_plan_id: number;
  belong_group_name: string;
  name: string;
  module_type: ModuleType;
  module_sub_type: ModuleSubType;
  tags: string;
  description: string;
  message: string;
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
