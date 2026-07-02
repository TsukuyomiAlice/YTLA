<template>
  <div class="data-manager-container">
    <h2 class="section-title">{{ $t('data_power.modules.data_manager.main.title') }}</h2>

    <!-- 错误信息 -->
    <div v-if="error" class="error-message">{{ error }}</div>

    <!-- 加载中 -->
    <div v-if="isLoading" class="loading-state">{{ $t('data_power.modules.data_manager.sub.uploading') }}</div>

    <!-- 空状态 -->
    <div v-else-if="files.length === 0" class="empty-state">
      {{ $t('data_power.modules.data_manager.main.no_files') }}
    </div>

    <!-- 文件列表 -->
    <div v-else class="file-list">
      <div class="file-header">
        <span class="col-name">{{ $t('data_power.modules.data_manager.main.col_name') }}</span>
        <span class="col-module-id">{{ $t('data_power.modules.data_manager.main.col_module_id') }}</span>
        <span class="col-module-subtype">{{ $t('data_power.modules.data_manager.main.col_module_subtype') }}</span>
        <span class="col-size">{{ $t('data_power.modules.data_manager.main.col_size') }}</span>
        <span class="col-time">{{ $t('data_power.modules.data_manager.main.col_time') }}</span>
        <span class="col-action">{{ $t('data_power.modules.data_manager.main.col_action') }}</span>
      </div>
      <div
        v-for="file in files"
        :key="file.file_path"
        class="file-row"
      >
        <span class="col-name" :title="file.file_name">{{ file.file_name }}</span>
        <span class="col-module-id">{{ file.module_id }}</span>
        <span class="col-module-subtype">{{ file.module_subtype_name }}</span>
        <span class="col-size">{{ formatFileSize(file.file_size) }}</span>
        <span class="col-time">{{ file.upload_time }}</span>
        <span class="col-action">
          <button
            class="delete-btn"
            @click="handleDelete(file.file_path)"
          >
            {{ $t('data_power.modules.data_manager.main.delete_btn') }}
          </button>
        </span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { useDataManagerStore } from '@/features/data_power/modules/data_manager/stores/dataManagerStore.ts'

const dataManagerStore = useDataManagerStore()

const files = computed(() => dataManagerStore.files)
const isLoading = computed(() => dataManagerStore.isLoading)
const error = computed(() => dataManagerStore.error)

const formatFileSize = (bytes: number): string => {
  const units = ['B', 'KB', 'MB', 'GB']
  let size = bytes
  let unitIndex = 0
  while (size >= 1024 && unitIndex < units.length - 1) {
    size /= 1024
    unitIndex++
  }
  return `${size.toFixed(1)} ${units[unitIndex]}`
}

const handleDelete = async (filePath: string) => {
  if (!confirm('确定要删除该文件吗？')) return
  await dataManagerStore.deleteFile(filePath)
}

onMounted(() => {
  dataManagerStore.fetchFiles()
})
</script>

<style scoped lang="scss">
.data-manager-container {
  padding: 20px;

  .section-title {
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: 1rem;
  }

  .error-message {
    color: #d32f2f;
    padding: 10px;
    margin-bottom: 1rem;
    background: #fdecea;
    border-radius: 4px;
  }

  .loading-state {
    text-align: center;
    padding: 2rem;
    color: #666;
  }

  .empty-state {
    text-align: center;
    padding: 2rem;
    color: #999;
  }

  .file-list {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    overflow: hidden;

    .file-header {
      display: flex;
      padding: 10px 16px;
      background: #f5f5f5;
      font-weight: 600;
      font-size: 0.875rem;
      border-bottom: 1px solid #e0e0e0;
    }

    .file-row {
      display: flex;
      padding: 10px 16px;
      border-bottom: 1px solid #f0f0f0;
      align-items: center;
      font-size: 0.875rem;

      &:last-child {
        border-bottom: none;
      }

      &:hover {
        background: #fafafa;
      }
    }

    .col-name {
      flex: 3;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    .col-module-id {
      flex: 1;
      text-align: center;
    }

    .col-module-subtype {
      flex: 1.5;
      text-align: center;
    }

    .col-size {
      flex: 1;
      text-align: center;
    }

    .col-time {
      flex: 2;
      text-align: center;
    }

    .col-action {
      flex: 1;
      text-align: right;
    }

    .delete-btn {
      padding: 4px 12px;
      background: #e53935;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 0.8rem;
      transition: background 0.2s;

      &:hover {
        background: #c62828;
      }
    }
  }
}
</style>
