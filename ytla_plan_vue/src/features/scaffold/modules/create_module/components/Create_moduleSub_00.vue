<template>
  <div class="sub-section">
    <h3>{{ '关于模块创建' }}</h3>
    <p>{{ '使用此工具快速创建新的功能模块' }}</p>
    
    <div v-if="scaffoldStore.result && scaffoldStore.result.success" class="result-section">
      <h4>{{ '生成结果' }}</h4>
      <div v-if="scaffoldStore.result.results.backend" class="result-item">
        <span class="label">后端路径：</span>
        <span class="path">{{ scaffoldStore.result.results.backend }}</span>
      </div>
      <div v-if="scaffoldStore.result.results.frontend" class="result-item">
        <span class="label">前端路径：</span>
        <span class="path">{{ scaffoldStore.result.results.frontend }}</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useScaffoldModuleStore } from '../stores/scaffoldModuleStore'

const scaffoldStore = useScaffoldModuleStore()
</script>

<style scoped lang="scss">
.sub-section {
  padding: 20px;
}

h3 {
  font-size: 18px;
  color: #333;
  margin-bottom: 12px;
}

p {
  color: #666;
  line-height: 1.6;
  margin-bottom: 20px;
}

.result-section {
  background: #f5f5f5;
  padding: 16px;
  border-radius: 4px;
  margin-top: 20px;
}

h4 {
  font-size: 16px;
  margin-bottom: 12px;
  color: #2e7d32;
}

.result-item {
  display: flex;
  gap: 8px;
  margin-bottom: 8px;
  
  .label {
    font-weight: 500;
    color: #333;
  }
  
  .path {
    font-family: monospace;
    color: #555;
  }
}
</style>
