<template>
  <button class="scale-button" @click="handleClick" :title="label">
    <span class="icon">{{ icon }}</span>
    <span v-if="showLabel" class="label">{{ label }}</span>
  </button>
</template>

<script setup lang="ts">
defineProps<{
  icon: string
  label?: string
  showLabel?: boolean
}>()

const emit = defineEmits<{
  (e: 'click'): void
}>()

const handleClick = () => {
  emit('click')
}
</script>

<style lang="scss" scoped>
.scale-button {
  flex: 1 1 calc(var(--max-button-width, 15%) - var(--gap-size, 1rem));
  min-width: var(--min-button-size, 5rem);
  max-width: var(--max-button-width, 15%);
  aspect-ratio: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: white;
  border: 1px solid #eee;
  border-radius: 0.75rem;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  transform: scale(0.95);

  &:hover {
    transform: scale(1);
    border-color: #42b983;
    box-shadow: 0 0.25rem 0.75rem rgba(66, 185, 131, 0.15);
  }

  .icon {
    font-size: calc(var(--min-button-size, 5rem) * 0.5);
    margin-bottom: 0.5rem;
  }

  .label {
    font-size: 0.875rem;
    color: #333;
  }
}

@media (max-width: 1024px) {
  .scale-button {
    flex-basis: calc(25% - var(--gap-size, 1rem));
    max-width: 25%;
  }
}

@media (max-width: 768px) {
  .scale-button {
    flex-basis: calc(33.333% - var(--gap-size, 1rem));
    max-width: 33.333%;
  }
}

@media (max-width: 480px) {
  .scale-button {
    flex-basis: calc(50% - var(--gap-size, 1rem));
    max-width: 50%;
  }
}
</style>
