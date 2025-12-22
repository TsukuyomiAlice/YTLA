<template>
  <div class="tags-wrapper">
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
        :ref="
          function () {
            return (tagInput)
          }
        "
        :value="newTag"
        @input="handleTagInput"
        class="tag-input"
        type="text"
        placeholder="输入标签"
        @keydown.enter="addNewTag"
        @keydown.esc="cancelAddTag"
        @blur="addNewTag"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  showTags: boolean
  tagsArray: string[]
  isAddingTag: boolean
  newTag: string
  tagInput: HTMLInputElement | null
  shouldShowAddButton: boolean
  showAddButton: boolean
  startAddingTag: () => void
  addNewTag: () => void
  removeTag: (index: number) => void
  cancelAddTag: () => void
}>()

const emit = defineEmits<{
  (e: 'update:newTag', value: string): void
}>()

// 处理标签输入变化
const handleTagInput = (e: Event) => {
  const target = e.target as HTMLInputElement
  emit('update:newTag', target.value)
}
</script>

<style scoped lang="scss">
@use '@/core/classic/cards/sidecard/styles/card-component-tags.scss';
</style>
