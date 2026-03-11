<template>
  <aside class="sidebar right-sidebar">
    <div class="sidebar-header">
      <SideCardController />
      <SideCardEditor
        ref="cardEditorRef"
        @refresh="handleRefresh"
        :card-container="{ cards }"
      />
    </div>
    <div class="sidebar-body">
      <SideCardPanel />
    </div>
  </aside>
</template>

<script setup lang="ts">
import { useSideCardLayer } from '@/core/classic/cards/sideCardLayer/composables/useSideCardLayer.ts'
import SideCardController from '@/core/classic/cards/sideCardController/layouts/SideCardController.vue'
import SideCardPanel from '@/core/classic/cards/sideCardPanel/layouts/SideCardPanel.vue'
import SideCardEditor from '@/core/classic/cards/sideCardEditor/layouts/SideCardEditor.vue'

const { cards, handleRefresh } = useSideCardLayer()
</script>

<style lang="scss" scoped>
@use '../styles/side-card-layer';
</style>
