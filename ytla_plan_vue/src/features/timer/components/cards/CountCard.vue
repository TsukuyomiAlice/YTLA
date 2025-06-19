<template>
  <SideCard
    :card-id="cardId"
    :name="name"
    :icon="iconPath"
    :background="background"
    :tags="tags"
    :description="description"
    :showIcon=true
    :showTitle=true
    :showTags=true
    :showSettings=true
    :showDeactivate=true
    :showClose=true
    @settings="handleEdit"
  >
    <template #card-content>
      <div class="count-body">
        <!-- 主显示区 -->
        <div class="counter-display">
          <span
            class="value">{{ isFutureTime ? '0秒' : (isStopped ? finalDuration : formattedDuration)
            }}</span>
        </div>

        <!-- 状态容器 -->
        <div class="status-container">
          <!-- 状态第一行 -->
          <div class="status-line">
            <div class="status-left">
              <i class="fas fa-clock"></i>
              <span class="status-text">{{ statusText }}</span>
            </div>
            <div class="mode-tags">
              <span class="mode-tag">{{ modeLabel }}</span>
              <span v-if="isFutureTime" class="mode-tag">尚未开始</span>
            </div>
          </div>

          <!-- 状态第二行 -->
          <div v-if="showEndInfo || isFutureTime" class="end-line">
            <span class="end-info">
              {{ isFutureTime ? futureStartInfo : endInfo }}
            </span>
          </div>
        </div>
      </div>
    </template>

    <template #left-actions-buttons>
      <!-- 撤销按钮 -->
      <button
        class="action-button"
        @click="handleUndo"
        title="撤销到上一次计时状态"
      >
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20">
          <rect x="4" y="4" width="1" height="16" />
          <path d="M11 4 L4 12 L11 20z" />
          <path d="M18 4 L11 12 L18 20z" />
        </svg>
      </button>

      <!-- 重置按钮 -->
      <button
        class="action-button"
        @click="handleReset"
        title="从现在重新开始计时"
      >
        <svg viewBox="0 0 24 24" width="20" height="20">
          <rect x="4" y="4" width="5" height="16" />
          <path d="M10 4 L18 12 L10 20z" />
        </svg>
      </button>
    </template>

    <template #secondary-content>
      <div class="detail-panel">
        <div class="detail-item">
          <label>开始时间：</label>
          <span>{{ formattedStartTime }}</span>
        </div>
        <div class="detail-item">
          <label>计时模式：</label>
          <span>{{ countModeLabel }}</span>
        </div>

        <!-- 模式特定信息 -->
        <div v-if="countMode === 'count-until-time-across'" class="detail-item">
          <label>计时时长：</label>
          <span>{{ countSingleLengthValue }} {{ durationUnit }}</span>
        </div>
        <div v-if="countMode === 'count-until-specific-time'" class="detail-item">
          <label>终了时间：</label>
          <span>{{ formattedEndTime }}</span>
        </div>
        <div v-if="countMode === 'count-until-time-across'" class="detail-item">
          <label>下次时间：</label>
          <span>{{ formattedEndTime }}</span>
        </div>
      </div>
    </template>
  </SideCard>
</template>

<script setup lang="ts">
import { computed, ref, onMounted, onBeforeUnmount, inject } from 'vue'
import { useSideCardEditor } from '@/core/cards/composables/useSideCardEditor.ts'
import SideCard from '@/core/cards/components/SideCard.vue'
import type { CountCardData } from '@/features/timer/types/timerCardTypes'

const props = defineProps({
  // 通用属性
  cardId: Number,
  name: String,
  tags: String,
  description: String,
  iconPath: String,
  background: String,

  // 计时专用属性
  countMode: {
    type: String,
    validator: (val: string) => [
      'count-nonstop',
      'count-until-time-across',
      'count-until-specific-time'
    ].includes(val)
  },
  startTime: String,
  endTime: String,
  countSingleLengthUnit: String,
  countSingleLengthValue: Number
})

const startTime = ref(props.startTime)

const handleEdit = () => {
  const { showEdit } = useSideCardEditor()
  showEdit({
    card_id: props.cardId,
    name: props.name,
    tags: props.tags,
    description: props.description,
    card_sub_type: 'count',
    icon_path: props.iconPath,
    background_path: props.background,
    count_mode: props.countMode,
    count_single_length_value: props.countSingleLengthValue,
    count_single_length_unit: props.countSingleLengthUnit,
    start_time: props.startTime,
    end_time: props.endTime
  } as CountCardData)
}

// 实时时间更新
const now = ref(Date.now())
let timer: number

const updateTime = () => {
  now.value = Date.now()
}

onMounted(() => {
  timer = window.setInterval(updateTime, 1000)
})

onBeforeUnmount(() => {
  clearInterval(timer)
})

// 核心计算属性
const startTimestamp = computed(() => {
  try {
    const parseDate = (dateStr: string) => {
      if (/^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$/.test(dateStr)) {
        const [datePart, timePart] = dateStr.split(' ')
        const [year, month, day] = datePart.split('-').map(Number)
        const [hours, minutes, seconds] = timePart.split(':').map(Number)
        return new Date(year, month - 1, day, hours, minutes, seconds).getTime()
      }
      return new Date(dateStr).getTime()
    }
    return parseDate(startTime.value as string)
  } catch {
    console.error('无效的开始时间格式:', startTime.value)
    return 0
  }
})

const countModeLabel = computed(() => {
  return {
    'count-nonstop': '不停止',
    'count-until-time-across': '超时停止',
    'count-until-specific-time': '指定时间'
  }[props.countMode || 'count-nonstop']
})

const durationUnit = computed(() => {
  return {
    day: '天',
    hour: '小时',
    minute: '分钟'
  }[props.countSingleLengthUnit || 'day']
})

const formattedEndTime = computed(() => {
  try {
    return new Date(props.endTime as string).toLocaleString('zh-CN', {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit'
    })
  } catch {
    return '无效时间格式'
  }
})

const targetDurationMs = computed(() => {
  if (props.countMode === 'count-until-specific-time') {
    try {
      const endTime = new Date(props.endTime as string).getTime()
      return endTime - startTimestamp.value
    } catch {
      return 0
    }
  } else if (props.countMode === 'count-until-time-across') {
    const timeUnitMap = {
      day: 86400000,
      hour: 3600000,
      minute: 60000
    }
    type TimeUnit = keyof typeof timeUnitMap;
    const unit = (props.countSingleLengthUnit || 'day') as TimeUnit
    return (props.countSingleLengthValue || 0) * timeUnitMap[unit]
  }
  return Infinity
})

const elapsed = computed(() => {
  if (!startTimestamp.value) return 0
  if (props.countMode === 'count-nonstop') {
    return now.value - startTimestamp.value
  }
  return Math.min(now.value - startTimestamp.value, targetDurationMs.value)
})

const isStopped = computed(() => {
  if (props.countMode === 'count-nonstop') return false
  return now.value >= (startTimestamp.value + targetDurationMs.value)
})

const isFutureTime = computed(() => now.value < startTimestamp.value)

const formattedDuration = computed(() => {
  const seconds = Math.floor(elapsed.value / 1000)
  const days = Math.floor(seconds / 86400)
  const hours = Math.floor((seconds % 86400) / 3600)
  const minutes = Math.floor((seconds % 3600) / 60)
  const secs = seconds % 60

  return [
    days > 0 ? `${days}天` : '',
    hours > 0 ? `${hours}时` : '',
    minutes > 0 ? `${minutes}分` : '',
    `${secs}秒`
  ].filter(Boolean).join(' ') || '0秒'
})

const finalDuration = computed(() => {
  return formattedDuration.value + ' (已停止)'
})

const modeLabel = computed(() => {
  return {
    'count-nonstop': '持续',
    'count-until-time-across': '滚动',
    'count-until-specific-time': '单次'
  }[props.countMode || 'count-nonstop']
})

const statusText = computed(() => {
  if (isFutureTime.value) return '尚未开始'
  return isStopped.value ? '已停止' : '计时中'
})

const endInfo = computed(() => {
  if (isStopped.value || props.countMode === 'count-nonstop') return ''
  return `剩余 ${formattedRemainingTime.value}`
})

const formattedRemainingTime = computed(() => {
  const remaining = targetDurationMs.value - elapsed.value
  return remaining > 0 ? formatDuration(remaining) : '0秒'
})

const showEndInfo = computed(() =>
  props.countMode !== 'count-nonstop' && !isStopped.value
)

const futureStartInfo = computed(() => {
  const diff = startTimestamp.value - now.value
  return `${formatDuration(diff)}后开始`
})

// 工具函数
const formatDuration = (ms: number) => {
  const seconds = Math.floor(ms / 1000)
  const days = Math.floor(seconds / 86400)
  const hours = Math.floor((seconds % 86400) / 3600)
  const minutes = Math.floor((seconds % 3600) / 60)
  const secs = seconds % 60

  return [
    days > 0 ? `${days}天` : '',
    hours > 0 ? `${hours}时` : '',
    minutes > 0 ? `${minutes}分` : '',
    `${secs}秒`
  ].filter(Boolean).join(' ') || '0秒'
}

const formattedStartTime = computed(() => {
  try {
    const date = new Date(startTimestamp.value)
    return isNaN(date.getTime())
      ? '无效时间'
      : date.toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        hour12: false
      })
  } catch {
    return '时间解析失败'
  }
})

const API_BASE = 'http://localhost:5000'
const handleReset = async () => {
  try {
    const response = await fetch(`${API_BASE}/card_action/${props.cardId}/timer_count_reset`, {
      method: 'POST'
    })
    const data = await response.json()

    if (data.success) {
      // 更新本地 startTime
      startTime.value = data.new_start_time
      // 触发界面刷新
      now.value = Date.now()
      if (props.countMode === 'count-until-time-across') {
        formattedStartTime
      }
    }
  } catch (error) {
    console.error('重置失败:', error)
  }
}


const handleUndo = async () => {
  try {
    const response = await fetch(`${API_BASE}/card_action/${props.cardId}/timer_count_undo`, {
      method: 'POST'
    })
    const data = await response.json()

    if (data.success) {
      // 更新本地 startTime
      startTime.value = data.new_start_time
      // 触发界面刷新
      now.value = Date.now()
    }
  } catch (error) {
    console.error('重置失败:', error)
  }
}

</script>

<style lang="scss" scoped>
.count-body {
  padding: 0.25rem 0;

  .counter-display {
    margin-bottom: 0.25rem;

    .value {
      font-size: 0.9rem;
      color: #2c3e50;
      display: block;
      text-align: left;
      letter-spacing: -0.03em;
    }
  }

  .status-container {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .status-line {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
    gap: 0.5rem;
  }

  .status-left {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex: 1;

    i {
      font-size: 0.9rem;
      color: #666;
      min-width: 1rem;
      text-align: center;
    }

    .status-text {
      font-size: 0.9rem;
      white-space: nowrap;
    }
  }

  .mode-tag {
    background: #e8f4ff;
    color: #2196f3;
    padding: 0.25rem 0.75rem;
    border-radius: 0.75rem;
    font-size: 0.85rem;
    margin-left: 0;
  }

  .end-line {
    display: flex;
    justify-content: flex-end;
    width: 100%;

    .end-info {
      color: #888;
      font-size: 0.85rem;
      text-align: right;
      padding-right: 0.5rem;
    }
  }
}

.detail-panel {
  padding: 0;

  .detail-item {
    display: flex;
    justify-content: space-between;
    padding: 0.2rem 0;
    border-bottom: 1px solid #eee;
    font-size: 0.9rem;

    label {
      color: #888;
      min-width: 4.5rem;
    }

    span {
      color: #444;
      font-weight: 500;
      max-width: 12rem;
      text-align: right;
    }
  }
}

@media (max-width: 480px) {
  .count-body {
    .end-line .end-info {
      text-align: left;
      padding-right: 0;
    }
  }
}

.action-button {
  background: transparent;
  border: none;
  cursor: pointer;
  outline: none;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 1.25rem;
  height: 1.25rem;
  color: gray;
  transition: color 0.3s ease;

  svg {
    fill: currentColor;
  }

  &:hover {
    color: #2196f3;
  }
}
</style>
