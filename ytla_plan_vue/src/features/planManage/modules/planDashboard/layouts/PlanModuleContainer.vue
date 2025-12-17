<template>
  <div class="module-group"
       @dragover.prevent
       @dragenter.prevent
       @drop="handleDrop">
    <div class="group-header" v-if="!isUngrouped">
      <!-- 可编辑的分组名称 -->
      <div
        class="editable-group-name"
        :contenteditable="isEditing"
        @click="editingGroup"
        @blur="handleNameBlur"
        @keydown.enter="handleNameBlur"
        @keydown.esc="cancelEditing"
      >{{ groupName }}
      </div>
      <button
        class="delete-group-btn"
        @click="handleDeleteGroup"
      >×
      </button>
    </div>
    <div class="group-header" v-else>
      <!-- 不可编辑 未分组标题 -->
      <div class="group-name">{{ groupName }}</div>
    </div>
    <div class="modules-list">
      <transition-group name="fade-scale">
        <component
          :is="getComponent(module)"
          v-for="module in modules"
          :key="module.module_id"
          :module-id="module.module_id"
          :data-module-id="module.plan_id"
          v-bind="getModuleProps(module)"
        />
      </transition-group>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { getModuleCardRegistry } from '@/core/classic/modules/moduleCard/registries/moduleCardRegistry.ts'

const getComponent = (module: any) => {
  const registry = getModuleCardRegistry()
  return registry?.components.default
}

const getModuleProps = (module: any) => {
  const registry = getModuleCardRegistry()
  return registry ? registry.getModuleProps(module) : {}
}

const props = defineProps<{
  groupName: string
  modules: any[]
}>()

const { t } = useI18n()
const isUngrouped = computed(() => props.groupName === t('planManage.PlanDashBoardMain_00_001'))

const emit = defineEmits<{
  (e: 'update:groupName', name: string): void
  (e: 'deleteGroup', name: string): void
}>()

import { useModuleGroup } from '@/core/classic/modules/moduleCard/composables/useModuleGroup.ts'

const {
  isEditing, tempName,
  editingGroup, handleNameBlur, cancelEditing, handleDeleteGroup
} = useModuleGroup(props, emit)

import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'

const moduleProcessStore = useModuleProcessStore()
import { useModuleCardStore } from '@/core/classic/modules/moduleCard/stores/moduleCardStore.ts'

const moduleStore = useModuleCardStore()
const handleDrop = async (e: DragEvent) => {
  const moduleId = Number(e.dataTransfer?.getData('moduleId'))
  const toGroup = isUngrouped.value ? '' : props.groupName
  try {
    // 更新模块分组
    await moduleStore.updateModuleBelongGroupName(moduleId, toGroup)

    // 刷新数据
    await moduleStore.fetchModules(moduleProcessStore.belongPlanId!)
  } catch (error) {
    console.error('模块移动失败:', error)
  }
}
</script>

<style scoped>
.module-group {
  border: 1px solid #e0e0e0;
  border-radius: 0.5rem;
  padding: 1rem;
  background: white;
}

.group-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.6rem;
}

.editable-group-name {
  flex: 1;
  padding: 0.2rem;
  border: 1px solid transparent;
  border-radius: 0.25rem;
  min-height: 1.5em;
}

.editable-group-name[contenteditable="true"] {
  border-color: #ddd;
  background: #f8f8f8;
}

.delete-group-btn {
  background: none;
  border: none;
  color: #f44336;
  font-size: 1.2rem;
  cursor: pointer;
  margin-left: 0.5rem;
}

.modules-list {
  display: grid;
  gap: 0.6rem;
}

.fade-scale-enter-active,
.fade-scale-leave-active {
  transition: all 0.3s ease;
}

.fade-scale-enter-from,
.fade-scale-leave-to {
  opacity: 0;
  transform: scale(0.8);
}

</style>
