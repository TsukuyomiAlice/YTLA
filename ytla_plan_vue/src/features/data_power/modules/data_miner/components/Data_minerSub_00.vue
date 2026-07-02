<template>
  <div class="data-miner-sub">
    <!-- return to dashboard 按钮 -->
    <return-to-plan-dashboard-button />

    <!-- 加载中 -->
    <div v-if="isLoading" class="loading-state">{{ $t('data_power.modules.data_miner.sub.loading') }}</div>

    <!-- 无数据 -->
    <div v-else-if="!fileContent" class="empty-state">
      {{ $t('data_power.modules.data_miner.sub.no_content') }}
    </div>

    <!-- 单表数据展示 -->
    <div v-else-if="fileContent.file_type === 'table'" class="content-section">
      <h3 class="content-title">{{ currentFile?.file_name || $t('data_power.modules.data_miner.sub.table_title') }}</h3>
      <div class="table-wrapper">
        <table class="data-table">
          <thead>
            <tr>
              <th v-for="col in fileContent.columns" :key="col">{{ col }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(row, idx) in fileContent.rows" :key="idx">
              <td v-for="col in fileContent.columns" :key="col">{{ row[col] }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- 多表逐一展示 -->
    <div v-else-if="fileContent.file_type === 'multi_table'" class="content-section">
      <h3 class="content-title">{{ currentFile?.file_name || $t('data_power.modules.data_miner.sub.table_title') }}</h3>
      <div v-for="(tbl, idx) in fileContent.tables" :key="idx" class="multi-table-block">
        <h4 class="table-subtitle">{{ tbl.name }}</h4>
        <div class="table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th v-for="col in tbl.columns" :key="col">{{ col }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(row, ridx) in tbl.rows" :key="ridx">
                <td v-for="col in tbl.columns" :key="col">{{ row[col] }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- JSON 数据展示 -->
    <div v-else-if="fileContent.file_type === 'json'" class="content-section">
      <h3 class="content-title">{{ currentFile?.file_name || $t('data_power.modules.data_miner.sub.json_title') }}</h3>
      <pre class="json-content">{{ fileContent.content }}</pre>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted } from 'vue'
import { useData_minerStore } from '@/features/data_power/modules/data_miner/stores/data_minerStore.ts'
import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'
import ReturnToPlanDashboardButton from '@/features/data_power/modules/_type/ui/ReturnToPlanDashboardButton.vue'

const dataMinerStore = useData_minerStore()
const moduleProcessStore = useModuleProcessStore()

const isLoading = ref(false)

interface TableData {
  name: string
  columns: string[]
  rows: Record<string, any>[]
}

const fileContent = ref<{
  file_type: string
  columns?: string[]
  rows?: Record<string, any>[]
  tables?: TableData[]
  content?: string
} | null>(null)

const currentFile = ref<any>(null)

const fetchContent = async (file: any) => {
  isLoading.value = true
  currentFile.value = file
  fileContent.value = null
  const planId = moduleProcessStore.belongPlanId
  if (!planId) {
    isLoading.value = false
    return
  }
  try {
    const result = await dataMinerStore.viewProcessedFile(planId, file.file_path)
    if (result.success && result.data) {
      fileContent.value = result.data
    }
  } catch (e) {
    fileContent.value = null
  } finally {
    isLoading.value = false
  }
}

// 监听 Store 的当前查看文件变化
watch(
  () => dataMinerStore.currentViewFile,
  (newFile) => {
    if (newFile) {
      fetchContent(newFile)
    } else {
      currentFile.value = null
      fileContent.value = null
    }
  },
  { immediate: true }
)
</script>

<style scoped lang="scss">
.data-miner-sub {
  padding: 20px;

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

  .content-section {
    margin-top: 1rem;

    .content-title {
      font-size: 1rem;
      font-weight: 600;
      margin-bottom: 0.75rem;
    }

    .table-wrapper {
      overflow-x: auto;
      border: 1px solid #e0e0e0;
      border-radius: 8px;

      .data-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.875rem;

        thead {
          background: #f5f5f5;

          th {
            padding: 10px 16px;
            text-align: left;
            font-weight: 600;
            border-bottom: 1px solid #e0e0e0;
            white-space: nowrap;
          }
        }

        tbody {
          tr {
            border-bottom: 1px solid #f0f0f0;

            &:last-child {
              border-bottom: none;
            }

            &:hover {
              background: #fafafa;
            }

            td {
              padding: 8px 16px;
              white-space: nowrap;
            }
          }
        }
      }
    }

    .multi-table-block {
      margin-bottom: 1.5rem;

      &:last-child {
        margin-bottom: 0;
      }

      .table-subtitle {
        font-size: 0.9375rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #444;
      }
    }

    .json-content {
      background: #f5f5f5;
      border: 1px solid #e0e0e0;
      border-radius: 8px;
      padding: 16px;
      overflow-x: auto;
      font-size: 0.8125rem;
      line-height: 1.5;
      max-height: 500px;
      overflow-y: auto;
    }
  }
}
</style>
