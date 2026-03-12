<template>
  <div class="flow-navigator">
    <div class="flow-content-container">
      <slot></slot>
    </div>
    <div class="flow-actions">
      <!-- 取消/返回按钮 -->
      <ButtonAction
        v-if="showCancel"
        type="cancel"
        :disabled="isSubmitting"
        @click="handleCancel"
      >
        {{ isEditing ? $t('classic.cards.sideCardEditor.Cancel') : $t('classic.cards.sideCardEditor.Back') }}
      </ButtonAction>

      <!-- 上一步按钮 -->
      <ButtonAction
        v-if="showPrev"
        type="prev"
        :disabled="isSubmitting"
        @click="handlePrev"
      >
        {{ $t('classic.cards.sideCardEditor.Prev') }}
      </ButtonAction>

      <!-- 下一步按钮 -->
      <ButtonAction
        v-if="showNext"
        type="next"
        :disabled="isSubmitting"
        @click="handleNext"
      >
        {{ $t('classic.cards.sideCardEditor.Next') }}
      </ButtonAction>

      <!-- 提交按钮（动态文字） -->
      <ButtonAction
        v-if="showSubmit"
        type="submit"
        :disabled="isSubmitting || submitDisabled"
        @click="handleSubmit"
      >
        <span v-if="isSubmitting">{{ $t('classic.cards.sideCardEditor.Processing') }}</span>
        <span v-else>{{ isEditing ? $t('classic.cards.sideCardEditor.Save') : $t('classic.cards.sideCardEditor.Add') }}</span>
      </ButtonAction>
    </div>
  </div>
</template>

<script setup lang="ts">
import ButtonAction from '@/core/classic/cards/sideCardEditor/ui/ButtonAction.vue'
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

<style scoped lang="scss">
@use '../styles/side-card-editor-flow-navigator';
</style>
