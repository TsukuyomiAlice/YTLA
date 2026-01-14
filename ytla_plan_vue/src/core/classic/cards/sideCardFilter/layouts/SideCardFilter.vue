<template>
  <div class="filter-group">
    <input
      :value="filterValue"
      @input="handleFilterInput"
      type="text"
      :placeholder="$t('classic.cards.sideCardFilter.hint')"
    />
    <button class="button-clear" @click="clearFilter">{{ $t('classic.cards.sideCardFilter.clear') }}</button>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  filterValue: string
  handleFilterInput: (e: Event) => void
  clearFilter: () => void
}>()
</script>

<style scoped lang="scss">
@use '../styles/side-card-filter';
</style>
