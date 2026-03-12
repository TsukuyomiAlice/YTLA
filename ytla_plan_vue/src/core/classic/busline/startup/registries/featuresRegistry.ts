import { loadCardRegistries } from '@/core/classic/cards/sideCard/factories/cardRegistryLoader'
import { loadModuleRegistries } from '@/core/classic/modules/moduleCard/factories/moduleRegistryLoader'

// 动态加载所有功能域的注册文件
loadCardRegistries()
loadModuleRegistries()