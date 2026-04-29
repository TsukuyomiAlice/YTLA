<template>
  <div class="avatar-container">
    <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
      <rect width="48" height="48" rx="8" fill="#E8F5E9" />
      <rect x="8" y="8" width="14" height="14" rx="2" stroke="#2E7D32" stroke-width="2" />
      <rect x="26" y="8" width="14" height="14" rx="2" stroke="#2E7D32" stroke-width="2" />
      <rect x="8" y="26" width="14" height="14" rx="2" stroke="#2E7D32" stroke-width="2" />
      <rect x="26" y="26" width="14" height="14" rx="2" stroke="#2E7D32" stroke-width="2" />
    </svg>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped lang="scss">
.avatar-container {
  width: 100%;
  height: 100%;
  
  svg {
    width: 100%;
    height: 100%;
  }
}
</style>
