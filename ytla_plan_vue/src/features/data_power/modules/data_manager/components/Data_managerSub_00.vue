<template>
  <div class="data-manager-sub">
    <!-- 返回 dashboard 按钮 -->
    <return-to-plan-dashboard-button />

    <!-- 上传区域 -->
    <div class="upload-section">
      <h3 class="upload-title">{{ $t('data_power.modules.data_manager.sub.upload_title') }}</h3>

      <div class="upload-area">
        <input
          ref="fileInputRef"
          type="file"
          class="file-input"
          @change="onFileSelected"
        />
        <button
          class="upload-btn"
          :disabled="!selectedFile || isUploading"
          @click="handleUpload"
        >
          {{ isUploading ? $t('data_power.modules.data_manager.sub.uploading') : $t('data_power.modules.data_manager.sub.upload_start') }}
        </button>
      </div>

      <!-- 上传错误 -->
      <div v-if="error" class="upload-error">{{ error }}</div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useDataManagerStore } from '@/features/data_power/modules/data_manager/stores/dataManagerStore.ts'
import ReturnToPlanDashboardButton from '@/features/data_power/modules/_type/ui/ReturnToPlanDashboardButton.vue'

const dataManagerStore = useDataManagerStore()

const fileInputRef = ref<HTMLInputElement | null>(null)
const selectedFile = ref<File | null>(null)

const isUploading = computed(() => dataManagerStore.isUploading)
const error = computed(() => dataManagerStore.error)

const onFileSelected = (event: Event) => {
  const input = event.target as HTMLInputElement
  if (input.files && input.files.length > 0) {
    selectedFile.value = input.files[0]
  }
}

const handleUpload = async () => {
  if (!selectedFile.value) return

  const result = await dataManagerStore.uploadFile(selectedFile.value)
  if (result.success) {
    selectedFile.value = null
    if (fileInputRef.value) {
      fileInputRef.value.value = ''
    }
  }
}
</script>

<style scoped lang="scss">
.data-manager-sub {
  padding: 20px;

  .upload-section {
    margin-top: 1rem;
    padding: 1rem;
    border: 1px solid #e0e0e0;
    border-radius: 8px;

    .upload-title {
      font-size: 1rem;
      font-weight: 600;
      margin-bottom: 0.75rem;
    }

    .upload-area {
      display: flex;
      gap: 10px;
      align-items: center;

      .file-input {
        flex: 1;
        padding: 6px;
        border: 1px solid #e0e0e0;
        border-radius: 4px;
        font-size: 0.875rem;
      }

      .upload-btn {
        padding: 8px 20px;
        background: #4CAF50;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 0.875rem;
        transition: background 0.2s;
        white-space: nowrap;

        &:hover:not(:disabled) {
          background: #388E3C;
        }

        &:disabled {
          background: #A5D6A7;
          cursor: not-allowed;
        }
      }
    }

    .upload-error {
      margin-top: 0.5rem;
      color: #d32f2f;
      font-size: 0.8rem;
    }
  }
}
</style>
