<template>
  <div class="flow-navigator">
    <div class="flow-content-container">
      <slot></slot>
    </div>
    <div class="flow-actions">
      <!-- 取消/返回按钮 -->
      <button
        v-if="showCancel"
        class="action-btn cancel"
        @click="handleCancel"
        :disabled="isSubmitting"
      >
        {{ isEditing ? $t('classic.cards.sideCardEditor.Cancel') : $t('classic.cards.sideCardEditor.Back') }}
      </button>

      <!-- 上一步按钮 -->
      <button
        v-if="showPrev"
        class="action-btn prev"
        @click="handlePrev"
        :disabled="isSubmitting"
      >
        {{ $t('classic.cards.sideCardEditor.Prev') }}
      </button>

      <!-- 下一步按钮 -->
      <button
        v-if="showNext"
        class="action-btn next"
        @click="handleNext"
        :disabled="isSubmitting"
      >
        {{ $t('classic.cards.sideCardEditor.Next') }}
      </button>

      <!-- 提交按钮（动态文字） -->
      <button
        v-if="showSubmit"
        class="action-btn submit"
        @click="handleSubmit"
        :disabled="isSubmitting || submitDisabled"
      >
        <span v-if="isSubmitting">{{ $t('classic.cards.sideCardEditor.Processing') }}</span>
        <span v-else>{{ isEditing ? $t('classic.cards.sideCardEditor.Save') : $t('classic.cards.sideCardEditor.Add') }}</span>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import type {
  SideEditorFlowNavigatorProps, SideEditorFlowNavigatorEmits
} from '@/core/classic/cards/sideCardEditor/definitions/sideCardEditorNavigatorType.ts'

const props = withDefaults(defineProps<SideEditorFlowNavigatorProps>(), {
  isEditing: false,
  showCancel: true,
  showPrev: false,
  showNext: false,
  showSubmit: true,
  submitDisabled: false
})

const emit = defineEmits<SideEditorFlowNavigatorEmits>()

import { useSideCardEditorFlowNavigator } from '@/core/classic/cards/sideCardEditor/composables/useSideCardEditorFlowNavigator.ts'
const { isSubmitting, handleCancel, handlePrev, handleNext, handleSubmit } = useSideCardEditorFlowNavigator(props, emit)
</script>

<style lang="scss" scoped>
@use '../styles/side-card-editor-flow-navigator';
</style>
