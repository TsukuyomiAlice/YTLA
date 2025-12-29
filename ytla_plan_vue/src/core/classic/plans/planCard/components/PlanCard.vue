<template>
  <div
    class="plan-container"
    :draggable="!isPinned"
    @dragstart="handleDragStart"
    @dragend="handleDragEnd"
    @dragover.prevent
    @dragenter.prevent
    @click.stop
    :style="containerStyle"
  >
    <!-- 主显示区 -->
    <div class="main-content">
      <!-- 左上角按钮区 -->
      <div class="action-column-top --left">
        <button
          class="action-button"
          @click.stop="togglePin"
          :aria-label="isPinned ? '取消固定' : '固定位置'"
          :title="isPinned ? '取消固定' : '固定位置'"
          :class="{ '--pinned': isPinned }"
        >
          <svg class="pin-button" viewBox="0 0 24 24" fill="currentColor"
               :class="{ '--pinned': isPinned }">
            <path
              d="M16 12V4h1c.55 0 1-.45 1-1s-.45-1-1-1H7c-.55 0-1 .45-1 1s.45 1 1 1h1v8l-2 2v2h5.2v6h1.6v-6H18v-2l-2-2z" />
          </svg>
        </button>
      </div>

      <!-- 主内容区 -->
      <div class="content-wrapper">
        <div class="header">
          <div class="icon-container">
            <img
              :src="fullIconPath.iconImage"
              class="icon"
              @error="handleIconError"
              alt=""
            >
          </div>
          <div class="title-wrapper">
            <h3>
              <div class="editable-title">{{ name }}</div>
            </h3>
          </div>

          <div class="action-column-right">
            <button
              class="action-button-big"
              @click.stop="startEditing(props.planId as number)"
              title="编辑计划"
            >
              <svg class="edit-info" viewBox="0 0 48 48" fill="currentColor">
                <path
                  d="M38 6h-8.36C28.8 3.68 26.6 2 24 2c-2.6 0-4.8 1.68-5.64 4H10c-2.2 0-4 1.8-4 4v32c0 2.2 1.8 4 4 4h28c2.2 0 4-1.8 4-4V10c0-2.2-1.8-4-4-4zm-14 0c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zM14 14h20V10h4v32H10V10h4v4z" />
              </svg>
            </button>
          </div>
        </div>

        <!-- tag区域 -->
        <div class="tags-container">
          <span class="tag-slim" v-for="(tag, index) in tagsArray" :key="index"> {{ tag }}
          </span>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { TagString } from '@/core/classic/plans/planCard/types/planTypes.ts'
const props = withDefaults(defineProps<{
  icon?: string
  background?: string
  name?: string
  tags?: TagString
  description?: string

  spanColumns?: number
  planId?: number
  order?: number
}>(), {
  icon: '',
  background: '',
  name: '默认标题',
  tags: '',
  description: '...',

  spanColumns: 1
})

const emit = defineEmits<{
  (e: 'edit', id: number): void
}>()

import { usePanelStore } from '@/core/classic/frame/panel/stores/panelStore.ts'
import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'
const startEditing = (planId: number) => {
  const panelStore = usePanelStore()
  panelStore.switchPanel(`plan_${planId}`, 'planDashboard')
  const moduleProcessStore = useModuleProcessStore()
  moduleProcessStore.setModule('planDashboard', planId)
}

import { usePlanCard } from '@/core/classic/plans/planCard/composables/usePlanCard.ts'
const {
  tagsArray,
  isPinned, handleDragStart, handleDragEnd, togglePin
} = usePlanCard(props, emit)

import { usePlanCardEditor } from '@/core/classic/plans/planCard/composables/usePlanCardEditor.ts'
const {
  fullIconPath, handleIconError,
  containerStyle,
} = usePlanCardEditor(props, emit)
</script>

<style lang="scss" scoped>
@use '../styles/plan-card';
@use '../../../cards/sideCard/styles/ui-button';
@use '../../../cards/sideCard/styles/ui-icon';
@use '../../../cards/sideCard/styles/ui-tags';
@use '../../../cards/sideCard/styles/ui-text';
</style>
