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
      <div class="countdown-body">
        <!-- 主显示区 -->
        <div class="counter-display">
          <span class="value">{{ displayTime }}</span>
        </div>

        <!-- 状态容器 -->
        <div class="status-container">
          <!-- 状态第一行 -->
          <div class="status-line">
            <div class="status-left">
              <i class="fas fa-hourglass-half"></i>
              <span class="status-text">{{ statusText }}</span>
            </div>
            <div class="mode-tags">
              <span class="mode-tag">{{ modeLabel }}</span>
              <span v-if="isNotStarted" class="mode-tag">尚未开始</span>
            </div>
          </div>

          <!-- 第二行状态 -->
          <div v-if="showRemaining || isFutureTime" class="end-line">
            <span
              class="end-info"> {{ isFutureTime ? `${futureStartInfo}` : `剩余 ${formattedRemainingTime}`
              }} </span>
          </div>
        </div>
      </div>
    </template>

    <template #secondary-content>
      <div class="detail-panel">
        <div class="detail-item">
          <label>开始时间：</label>
          <span>{{ formattedStartTime }}</span>
        </div>

        <!-- 单次模式特定信息 -->
        <template v-if="isSingle">
          <div class="detail-item">
            <label>计时模式：</label>
            <span>{{ countdownType }}</span>
          </div>
          <div v-if="isSpecificTimeMode" class="detail-item">
            <label>结束时间：</label>
            <span>{{ formattedEndTime }}</span>
          </div>
          <template v-else>
            <div class="detail-item">
              <label>持续时长：</label>
              <span>{{ durationPeriod }}</span>
            </div>
            <div class="detail-item">
              <label>结束时间：</label>
              <span>{{ formattedEndTime }}</span>
            </div>
          </template>
        </template>

        <!-- 重复模式信息 -->
        <template v-if="isRepeat">
          <div class="detail-item">
            <label>重复周期：</label>
            <span>{{ repeatPeriod }}</span>
          </div>
          <div class="detail-item">
            <label>下次到期：</label>
            <span>{{ formattedNextTime }}</span>
          </div>
        </template>
      </div>
    </template>
  </SideCard>
</template>

<script setup lang="ts">
import { computed, ref, onMounted, onBeforeUnmount } from 'vue'
import { useSideCardEditor } from '@/core/domain/area/cards/composables/useSideCardEditor.ts'
import SideCard from '@/core/domain/area/cards/components/SideCard.vue'
import type { CountdownCardData } from '@/features/timer/cards/countdown/types/cardDataType.ts'

//// Props 和 Emits 定义
const props = defineProps({
  // 通用属性
  cardId: Number,
  name: String,
  tags: String,
  description: String,
  iconPath: String,
  background: String,

  // 倒计时专用属性
  countdownMode: {
    type: String,
    validator: (val: string) => ['single', 'repeat'].includes(val)
  },
  startTime: String,
  countdownSingleMode: {
    type: String,
    validator: (val: string) => ['countdown-until-specific-time', 'countdown-time-limit'].includes(val)
  },
  endTime: String,
  countdownSingleLengthValue: Number,
  countdownSingleLengthUnit: {
    type: String,
    validator: (val: string): val is TimeUnit => ['minute', 'hour', 'day'].includes(val)
  },
  countdownRepeatPeriodValue: Number,
  countdownRepeatPeriodUnit: {
    type: String,
    validator: (val: string): val is TimeUnit => ['minute', 'hour', 'day'].includes(val)
  },
})

//// 响应式数据
const now = ref(Date.now())

let timer: number

//// 常量与工具函数
const timeUnitMap = {
  minute: 60000,
  hour: 3600000,
  day: 86400000,
}
type TimeUnit = keyof typeof timeUnitMap;

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

const formatDate = (dateStr: string | number) => {
  try {
    const date = new Date(dateStr)
    if (isNaN(date.getTime())) return '--/--/-- --:--'
    return date.toLocaleString('zh-CN', {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit'
    })
  } catch {
    return '--/--/-- --:--'
  }
}

//// 计算属性
const isSingle = computed(() => props.countdownMode === 'single')
const isRepeat = computed(() => props.countdownMode === 'repeat')
const isSpecificTimeMode = computed(() => props.countdownSingleMode === 'countdown-until-specific-time')
const isTimeLimitMode = computed(() => props.countdownSingleMode === 'countdown-time-limit')

const startTimestamp = computed(() => new Date(props.startTime as string).getTime())
const endTimestamp = computed(() => new Date(props.endTime as string).getTime())

const singleEndTimestamp = computed(() => {
  if (isSpecificTimeMode.value) {
    return endTimestamp.value
  }
  const unit = (props.countdownSingleLengthUnit || 'minute') as TimeUnit;
  return startTimestamp.value + (props.countdownSingleLengthValue || 0) * timeUnitMap[unit];
})

const timeLeft = computed(() => {
  const diff = targetDate.value - now.value
  return diff > 0 ? diff : 0
})

const totalDuration = computed(() => {
  if (isSingle.value && isTimeLimitMode.value) {
    const unit = (props.countdownSingleLengthUnit || 'minute') as TimeUnit;
    return (props.countdownSingleLengthValue || 0) * timeUnitMap[unit];
  }
  return targetDate.value - startTimestamp.value
})

const elapsed = computed(() => totalDuration.value - timeLeft.value)

const nextRepeatDate = computed(() => {
  if (!isRepeat.value) return 0

  // 对于重复模式，直接使用结束时间作为目标日期
  return endTimestamp.value
})

const targetDate = computed(() => {
  if (isSingle.value) return singleEndTimestamp.value
  return nextRepeatDate.value
})

const displayTime = computed(() => {
  if (isRepeat.value) {
    // 对于重复模式，显示从开始时间到结束时间的完整时长
    return formatDuration(endTimestamp.value - startTimestamp.value)
  }
  if (now.value < startTimestamp.value) {
    return formatDuration(singleEndTimestamp.value - startTimestamp.value)
  }
  return formatDuration(timeLeft.value)
})

const formattedRemainingTime = computed(() => formatDuration(timeLeft.value))

const modeLabel = computed(() => {
  return isRepeat.value ? '循环' : '单次'
})

const isFutureTime = computed(() => now.value < startTimestamp.value)

const futureStartInfo = computed(() => {
  const diff = startTimestamp.value - now.value
  return `${formatDuration(diff)}后开始`
})

const statusText = computed(() => {
  if (isFutureTime.value) return '尚未开始'
  return timeLeft.value > 0 ? '倒计时中' : '已停止'
})

const countdownType = computed(() => {
  return isSpecificTimeMode.value ? '指定时间' : '指定时长'
})

const showRemaining = computed(() =>
  timeLeft.value > 0 && !isFutureTime.value
)

const timeUnit = computed(() => ({
  minute: '分钟',
  hour: '小时',
  day: '天'
})[props.countdownRepeatPeriodUnit || 'minute'] || '单位错误')

const durationUnit = computed(() => ({
  minute: '分钟',
  hour: '小时',
  day: '天'
})[props.countdownSingleLengthUnit || 'minute'] || '单位错误')

const durationPeriod = computed(() => {
  if (isSingle.value && isTimeLimitMode.value) {
    return `${props.countdownSingleLengthValue} ${durationUnit.value}`
  }
  return ''
})

const formattedStartTime = computed(() => formatDate(props.startTime as string))
const formattedEndTime = computed(() => {
  if (isSpecificTimeMode.value) return formatDate(props.endTime as string)
  return formatDate(singleEndTimestamp.value) // 显示计算出的结束时间
})
const formattedNextTime = computed(() => formatDate(targetDate.value))

const repeatPeriod = computed(() => {
  if (isRepeat.value) {
    return `每 ${props.countdownRepeatPeriodValue} ${timeUnit.value}`
  }
  return ''
})

const isNotStarted = computed(() => startTimestamp.value > now.value)

//// 生命周期钩子
onMounted(() => {
  try {
    timer = window.setInterval(updateTime, 1000)
  } catch (error) {
    console.error('Failed to start timer:', error)
  }
})

onBeforeUnmount(() => {
  clearInterval(timer)
})

const handleEdit = () => {
  const { showEdit } = useSideCardEditor()
  showEdit({
    card_id: props.cardId,
    name: props.name,
    tags: props.tags,
    description: props.description,
    card_sub_type: 'countdown',
    countdown_mode: props.countdownMode,
    countdown_single_mode: props.countdownSingleMode,
    countdown_single_length_value: props.countdownSingleLengthValue,
    countdown_single_length_unit: props.countdownSingleLengthUnit,
    countdown_repeat_period_value: props.countdownRepeatPeriodValue,
    countdown_repeat_period_unit: props.countdownRepeatPeriodUnit,
    start_time: props.startTime,
    end_time: props.endTime
  } as CountdownCardData)
}

const updateTime = () => {
  now.value = Date.now()
}

</script>

<style lang="scss" scoped>
.countdown-body {
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
  .countdown-body {
    .end-line .end-info {
      text-align: left;
      padding-right: 0;
    }
  }
}
</style>
