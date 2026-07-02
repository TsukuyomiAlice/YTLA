<template>
  <div class="data-miner-container">
    <h2 class="section-title">{{ $t('data_power.modules.data_miner.main.title') }}</h2>

    <!-- 状态消息 -->
    <div v-if="statusMsg" class="status-message" :class="statusType">{{ statusMsg }}</div>

    <!-- 加载中 -->
    <div v-if="isLoading" class="loading-state">{{ $t('data_power.modules.data_miner.main.loading') }}</div>

    <!-- 空状态 -->
    <div v-else-if="mergedFiles.length === 0" class="empty-state">
      {{ $t('data_power.modules.data_miner.main.no_files') }}
    </div>

    <!-- 文件列表 -->
    <div v-else class="file-list">
      <div class="file-header">
        <span class="col-name">{{ $t('data_power.modules.data_miner.main.col_filename') }}</span>
        <span class="col-module-id">{{ $t('data_power.modules.data_miner.main.col_module_id') }}</span>
        <span class="col-source">{{ $t('data_power.modules.data_miner.main.col_source') }}</span>
        <span class="col-size">{{ $t('data_power.modules.data_miner.main.col_size') }}</span>
        <span class="col-time">{{ $t('data_power.modules.data_miner.main.col_time') }}</span>
        <span class="col-action">{{ $t('data_power.modules.data_miner.main.col_action') }}</span>
      </div>
      <div
        v-for="row in mergedFiles"
        :key="`${row.source}_${row.file_path}`"
        class="file-row"
      >
        <span class="col-name" :title="row.file_name">{{ row.file_name }}</span>
        <span class="col-module-id">{{ row.module_id }}</span>
        <span class="col-source">
          <span v-if="row.source === 'raw'" class="source-tag source-raw">{{ row.source_label }}</span>
          <span v-else class="source-tag source-processed">{{ row.source_label }}</span>
        </span>
        <span class="col-size">{{ formatFileSize(row.file_size) }}</span>
        <span class="col-time">{{ row.generated_time }}</span>
        <span class="col-action">
          <!-- 原始文件：分析按钮 -->
          <button
            v-if="row.source === 'raw'"
            class="action-btn analyze-btn"
            :disabled="processingFilePath === row.file_path"
            @click="handleProcess(row)"
          >
            {{ processingFilePath === row.file_path
              ? $t('data_power.modules.data_miner.main.processing')
              : $t('data_power.modules.data_miner.main.analyze_btn') }}
          </button>
          <!-- 已处理文件：查看 + 删除按钮 -->
          <template v-else>
            <button
              class="action-btn view-btn"
              @click="handleView(row)"
            >
              {{ $t('data_power.modules.data_miner.main.view_btn') }}
            </button>
            <button
              class="action-btn delete-btn"
              @click="handleDelete(row)"
            >
              {{ $t('data_power.modules.data_miner.main.delete_btn') }}
            </button>
          </template>
        </span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onActivated, ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { useData_minerStore } from '@/features/data_power/modules/data_miner/stores/data_minerStore.ts'
import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'

const dataMinerStore = useData_minerStore()
const { t } = useI18n()
const moduleProcessStore = useModuleProcessStore()

const isLoading = ref(false)
const processingFilePath = ref<string | null>(null)
const statusMsg = ref<string>('')
const statusType = ref<'success' | 'error'>('success')

const sourceFiles = computed(() => dataMinerStore.sourceFiles)
const processedFiles = computed(() => dataMinerStore.processedFiles)

const mergedFiles = computed(() => {
  const rawItems = (sourceFiles.value || []).map(f => ({
    file_name: f.file_name,
    file_path: f.file_path,
    file_size: f.file_size,
    generated_time: f.upload_time,
    module_id: f.module_id,
    source: 'raw' as const,
    source_label: 'Data Manager'
  }))

  const processedItems = (processedFiles.value || []).map(f => ({
    file_name: f.file_name,
    file_path: f.file_path,
    file_size: f.file_size,
    generated_time: f.processed_time,
    module_id: f.module_id,
    source: 'processed' as const,
    source_label: 'Data Miner'
  }))

  return [...rawItems, ...processedItems]
})

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

const clearStatus = () => {
  statusMsg.value = ''
}

const fetchAllFiles = async () => {
  isLoading.value = true
  clearStatus()
  try {
    await Promise.all([
      dataMinerStore.fetchSourceFiles(),
      dataMinerStore.fetchProcessedFiles(),
    ])
  } catch (e) {
    statusMsg.value = '加载文件列表失败'
    statusType.value = 'error'
  } finally {
    isLoading.value = false
  }
}

const handleProcess = async (row: any) => {
  clearStatus()
  const planId = moduleProcessStore.belongPlanId
  if (!planId) {
    statusMsg.value = '无法获取计划ID'
    statusType.value = 'error'
    return
  }
  const currentModuleId = moduleProcessStore.moduleId
  if (typeof currentModuleId !== 'number') {
    statusMsg.value = '无法获取当前模组ID'
    statusType.value = 'error'
    return
  }
  processingFilePath.value = row.file_path
  try {
    const result = await dataMinerStore.processFile(planId, row.file_path, currentModuleId)
    if (result.success) {
      statusMsg.value = '文件分析完成'
      statusType.value = 'success'
      await fetchAllFiles()
    } else {
      statusMsg.value = result.message || '分析失败'
      statusType.value = 'error'
    }
  } catch (e) {
    statusMsg.value = '分析过程出错'
    statusType.value = 'error'
  } finally {
    processingFilePath.value = null
  }
}

const handleView = (row: any) => {
  clearStatus()
  dataMinerStore.showSubView(row)
}

const handleDelete = async (row: any) => {
  clearStatus()
  if (!confirm(t('data_power.modules.data_miner.confirm_delete'))) return
  const planId = moduleProcessStore.belongPlanId
  if (!planId) {
    statusMsg.value = '无法获取计划ID'
    statusType.value = 'error'
    return
  }
  try {
    const result = await dataMinerStore.deleteProcessedFile(planId, row.file_path)
    if (result.success) {
      // 如果删除的文件正好是 sub 区域当前显示的内容，则清空 sub 区域
      const currentViewFile = dataMinerStore.currentViewFile
      if (currentViewFile) {
        const deletedDir = row.file_path.substring(0, row.file_path.lastIndexOf('/'))
        const currentDir = currentViewFile.file_path.substring(0, currentViewFile.file_path.lastIndexOf('/'))
        if (row.file_path === currentViewFile.file_path || deletedDir === currentDir) {
          dataMinerStore.hideSubView()
        }
      }
      statusMsg.value = t('data_power.modules.data_miner.delete_success')
      statusType.value = 'success'
      await fetchAllFiles()
    } else {
      statusMsg.value = result.message || '删除失败'
      statusType.value = 'error'
    }
  } catch (e) {
    statusMsg.value = '删除过程出错'
    statusType.value = 'error'
  }
}

onActivated(() => {
  fetchAllFiles()
})
</script>

<style scoped lang="scss">
.data-miner-container {
  padding: 20px;

  .section-title {
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: 1rem;
  }

  .status-message {
    padding: 8px 12px;
    margin-bottom: 0.75rem;
    border-radius: 4px;
    font-size: 0.875rem;

    &.success {
      color: #2e7d32;
      background: #e8f5e9;
    }

    &.error {
      color: #d32f2f;
      background: #fdecea;
    }
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

    .col-source {
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
      flex: 1.5;
      text-align: right;
      display: flex;
      gap: 6px;
      justify-content: flex-end;
    }

    .source-tag {
      display: inline-block;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 0.75rem;

      &.source-raw {
        background: #e3f2fd;
        color: #1565c0;
      }

      &.source-processed {
        background: #f3e5f5;
        color: #7b1fa2;
      }
    }

    .action-btn {
      padding: 4px 12px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 0.8rem;
      transition: background 0.2s;
      white-space: nowrap;

      &.analyze-btn {
        background: #1976d2;
        color: white;

        &:hover:not(:disabled) {
          background: #1565c0;
        }

        &:disabled {
          background: #90caf9;
          cursor: not-allowed;
        }
      }

      &.view-btn {
        background: #388e3c;
        color: white;

        &:hover {
          background: #2e7d32;
        }
      }

      &.delete-btn {
        background: #e53935;
        color: white;

        &:hover {
          background: #c62828;
        }
      }
    }
  }
}
</style>
