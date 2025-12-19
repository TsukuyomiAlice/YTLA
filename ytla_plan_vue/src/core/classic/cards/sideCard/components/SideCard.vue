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
        <button-pin :is-pinned="isPinned" :toggle-pin="togglePin" />

        <button-change-icon :show-icon="showIcon" :trigger-icon-upload="triggerIconUpload" />
        <input ref="iconUploadInput" type="file" accept="image/*" hidden @change="handleIconUpload"/>

        <button-change-background :trigger-bg-upload="triggerBgUpload" />
        <input ref="bgUploadInput" type="file" accept="image/*" hidden @change="handleBgUpload" />

        <slot name="top-left-actions"></slot>
      </div>

      <!-- 右上角按钮区 -->
      <div class="action-column-top --top-right">
        <button-edit :show-settings="showSettings" :card-id="cardId" @edit="emit('edit', $event)" />

        <button-deactivate :show-deactivate="showDeactivate" :handle-deactivate="handleDeactivate" />

        <button-close :show-close="showClose" :handle-close="handleClose" />
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
              alt=""
            />
            <button
              v-if="fullIconPath && showIcon"
              class="icon-remove-btn"
              @click.stop="removeIcon"
            >
              ×
            </button>
          </div>
          <div class="title-wrapper">
            <h3>
              <div
                v-if="showTitle"
                :ref="
                  function (el) {
                    return (titleRef = el as HTMLElement | null)
                  }
                "
                class="editable-title"
                :contenteditable="isTitleEditable"
                @click="startEditing('title')"
                @blur="handleTitleBlur"
                @keydown.enter="handleTitleBlur($event)"
                @keydown.esc="cancelEdit('title')"
                :data-placeholder="!name ? '...' : ''"
              >
                {{ name }}
              </div>
            </h3>
          </div>
        </div>

        <!-- tag区域 -->
        <div
          class="tags-container"
          v-if="(tagsArray.length > 0 || isAddingTag || shouldShowAddButton) && showTags"
        >
          <span class="tag" v-for="(tag, index) in tagsArray" :key="index">
            {{ tag }}
            <button class="tag-remove" @click.stop="removeTag(index)">×</button>
          </span>

          <button v-if="showAddButton" class="tag-add-button" @click.stop="startAddingTag">
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
          />
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
        <button class="toggle-button" @click="toggleExpanded" :aria-expanded="isExpanded">
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
            >
              {{ description }}
            </div>
          </strong>
        </div>
        <slot name="secondary-content"></slot>
      </div>
    </transition>
  </div>
</template>

<script setup lang="ts">
import type { SideCardProps, SideCardEmits } from '@/core/classic/cards/sideCard/types/sideCardType.ts'
const props = withDefaults(
  defineProps<SideCardProps>(),
  {
    cardId: 0,
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
  },
)

const emit = defineEmits<SideCardEmits>()

import { useSideCard } from '@/core/classic/cards/sideCard/composables/useSideCard.ts'
import ButtonPin from '@/core/classic/cards/sideCard/ui/ButtonPin.vue'
import ButtonChangeIcon from '@/core/classic/cards/sideCard/ui/ButtonChangeIcon.vue'
import ButtonChangeBackground from '@/core/classic/cards/sideCard/ui/ButtonChangeBackground.vue'
import ButtonEdit from '@/core/classic/cards/sideCard/ui/ButtonEdit.vue'
import ButtonDeactivate from '@/core/classic/cards/sideCard/ui/ButtonDeactivate.vue'
import ButtonClose from '@/core/classic/cards/sideCard/ui/ButtonClose.vue'
const {
  isExpanded,
  titleRef,
  isTitleEditable,
  isDescriptionEditable,
  tagsArray,
  isAddingTag,
  newTag,
  tagInput,
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
  bgUploadInput,
  handleBgUpload,
  removeIcon,
  triggerBgUpload,
  handleDragStart,
  handleDragEnd, isPinned, togglePin, fullIconPath, iconUploadInput, triggerIconUpload, handleIconUpload
} = useSideCard(props, emit)
</script>

<style lang="scss" scoped>
@use '../styles/sidecard';
@use '../styles/card-component-button';
@use '../styles/card-component-icon';
@use '../styles/card-component-tags';
@use '../styles/card-component-text';
</style>
