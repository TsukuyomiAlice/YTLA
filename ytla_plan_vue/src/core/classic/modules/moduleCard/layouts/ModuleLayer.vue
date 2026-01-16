<template>
  <div
    class="main-content-layer"
    :class="[
      `mode-${mainContentDisplayMode}`,
      {
        'swapped': isSideBarSwapped,
        'show-sub-frame': showSubFrame,
        'expanded': isRightSideBarExpanded
      }
    ]"
  >
    <!-- 模式6/7的展开按钮 -->
    <button
      v-if="needsExpandButton"
      class="expand-button"
      :class="{ 'swapped-position': isSideBarSwapped }"
      :style="toggleExpandStyle"
      @click="toggleExpand"
    >
      {{ toggleExpandLabel }}
    </button>

    <!-- 主内容区域 -->
    <ModuleMainFrame>
      <keep-alive>
        <component :is="activeModule?.mainComponent"
                   :key="`${activePanel}_${activeModuleId}`" />
      </keep-alive>
    </ModuleMainFrame>

    <!-- 右侧子区域 -->
    <ModuleSubFrame v-if="showSubFrame">
      <keep-alive>
        <component :is="activeModule?.subComponent"
                   :key="`${activePanel}_${activeModuleId}`" />
      </keep-alive>
    </ModuleSubFrame>
  </div>
</template>

<script setup lang="ts">
// frame display
import { computed } from 'vue'

import ModuleMainFrame from '@/core/classic/modules/moduleCard/layouts/ModuleMainFrame.vue'
import ModuleSubFrame from '@/core/classic/modules/moduleCard/layouts/ModuleSubFrame.vue'

import { useLayoutStore } from '@/core/classic/frame/main/services/layoutStore.ts'

const layoutStore = useLayoutStore()
const showSubFrame = computed(() => layoutStore.showSubFrame)
const swapSubFrame = computed(() => layoutStore.swapSubFrame)
const toggleExpand = (): void => {
  layoutStore.toggleExpand()
}

import { storeToRefs } from 'pinia'

const {
  mainContentDisplayMode,
  isSideBarSwapped,
  isRightSideBarExpanded
} = storeToRefs(layoutStore)

const needsExpandButton = computed((): boolean =>
  [4, 5, 6, 7].includes(mainContentDisplayMode.value)
)

const toggleExpandLabel = computed(() => {
  const arrow = isSideBarSwapped.value ?
    (swapSubFrame.value ?
      (isRightSideBarExpanded.value ? '▶' : '◀') :
      (isRightSideBarExpanded.value ? '◀' : '▶')) :
    (swapSubFrame.value ?
      (isRightSideBarExpanded.value ? '◀' : '▶') :
      (isRightSideBarExpanded.value ? '◀' : '▶'))
  return `${arrow}`
})

const toggleExpandStyle = computed(() => {
  const dynamicOffset = isSideBarSwapped.value ?
    (swapSubFrame.value ?
      (isRightSideBarExpanded.value ? '0' : `calc(max(200px, 38.2vw))`) :
      (isRightSideBarExpanded.value ? `calc(100vw - max(80px, 5vw) - 1.3rem)` : `calc(100vw - max(80px, 5vw) - max(200px, 38.2vw) - 1.3rem)`)) :
    (swapSubFrame.value ?
        (isRightSideBarExpanded.value ? '0' : `calc(max(200px, 38.2vw))`) :
        (isRightSideBarExpanded.value ? '0' : `calc(max(200px, 38.2vw))`)
    )
  return {
    [isSideBarSwapped.value ? 'left' : 'right']: dynamicOffset
  }
})

// panel store
import { usePanelStore } from '@/core/classic/frame/panel/stores/panelStore.ts'

const panelStore = usePanelStore()
const { activeModuleSubType } = storeToRefs(panelStore)

import { getModuleConfig } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'

const activeModule = computed(() => {
  return getModuleConfig(activeModuleSubType.value)
})


// 新增获取复合key：${activePanel}_${activeModuleId}
const { activePanel, activeModuleId } = storeToRefs(panelStore)
</script>

<style lang="scss" scoped>
@use '../../../frame/main/styles/main-content-layer';
</style>
