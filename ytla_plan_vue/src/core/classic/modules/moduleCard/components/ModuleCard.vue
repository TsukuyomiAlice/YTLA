<template>
  <div
    class="module-item"
    :draggable="activeFlag === '1'"
    @dragstart="handleDragStart"
    @dragend="handleDragEnd"
    @dragover.prevent
    @dragenter.prevent
    :style="containerStyle"
    @click="handleModuleClick(moduleId as number)"
  >
    <!-- 左侧图标 -->
    <div class="module-icon">
      <img :src="fullIconPath.iconImage" class="icon" @error="handleIconError" alt="" />
    </div>

    <!-- 主要内容 -->
    <div class="module-content">{{ name }} &nbsp; {{ message }}</div>

    <!-- 右侧设置按钮 -->
    <button class="action-button" @click.stop="startEditing(moduleId as number)">
      <svg class="edit-info" viewBox="0 0 48 48" fill="currentColor">
        <path
          d="M38 6h-8.36C28.8 3.68 26.6 2 24 2c-2.6 0-4.8 1.68-5.64 4H10c-2.2 0-4 1.8-4 4v32c0 2.2 1.8 4 4 4h28c2.2 0 4-1.8 4-4V10c0-2.2-1.8-4-4-4zm-14 0c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zM14 14h20V10h4v32H10V10h4v4z"
        />
      </svg>
    </button>
  </div>
</template>

<script setup lang="ts">
const props = withDefaults(
  defineProps<{
    icon?: string
    background?: string
    name?: string
    tags?: string
    description?: string
    message?: string
    activeFlag?: string

    moduleId?: number
    order?: number
  }>(),
  {
    icon: '',
    background: '',
    name: '默认标题',
    tags: '',
    description: '...',
    message: '...',
    activeFlag: '1',
  },
)
const emit = defineEmits<{
  (e: 'click'): void
  (e: 'edit'): void
  (e: 'module-click', moduleId: number): void
}>()

import { useModuleCard } from '@/core/classic/modules/moduleCard/composables/useModuleCard.ts'

const { handleDragStart, handleDragEnd, handleModuleClick, startEditing } = useModuleCard(
  props,
  emit,
)

import { useModuleCardEditor } from '@/core/classic/modules/moduleCard/composables/useModuleCardEditor.ts'

const { fullIconPath, handleIconError, containerStyle } = useModuleCardEditor(props, emit)
</script>

<style lang="scss" scoped>
@use '../styles/module-card';
@use '../../../cards/sideCard/styles/card-component-button';
@use '../../../cards/sideCard/styles/card-component-icon';
@use '../../../cards/sideCard/styles/card-component-tags';
@use '../../../cards/sideCard/styles/card-component-text';

.icon {
  width: 2rem;
  height: 2rem;
}

.action-button {
  width: 2rem;
  height: 2rem;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 0.25rem;
}
</style>
