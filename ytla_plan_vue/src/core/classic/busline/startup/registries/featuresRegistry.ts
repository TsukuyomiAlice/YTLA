import { loadRegistries } from '../utils/dynamicLoader'

// 动态加载所有功能域的注册文件
loadRegistries(['features-modules', 'features-cards'], { eager: true })