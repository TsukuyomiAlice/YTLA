<template>
  <div
    class="tags-container"
    v-if="(tagsArray.length > 0 || isAddingTag || shouldShowAddButton) && showTags"
  >
    <span class="tag" v-for="(tag, index) in tagsArray" :key="index">
      {{ tag }}
      <button class="tag-remove" @click.stop="removeTag(index)">×</button>
    </span>

    <button v-if="showAddButton" class="tag-add-button" @click.stop="startAddingTag">+</button>

    <input
      v-if="isAddingTag"
      :ref="
        function () {
          return tagInput
        }
      "
      :value="newTag"
      @input="handleTagInput"
      class="tag-input"
      type="text"
      :placeholder="$t('classic.cards.sideCard.container_tag_new')"
      @keydown.enter="addNewTag"
      @keydown.esc="cancelAddTag"
      @blur="addNewTag"
    />
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
  handleTagInput: (e: Event) => void
  cancelAddTag: () => void
}>()
</script>

<style scoped lang="scss">
@use '../styles/container-tags';
</style>
