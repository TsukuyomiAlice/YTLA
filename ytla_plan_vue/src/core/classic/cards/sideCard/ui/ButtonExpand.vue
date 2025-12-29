<template>
  <button class="toggle-expand-button" @click="toggleExpanded" :aria-expanded="isExpanded">
    <span class="arrow" :class="{ '--up': isExpanded }">▼</span>
  </button>
</template>

<script setup lang="ts">
const { toggleExpanded, isExpanded } = defineProps<{
  toggleExpanded: () => void
  isExpanded: boolean
}>()
</script>

<style scoped lang="scss">
.toggle-expand-button {
  background: none;
  border: none;
  padding: 0.1rem 0.2rem;
  cursor: pointer;
  color: #666;
  transition: color 0.3s ease;

  &:hover {
    color: #42b983;
  }

  .arrow {
    display: inline-block;
    transition: transform 0.3s ease;
    margin-left: 0.1rem;

    &.--up {
      transform: rotate(180deg);
    }
  }
}
</style>
