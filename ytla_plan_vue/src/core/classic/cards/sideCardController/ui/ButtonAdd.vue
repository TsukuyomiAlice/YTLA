<template>
  <button
    class="add-button"
    :class="{ active: isActive }"
    @click="handleClick"
    :title="title"
  >
    <span class="icon">{{ icon }}</span>
  </button>
</template>

<script setup lang="ts">
const props = withDefaults(defineProps<{
  icon: string
  title: string
  isActive?: boolean
}>(), {
  isActive: false
})

const emit = defineEmits<{
  (e: 'click'): void
}>()

const handleClick = () => {
  emit('click')
}
</script>

<style scoped lang="scss">
@use '../styles/side-card-controller';
</style>
