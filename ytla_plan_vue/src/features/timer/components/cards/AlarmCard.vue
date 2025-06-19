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
    <!-- 主内容区 -->
    <template #card-content>
      <div class="alarm-body">
        <div class="time-display">
          <span class="hours">{{ formattedTime.hours }}</span>
          <span class="separator">:</span>
          <span class="minutes">{{ formattedTime.minutes }}</span>
        </div>
        <div class="current-time">
          {{ currentTime }}
        </div>
        <div class="repeat-days">
          <span
            v-for="day in formattedDays"
            :key="day"
            class="day-tag"
          >
            {{ day }}
          </span>
        </div>
      </div>
    </template>

    <!-- 展开内容区 -->
    <template #secondary-content>
      <div class="detail-panel">
        <div class="detail-item">
          <label>创建日期：</label>
          <span>{{ formattedDateRange }}</span>
        </div>
      </div>
    </template>

    <!-- left-actions-buttons 插槽按钮 -->
    <template #left-actions-buttons>
      <button
        v-if="isAlarmTimeReached && !isButtonClicked"
        class="alarm-confirm-button"
        @click="handleButtonClick"
        title="点一下"
      >
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
          <path
            d="M12 22c1.1 0 2-.9 2-2h-4a2 2 0 0 0 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z" />
        </svg>
      </button>
    </template>
  </SideCard>
</template>

<script setup lang="ts">
import { computed, ref, onMounted, onBeforeUnmount, watch } from 'vue'
import { useSideCardEditor } from '@/core/cards/composables/useSideCardEditor.ts'
import SideCard from '@/core/cards/components/SideCard.vue'
import type { AlarmCardData } from '@/features/timer/types/timerCardTypes'

// 提示音
const alarmSound = new Audio('/resource/feature/alarmCard/祖堅正慶 - 無限停止 ～機工城アレキサンダー：天動編～.mp3')

const props = defineProps({
  // 通用props
  cardId: Number,
  name: String,
  tags: String,
  description: String,
  iconPath: String,
  background: String,

  // 专用props
  alarmTime: String,
  alarmDays: {
    type: Array as () => number[],
    default: () => []
  },
  startTime: String
})

const handleEdit = () => {
  const { showEdit } = useSideCardEditor()
  showEdit({
    card_id: props.cardId,
    name: props.name,
    tags: props.tags,
    description: props.description,
    card_sub_type: 'alarm',
    icon_path: props.iconPath,
    background_path: props.background,
    alarm_time: props.alarmTime,
    alarm_days: props.alarmDays,
    start_time: props.startTime
  } as AlarmCardData)
}

// 实时时钟
const currentTime = ref('--:--:--')
let timer: number

const updateClock = () => {
  const now = new Date()
  currentTime.value = now.toLocaleTimeString('zh-CN', {
    hour12: false,
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  })
}

onMounted(() => {
  updateClock()
  timer = window.setInterval(updateClock, 1000)
})

onBeforeUnmount(() => {
  clearInterval(timer)
})

const formattedTime = computed(() => {
  if (!props.alarmTime) return { hours: '--', minutes: '--' }
  const [hours, minutes] = props.alarmTime.split(':')
  return {
    hours: hours.padStart(2, '0'),
    minutes: minutes.padStart(2, '0')
  }
})

const formattedDays = computed(() => {
  const daysMap = ['日', '一', '二', '三', '四', '五', '六']
  return props.alarmDays
    .sort((a, b) => a - b)
    .map(d => `${daysMap[d]}`)
})

const formattedDateRange = computed(() => {
  if (!props.startTime) return '长期有效'
  try {
    const startDate = new Date(props.startTime)
    return startDate.toLocaleDateString('zh-CN', {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit'
    })
  } catch {
    return '日期格式错误'
  }
})

// 标记闹钟时间是否已到
const isAlarmTimeReached = ref(false)
// 标记提示音是否已播放
const isSoundPlayed = ref(false)
// 标记当前分钟内闹钟是否已经触发过
const isAlarmTriggeredThisMinute = ref(false)
// 标记按钮是否被点击
const isButtonClicked = ref(false)

watch(currentTime, () => {
  const now = new Date()
  const currentDay = now.getDay()
  const currentHourMinute = currentTime.value.slice(0, 5)
  if (currentHourMinute === `${formattedTime.value.hours}:${formattedTime.value.minutes}` && props.alarmDays.includes(currentDay)) {
    if (!isAlarmTriggeredThisMinute.value) {
      isAlarmTimeReached.value = true
      if (!isSoundPlayed.value) {
        alarmSound.play()
        isSoundPlayed.value = true
      }
      isAlarmTriggeredThisMinute.value = true
      isButtonClicked.value = false
    }
  } else {
    isAlarmTimeReached.value = false
    isSoundPlayed.value = false
    isAlarmTriggeredThisMinute.value = false
    isButtonClicked.value = false
  }
})

const handleButtonClick = () => {
  isAlarmTimeReached.value = false
  isButtonClicked.value = true
  alarmSound.pause()
  alarmSound.currentTime = 0
}
</script>

<style lang="scss" scoped>
/* 保持原有样式不变 */
.alarm-body {
  text-align: center;

  .time-display {
    font-size: 2rem;
    font-family: Arial;

    .separator {
      margin: 0 0.25rem;
      color: #666;
    }
  }

  .current-time {
    font-size: 1.2rem;
    font-family: Arial;
    color: #666;
  }

  .repeat-days {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    justify-content: center;
    margin-top: 0.5rem;

    .day-tag {
      background: #f0f9eb;
      color: #67c23a;
      padding: 0.2rem 0.2rem;
      border-radius: 0.5rem;
      font-size: 0.9em;
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
  .time-display {
    font-size: 1.6rem;
  }

  .current-time {
    font-size: 1rem;
  }

  .day-tag {
    font-size: 0.8em;
  }
}

.alarm-confirm-button {
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
  color: yellowgreen;
  transition: color 0.3s ease;

  &:hover {
    color: grey;
  }

  svg {
    fill: currentColor;
  }
}
</style>
