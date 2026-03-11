<template>
  <button class="button-clear" @click="handleClear">
    {{ $t('classic.cards.sideCardFilter.clear') }}
  </button>
</template>

<script setup lang="ts">
import type { SideCardFilterClearButtonProps } from '@/core/classic/cards/sideCardFilter/definitions/sideCardFilterType.ts'

defineProps<SideCardFilterClearButtonProps>()
</script>

<style scoped lang="scss">
@use '../styles/side-card-filter';
</style>
