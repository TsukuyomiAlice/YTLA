<template>
  <container-side-card :span-columns="spanColumns" :container-style="containerStyle" :is-pinned= "isPinned" :is-expanded="isExpanded" :handle-drag-start="handleDragStart" :handle-drag-end="handleDragEnd">
    <!-- 主显示区 -->
    <div class="main-content">
      <!-- 左上角按钮区 -->
      <div class="column-action-top --left">
        <button-pin :is-pinned="isPinned" :toggle-pin="togglePin" />

        <button-change-icon :show-icon="showIcon" :trigger-icon-upload="triggerIconUpload" />
        <input ref="iconUploadInput" type="file" accept="image/*" hidden @change="handleIconUpload" />

        <button-change-background :trigger-bg-upload="triggerBgUpload" />
        <input ref="bgUploadInput" type="file" accept="image/*" hidden @change="handleBgUpload" />

        <slot name="top-left-actions"></slot>
      </div>

      <!-- 右上角按钮区 -->
      <div class="column-action-top --right">
        <button-edit :show-settings="showSettings" :card-id="cardId" :handle-edit="handleEdit" />

        <button-deactivate :show-deactivate="showDeactivate" :handle-deactivate="handleDeactivate" />

        <button-close :show-close="showClose" :handle-close="handleClose" />

        <slot name="top-actions"></slot>
      </div>

      <!-- 主内容区 -->
      <div class="content-wrapper">
        <div class="header">
          <container-icon :full-icon-path="fullIconPath" :show-icon="showIcon" :handle-icon-error="handleIconError" :remove-icon="removeIcon" />

          <bar-title :show-title="showTitle" :name="name" :title-ref="titleRef" :is-title-editable="isTitleEditable" :start-edit-title="startEditTitle" :handle-title-blur="handleTitleBlur" :cancel-edit-title="cancelEditTitle" />
        </div>

        <!-- tag区域 -->
        <container-tags :show-tags="showTags" :tags-array="tagsArray" :is-adding-tag="isAddingTag" :new-tag="newTag" :tag-input="tagInput" :should-show-add-button="shouldShowAddButton" :show-add-button="showAddButton" :start-adding-tag="startAddingTag" :add-new-tag="addNewTag" :remove-tag="removeTag" :cancel-add-tag="cancelAddTag" :handle-tag-input="handleTagInput" />
        <!-- 主内容 -->
        <slot name="card-content"></slot>
      </div>
    </div>

    <!-- 主按钮区 -->
    <div class="column-action-central">
      <div class="column-action-central-left">
        <slot name="left-actions-buttons"></slot>
      </div>

      <div class="column-action-central-right">
        <slot name="right-actions"></slot>
        <button-expand :toggle-expanded="toggleExpanded" :is-expanded="isExpanded" />
      </div>
    </div>

    <!-- 副内容区 -->
    <transition name="slide-fade">
      <div v-show="isExpanded" class="secondary-content">
        <bar-description :description="description" :description-ref="descriptionRef" :is-description-editable="isDescriptionEditable" :start-edit-description="startEditDescription" :handle-description-blur="handleDescriptionBlur" :cancel-edit-description="cancelEditDescription" />
        <slot name="secondary-content"></slot>
      </div>
    </transition>
  </container-side-card>
</template>

<script setup lang="ts">
import ContainerSideCard from '@/core/classic/cards/sideCard/layouts/ContainerSideCard.vue'

import ButtonPin from '@/core/classic/cards/sideCard/ui/ButtonPin.vue'
import ButtonChangeIcon from '@/core/classic/cards/sideCard/ui/ButtonChangeIcon.vue'
import ButtonChangeBackground from '@/core/classic/cards/sideCard/ui/ButtonChangeBackground.vue'

import ButtonEdit from '@/core/classic/cards/sideCard/ui/ButtonEdit.vue'
import ButtonDeactivate from '@/core/classic/cards/sideCard/ui/ButtonDeactivate.vue'
import ButtonClose from '@/core/classic/cards/sideCard/ui/ButtonClose.vue'

import ButtonExpand from '@/core/classic/cards/sideCard/ui/ButtonExpand.vue'

import ContainerIcon from '@/core/classic/cards/sideCard/ui/ContainerIcon.vue'
import BarTitle from '@/core/classic/cards/sideCard/ui/BarTitle.vue'
import BarDescription from '@/core/classic/cards/sideCard/ui/BarDescription.vue'
import ContainerTags from '@/core/classic/cards/sideCard/ui/ContainerTags.vue'

import type {
  SideCardProps,
  SideCardEmits,
} from '@/core/classic/cards/sideCard/definitions/sideCardType.ts'

const props = withDefaults(defineProps<SideCardProps>(), {
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
})

const emit = defineEmits<SideCardEmits>()

import { useSideCard } from '@/core/classic/cards/sideCard/composables/useSideCard.ts'

const {
    handleDragStart, handleDragEnd,
    isPinned, togglePin,
    fullIconPath, iconUploadInput, triggerIconUpload, handleIconUpload,
    containerStyle, bgUploadInput, triggerBgUpload, handleBgUpload,

    handleEdit,
    handleDeactivate,
    handleClose,
    handleIconError, removeIcon,
    titleRef, isTitleEditable, handleTitleBlur, startEditTitle, cancelEditTitle,
    descriptionRef, isDescriptionEditable, handleDescriptionBlur, startEditDescription, cancelEditDescription,
    isExpanded, toggleExpanded,
    tagsArray, isAddingTag, newTag, tagInput, shouldShowAddButton, showAddButton, startAddingTag, addNewTag, removeTag, handleTagInput, cancelAddTag,

} = useSideCard(props, emit)
</script>

<style lang="scss" scoped>
@use '../styles/side-card';
@use '../styles/side-card-transition';
@use '../styles/column-component';
</style>
