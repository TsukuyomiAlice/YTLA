<template>
  <div
    class="card-container"
    :draggable="!isPinned"
    @dragstart="handleDragStart"
    @dragend="handleDragEnd"
    @dragover.prevent
    @dragenter.prevent
    :class="{
      '--expanded': isExpanded,
      '--span-2': spanColumns === 2,
      '--span-3': spanColumns === 3,
    }"
    @click.stop
    :style="containerStyle"
  >
    <!-- 主显示区 -->
    <div class="main-content">
      <!-- 左上角按钮区 -->
      <div class="action-column-top --top-left">
        <button
          class="action-button"
          @click.stop="togglePin"
          :aria-label="isPinned ? '取消固定' : '固定位置'"
          :title="isPinned ? '取消固定' : '固定位置'"
          :class="{ '--pinned': isPinned }"
        >
          <svg class="pin-button" viewBox="0 0 24 24" fill="currentColor" :class="{ '--pinned': isPinned }">
            <path
              d="M16 12V4h1c.55 0 1-.45 1-1s-.45-1-1-1H7c-.55 0-1 .45-1 1s.45 1 1 1h1v8l-2 2v2h5.2v6h1.6v-6H18v-2l-2-2z"/>
          </svg>
        </button>
        <button
          v-if="showIcon"
          class="action-button"
          @click.stop="triggerIconUpload"
          aria-label="修改图标"
          title="修改图标">
          <svg viewBox="0 0 24 24" fill="currentColor" class="icon-upload">
            <rect x="3" y="3" width="18" height="18" rx="3" ry="3" stroke="currentColor"
                  stroke-width="2" fill="none"/>
            <circle cx="9" cy="10" r="1.5" fill="currentColor"/>
            <circle cx="15" cy="10" r="1.5" fill="currentColor"/>
            <path d="M8 15a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1" stroke="currentColor" stroke-width="1.5"
                  fill="none" stroke-linecap="round"/>
          </svg>
        </button>
        <input
          ref="iconUploadInput"
          type="file"
          accept="image/*"
          hidden
          @change="handleIconUpload"
        >
        <button
          class="action-button"
          @click.stop="triggerBgUpload"
          aria-label="修改背景"
          title="修改背景">
          <svg viewBox="0 0 24 24" fill="currentColor" class="bg-upload">
            <path
              d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14zm-4-4v-2h-2v2h-2v2h2v2h2v-2h2v-2h-2zM13 7v2h2v2h-2v2H9v-2H7v-2h2V7z"/>
          </svg>
        </button>
        <input
          ref="bgUploadInput"
          type="file"
          accept="image/*"
          hidden
          @change="handleBgUpload"
        >
        <slot name="top-left-actions"></slot>
      </div>

      <!-- 右上角按钮区 -->
      <div class="action-column-top --top-right">
        <button
          v-if="showSettings"
          class="action-button"
          @click="$emit('edit', cardId as number)"
          aria-label="设置"
          title="设置"
        >
          <svg class="gear-icon" viewBox="0 0 24 24" fill="currentColor">
            <path
              d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.3-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.42-.48-.42h-3.84c-.24 0-.44.18-.47.42l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94 0 .31.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.3.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.04.24.24.42.48.42h3.84c.24 0 .44-.18.47-.42l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/>
          </svg>
        </button>
        <button
          v-if="showDeactivate"
          class="action-button"
          @click="handleDeactivate"
          aria-label="停用"
          title="停用"
        >
          <svg class="deactivate-icon" viewBox="0 0 24 24" fill="currentColor">
            <path d="M18 11H6c-.55 0-1 .45-1 1s.45 1 1 1h12c.55 0 1-.45 1-1s-.45-1-1-1z"/>
          </svg>
        </button>
        <button
          v-if="showClose"
          class="action-button"
          @click="handleClose"
          aria-label="关闭卡片"
          title="关闭卡片"
        >
          <svg class="trash-icon" viewBox="0 0 24 24" fill="currentColor">
            <path
              d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"/>
          </svg>
        </button>
        <slot name="top-actions"></slot>
      </div>

      <!-- 主内容区 -->
      <div class="content-wrapper">
        <!-- icon、标题、background -->
        <div class="header">
          <div class="icon-container">
            <img
              v-if="fullIconPath && showIcon"
              :src="fullIconPath.iconImage"
              class="icon"
              @error="handleIconError"
              alt="">
            <button
              v-if="fullIconPath && showIcon"
              class="icon-remove-btn"
              @click.stop="removeIcon"
            >×
            </button>
          </div>
          <div class="title-wrapper">
            <h3>
              <div
                v-if="showTitle"
                :ref="el => titleRef = el as HTMLElement | null"
                class="editable-title"
                :contenteditable="isTitleEditable"
                @click="startEditing('title')"
                @blur="handleTitleBlur"
                @keydown.enter="handleTitleBlur($event)"
                @keydown.esc="cancelEdit('title')"
                :data-placeholder="!name ? '...' : ''"
              >{{ name }}
              </div>
            </h3>
          </div>
        </div>

        <!-- tag区域 -->
        <div class="tags-container"
             v-if="(tagsArray.length > 0 || isAddingTag || shouldShowAddButton) && showTags">
          <span class="tag" v-for="(tag, index) in tagsArray" :key="index">
            {{ tag }}
            <button class="tag-remove" @click.stop="removeTag(index)">×</button>
          </span>

          <button
            v-if="showAddButton"
            class="tag-add-button"
            @click.stop="startAddingTag"
          >
            +
          </button>

          <input
            v-if="isAddingTag"
            ref="tagInput"
            v-model="newTag"
            class="tag-input"
            type="text"
            placeholder="输入标签"
            @keydown.enter="addNewTag"
            @keydown.esc="cancelAddTag"
            @blur="addNewTag"
          >
        </div>

        <!-- 主内容 -->
        <slot name="card-content"></slot>
      </div>
    </div>

    <!-- 主按钮区 -->
    <div class="action-column-central">
      <div class="action-column-central-left">
        <slot name="left-actions-buttons"></slot>
      </div>

      <div class="action-column-central-right">
        <slot name="right-actions"></slot>
        <button
          class="toggle-button"
          @click="toggleExpanded"
          :aria-expanded="isExpanded"
        >
          <span class="arrow" :class="{ '--up': isExpanded }">▼</span>
        </button>
      </div>
    </div>

    <!-- 副内容区 -->
    <transition name="slide-fade">
      <div v-show="isExpanded" class="secondary-content">
        <div class="description-text">
          <strong>
            <div
              class="editable-description"
              :contenteditable="isDescriptionEditable"
              @click="startEditing('description')"
              @blur="handleDescriptionBlur"
              @keydown.enter="handleDescriptionBlur($event)"
              @keydown.esc="cancelEdit('description')"
              :data-placeholder="!description ? '...' : ''"
            >{{ description }}
            </div>
          </strong>
        </div>
        <slot name="secondary-content"></slot>
      </div>
    </transition>
  </div>
</template>

<script setup lang="ts">
const props = withDefaults(defineProps<{
  cardType?: string
  cardId?: number
  icon?: string
  background?: string
  name?: string
  tags?: string
  description?: string

  spanColumns?: number
  initialExpanded?: boolean
  showIcon?: boolean
  showTitle?: boolean
  showTags?: boolean
  showSettings?: boolean
  showDeactivate?: boolean
  showClose?: boolean
  order?: number
}>(), {
  cardType: 'default',
  icon: '',
  background: '',
  name: '默认标题',
  tags: '',
  description: '...',

  spanColumns: 1,
  initialExpanded: false,
  showIcon: true,
  showTitle: true,
  showTags: true,
  showSettings: true,
  showDeactivate: true,
  showClose: true,
})


const emit = defineEmits<{
  (e: 'toggle-expanded', state: boolean): void
  (e: 'settings'): void
  (e: 'deactivate', id?: number): void
  (e: 'close', id?: number): void
  (e: 'left-action', action: string): void
  (e: 'update:tags', tags: string): void
  (e: 'edit', id: number): void
}>()

import { useSideCard } from '@/core/domain/area/cards/composables/useSideCard.ts'
const {
  isExpanded,
  titleRef,
  isTitleEditable,
  isDescriptionEditable,
  tagsArray,
  isAddingTag,
  newTag,
  tagInput,
  fullIconPath,
  containerStyle,
  shouldShowAddButton,
  showAddButton,
  handleIconError,
  handleDeactivate,
  handleClose,
  toggleExpanded,
  startEditing,
  cancelEdit,
  handleTitleBlur,
  handleDescriptionBlur,
  startAddingTag,
  addNewTag,
  removeTag,
  cancelAddTag,
  triggerIconUpload,
  iconUploadInput,
  bgUploadInput,
  handleIconUpload,
  handleBgUpload,
  removeIcon,
  triggerBgUpload,
  isPinned,
  handleDragStart,
  handleDragEnd,
  togglePin
} = useSideCard(props, emit)
</script>

<style lang="scss" scoped>
@use '../styles/sidecard';
@use '../styles/card-component-button';
@use '../styles/card-component-icon';
@use '../styles/card-component-tags';
@use '../styles/card-component-text';
</style>
