<template>
  <input
    :value="value"
    @input="handleInput"
    type="text"
    :placeholder="$t('classic.cards.sideCardFilter.hint')"
  />
</template>

<script setup lang="ts">
import type { SideCardFilterInputProps } from '@/core/classic/cards/sideCardFilter/definitions/sideCardFilterType.ts'

defineProps<SideCardFilterInputProps>()
</script>

<style scoped lang="scss">
@use '../styles/side-card-filter';
</style>
