// plan card registry
import { createPlanCardRegistry } from '@/core/domain/area/plans/registries/planCardRegistry.ts'
createPlanCardRegistry()
// module card registry
import { createModuleCardRegistry } from '@/core/domain/area/modules/registries/moduleCardRegistry.ts'
createModuleCardRegistry()

// system registry
import '@/features/planManage/modules/_type/registries/registries.ts'
