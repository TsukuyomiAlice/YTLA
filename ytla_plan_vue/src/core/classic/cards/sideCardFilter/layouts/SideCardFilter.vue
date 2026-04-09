<template>
  <div class="filter-group">
    <BarFilterInput
      :value="filterValue"
      :handle-input="handleFilterInput"
      :placeholder="$t('classic.cards.sideCardFilter.hint')"
    />
    <ButtonFilterClear
      :handle-clear="clearFilter"
      :label="$t('classic.cards.sideCardFilter.clear')"
    />
  </div>
</template>

<script setup lang="ts">
import { useSideCardFilter } from '../composables/useSideCardFilter'
import BarFilterInput from '../ui/BarFilterInput.vue'
import ButtonFilterClear from '../ui/ButtonFilterClear.vue'

const { filterValue, handleFilterInput, clearFilter } = useSideCardFilter()
</script>

<style scoped lang="scss">
@use '../styles/side-card-filter';
</style>
