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
        {{ isEditing ? '取消' : '返回' }}
      </button>

      <!-- 上一步按钮 -->
      <button
        v-if="showPrev"
        class="action-btn prev"
        @click="handlePrev"
        :disabled="isSubmitting"
      >
        上一步
      </button>

      <!-- 下一步按钮 -->
      <button
        v-if="showNext"
        class="action-btn next"
        @click="handleNext"
        :disabled="isSubmitting"
      >
        下一步
      </button>

      <!-- 提交按钮（动态文字） -->
      <button
        v-if="showSubmit"
        class="action-btn submit"
        @click="handleSubmit"
        :disabled="isSubmitting || submitDisabled"
      >
        <span v-if="isSubmitting">处理中...</span>
        <span v-else>{{ isEditing ? '保存' : '添加' }}</span>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const props = withDefaults(defineProps<{
  isEditing?: boolean
  showCancel?: boolean
  showPrev?: boolean
  showNext?: boolean
  showSubmit?: boolean
  submitDisabled?: boolean
}>(), {
  isEditing: false,
  showCancel: true,
  showPrev: false,
  showNext: false,
  showSubmit: true,
  submitDisabled: false
})

const emit = defineEmits<{
  (e: 'cancelEdit'): void
  (e: 'prev'): void
  (e: 'next'): void
  (e: 'submit'): void
}>()

const isSubmitting = ref(false)


const handleCancel = () => {
  if (!isSubmitting.value) emit('cancelEdit')
}

const handlePrev = () => {
  if (!isSubmitting.value) emit('prev')
}

const handleNext = () => {
  if (!isSubmitting.value) emit('next')
}

const handleSubmit = async () => {
  if (isSubmitting.value || props.submitDisabled) return

  isSubmitting.value = true
  try {
    emit('submit')
  } finally {
    isSubmitting.value = false
  }
}
</script>

<style lang="scss" scoped>
@use '@/core/sideCards/styles/card-editor-flow-navigator';
</style>
