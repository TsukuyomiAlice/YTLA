<template>
  <div class="scaffold-container">
    <h2>{{ '创建模块脚手架' }}</h2>
    
    <div class="form-section">
      <div class="radio-group">
        <label>
          <input type="radio" v-model="scaffoldStore.isCore" :value="false" />
          Feature模块
        </label>
        <label>
          <input type="radio" v-model="scaffoldStore.isCore" :value="true" />
          Core模块
        </label>
      </div>

      <div class="form-group">
        <label>版本</label>
        <select v-model="scaffoldStore.version">
          <option value="classic">Classic</option>
        </select>
      </div>

      <div class="form-group">
        <label>类型名称 <span style="color: red;">*</span></label>
        <input
          type="text"
          v-model="scaffoldStore.typeName"
          placeholder="输入类型名称"
        />
        <div v-if="validationError" class="error-msg">{{validationError}}</div>
      </div>

      <div class="form-group">
        <label>子类型名称</label>
        <input
          type="text"
          v-model="scaffoldStore.subTypeName"
          placeholder="输入子类型名称"
        />
      </div>

      <div class="checkbox-group">
        <label>
          <input type="checkbox" v-model="scaffoldStore.genBackend" />
          生成后端
        </label>
        <label>
          <input type="checkbox" v-model="scaffoldStore.genFrontend" />
          生成前端
        </label>
      </div>

      <div class="button-group">
        <button @click="handleSubmit" :disabled="scaffoldStore.isLoading" class="btn-generate">
          {{scaffoldStore.isLoading ? '正在生成...' : '生成' }}
        </button>
        <button @click="handleReset" class="btn-reset">重置</button>
      </div>

      <div v-if="scaffoldStore.error" class="error-message">
        生成失败：{{ scaffoldStore.error }}
      </div>

      <div v-if="scaffoldStore.result && scaffoldStore.result.success" class="success-message">
        生成成功！
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useScaffoldModuleStore } from '../stores/scaffoldModuleStore'
import { computed } from 'vue'

const scaffoldStore = useScaffoldModuleStore()

const validationError = computed(() => {
  if (!scaffoldStore.typeName.trim()) {
    return '请输入类型名称'
  }
  return ''
})

const handleSubmit = async () => {
  if (!validationError.value) {
    await scaffoldStore.submitForm()
  }
}

const handleReset = () => {
  scaffoldStore.resetForm()
}

</script>

<style scoped lang="scss">
.scaffold-container {
  max-width: 600px;
  padding: 24px;
}

h2 {
  font-size: 20px;
  margin-bottom: 20px;
  color: #333;
}

.form-section {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.radio-group {
  display: flex;
  gap: 20px;
  
  label {
    display: flex;
    align-items: center;
    gap: 6px;
    cursor: pointer;
  }
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
  
  label {
    font-weight: 500;
  }
  
  input, select {
    padding: 8px 12px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 14px;
  }
}

.checkbox-group {
  display: flex;
  gap: 20px;
  
  label {
    display: flex;
    align-items: center;
    gap: 6px;
    cursor: pointer;
  }
}

.button-group {
  display: flex;
  gap: 12px;
  margin-top: 12px;
}

.btn-generate {
  padding: 10px 24px;
  background: #2e7d32;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  
  &:disabled {
    background: #aaa;
    cursor: not-allowed;
  }
  
  &:hover:not(:disabled) {
    background: #225e26;
  }
}

.btn-reset {
  padding: 10px 24px;
  background: #f44336;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  
  &:hover {
    background: #d32f2f;
  }
}

.error-msg {
  color: #d32f2f;
  font-size: 12px;
}

.error-message {
  color: #d32f2f;
  padding: 12px;
  background: #ffebee;
  border-radius: 4px;
}

.success-message {
  color: #2e7d32;
  padding: 12px;
  background: #e8f5e9;
  border-radius: 4px;
}
</style>
