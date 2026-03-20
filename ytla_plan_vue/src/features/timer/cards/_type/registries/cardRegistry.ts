import type { sideCardRegistry } from '@/core/classic/cards/sideCard/factories/cardRegistry.ts'
import { buildCardRegistry } from '@/core/classic/cards/sideCard/factories/cardRegistryHelper.ts'
import SideCard from '@/core/classic/cards/sideCard/components/SideCard.vue'

const registryModules = import.meta.glob('@/features/timer/cards/**/registries/registry.ts', { eager: true })

export const timerCardConfig = buildCardRegistry(SideCard, registryModules) as sideCardRegistry
