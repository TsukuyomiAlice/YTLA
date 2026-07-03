<template>
  <div class="ec-sub">
    <!-- return to dashboard 按钮 -->
    <return-to-plan-dashboard-button />

    <!-- 加载中 -->
    <div v-if="store.isLoading" class="ec-sub-loading">
      {{ $t('divination.modules.eight_characters.main.loading') }}
    </div>

    <!-- 空状态 -->
    <div v-else-if="store.historyRecords.length === 0" class="ec-sub-empty">
      {{ $t('divination.modules.eight_characters.sub.empty') }}
    </div>

    <!-- 历史记录列表 -->
    <div v-else class="ec-sub-list">
      <h3 class="ec-sub-title">{{ $t('divination.modules.eight_characters.sub.title') }}</h3>
      <div
        v-for="record in store.historyRecords"
        :key="record.RECORD_ID"
        class="ec-sub-item"
        :class="{ 'ec-sub-item--selected': store.selectedRecord?.RECORD_ID === record.RECORD_ID }"
        @click="handleSelect(record)"
      >
        <div class="ec-sub-item__main">
          <span class="ec-sub-item__pillars">{{ formatPillars(record) }}</span>
          <span class="ec-sub-item__time">{{ formatTime(record.UPDATE_DATETIME) }}</span>
        </div>
        <button
          class="ec-sub-item__delete"
          @click.stop="handleDelete(record)"
          :title="$t('divination.modules.eight_characters.sub.delete_confirm')"
        >
          ✕
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onActivated, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { useEightCharactersStore } from '@/features/divination/modules/eight_characters/stores/eightCharactersStore.ts'
import type { HistoryRecord } from '@/features/divination/modules/eight_characters/stores/eightCharactersStore.ts'
import ReturnToPlanDashboardButton from '@/features/divination/modules/_type/ui/ReturnToPlanDashboardButton.vue'

const { t } = useI18n()
const store = useEightCharactersStore()

onMounted(() => {
  store.fetchHistoryList()
})

// 每次页面切换到前台时自动刷新历史记录列表
onActivated(() => {
  store.fetchHistoryList()
})

function formatPillars(record: HistoryRecord): string {
  const ec = record.EIGHT_CHARACTERS
  if (!ec || ec.length < 8) return '--'
  // ec 格式如 "癸酉辛酉壬申己丑"，每2个字一柱
  const parts = []
  for (let i = 0; i < 8; i += 2) {
    parts.push(ec.substring(i, i + 2))
  }
  return parts.join('  ')
}

function formatTime(dateStr: string): string {
  if (!dateStr) return ''
  const d = new Date(dateStr)
  const pad = (n: number) => String(n).padStart(2, '0')
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}`
}

function handleSelect(record: HistoryRecord) {
  store.selectHistoryRecord(record)
}

async function handleDelete(record: HistoryRecord) {
  const confirmed = confirm(t('divination.modules.eight_characters.sub.delete_confirm'))
  if (!confirmed) return
  await store.deleteHistoryRecord(record.EIGHT_CHARACTERS, record.GENDER)
  // Store 的 deleteHistoryRecord 已做本地过滤，删除后列表会自动更新
}
</script>

<style scoped lang="scss">
.ec-sub {
  padding: 20px;

  .ec-sub-loading,
  .ec-sub-empty {
    text-align: center;
    padding: 2rem;
    color: #999;
  }

  .ec-sub-list {
    margin-top: 1rem;

    .ec-sub-title {
      font-size: 1rem;
      font-weight: 600;
      margin-bottom: 0.75rem;
      color: #333;
    }

    .ec-sub-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 16px;
      border: 1px solid #e8e8e8;
      border-radius: 8px;
      margin-bottom: 8px;
      cursor: pointer;
      transition: background-color 0.2s, border-color 0.2s;

      &:hover {
        background-color: #f9f9f9;
        border-color: #d0d0d0;
      }

      &--selected {
        background-color: #e6f7ff;
        border-color: #91d5ff;

        &:hover {
          background-color: #e6f7ff;
        }
      }

      &__main {
        display: flex;
        flex-direction: column;
        gap: 4px;
        min-width: 0;
      }

      &__pillars {
        font-size: 0.9375rem;
        font-weight: 500;
        color: #333;
        font-family: 'Noto Sans SC', 'Microsoft YaHei', sans-serif;
        letter-spacing: 0.02em;
      }

      &__time {
        font-size: 0.75rem;
        color: #999;
      }

      &__delete {
        flex-shrink: 0;
        width: 28px;
        height: 28px;
        border: none;
        background: transparent;
        border-radius: 50%;
        cursor: pointer;
        font-size: 0.8125rem;
        color: #ccc;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: background-color 0.2s, color 0.2s;

        &:hover {
          background-color: #fff1f0;
          color: #ff4d4f;
        }
      }
    }
  }
}
</style>
