<template>
  <div class="filter-group">
    <FilterInput
      :value="filterValue"
      :handle-input="handleFilterInput"
    />
    <ButtonClear :handle-clear="clearFilter" />
  </div>
</template>

<script setup lang="ts">
import type { SideCardFilterProps } from '@/core/classic/cards/sideCardFilter/definitions/sideCardFilterType.ts'
import FilterInput from '@/core/classic/cards/sideCardFilter/ui/FilterInput.vue'
import ButtonClear from '@/core/classic/cards/sideCardFilter/ui/ButtonClear.vue'

defineProps<SideCardFilterProps>()
</script>

<style scoped lang="scss">
@use '../styles/side-card-filter';
</style>
