import { loadRegistries, type PatternKey } from '../utils/dynamicLoader'

// 动态加载核心注册文件
loadRegistries(['core', 'plan-manage'], { eager: true })