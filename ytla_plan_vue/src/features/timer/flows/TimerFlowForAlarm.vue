<template>
  <SideCardEditorFlowNavigator
    :is-editing="isEditMode"
    :show-prev="showPrev"
    :submit-disabled="!canSubmit"
    @cancel="handleCancel"
    @prev="handlePrev"
    @submit="handleSubmit"
  >
    <div class="alarm-config-container">
      <!-- 时间设置区域 -->
      <section class="time-section">
        <div class="time-input-group">
          <input
            v-model="alarmTime"
            type="time"
            class="time-picker"
            required
            @change="validateTime"
          >
          <span class="time-hint">24小时制</span>
        </div>
      </section>

      <!-- 周期选择区域 -->
      <section class="repeat-section">
        <h3 class="section-title">重复周期</h3>
        <div class="day-selector">
          <div class="quick-select-buttons">
            <button @click="selectAllDays" class="quick-btn">全选</button>
            <button @click="selectWorkDays" class="quick-btn">工作日</button>
            <button @click="selectWeekendDays" class="quick-btn">周末</button>
          </div>

          <div class="day-grid">
            <div
              v-for="day in days"
              :key="day.value"
              class="day-item"
              :class="{ 'active': selectedDays.includes(day.value) }"
            >
              <input
                type="checkbox"
                v-model="selectedDays"
                :value="day.value"
                :id="'day'+day.value"
                hidden
              >
              <label :for="'day'+day.value" class="day-label">
                {{ day.label }}
              </label>
            </div>
          </div>
        </div>
      </section>

      <section class="time-section">
        <h3 class="section-title">开始时间</h3>
        <div class="input-wrapper">
          <input
            v-model="startTime"
            type="datetime-local"
          >
          <button type="button" @click="resetStartTime">清空</button>
        </div>
      </section>
    </div>
  </SideCardEditorFlowNavigator>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import SideCardEditorFlowNavigator from '@/core/cards/layouts/SideCardEditorFlowNavigator.vue'
import { formatDateTime, formatDateTimeNoSecs, currentDateTime } from '@/core/frame/utils/timeUtils.ts'
import type { AlarmCardData, TimerCardSubType } from '@/features/timer/types/timerCardTypes'

const props = defineProps<{
  mode: 'create' | 'edit'
  initialData?: AlarmCardData
  cardSubType: TimerCardSubType
}>()

const emit = defineEmits<{
  (e: 'submit', payload: AlarmCardData | Omit<AlarmCardData, 'card_id'>): void
  (e: 'cancel'): void
  (e: 'prev'): void
}>()

const alarmTime = ref('')
const startTime = ref('')
const selectedDays = ref<string[]>(['1', '2', '3', '4', '5']) // 默认工作日
const days = [
  { value: '0', label: '日' },
  { value: '1', label: '一' },
  { value: '2', label: '二' },
  { value: '3', label: '三' },
  { value: '4', label: '四' },
  { value: '5', label: '五' },
  { value: '6', label: '六' }
]

const initializeEditData = () => {
  if (props.mode === 'edit' && props.initialData) {
    alarmTime.value = props.initialData.alarm_time || ''
    selectedDays.value = props.initialData.alarm_days?.map(String) || []
    startTime.value = formatDateTimeNoSecs(props.initialData.start_time) || ''
  }
}

const buildPayload = () => ({
  alarm_time: alarmTime.value,
  alarm_days: selectedDays.value.map(Number),
  start_time: startTime.value ? formatDateTime(startTime.value) : currentDateTime(),
  ...(props.mode === 'create' ? {
    name: `新的${props.cardSubType}`,
    tags: '',
    description: ''
  } : {})
})

const validateTime = () => {
  if (!alarmTime.value) {
    return false
  }
  return true
}

const canSubmit = computed(() => validateTime())

const handleSubmit = () => {
  if (!canSubmit.value) return

  const basePayload = buildPayload()
  const fullPayload = props.mode === 'edit'
    ? { ...props.initialData, ...basePayload }
    : { ...basePayload, card_sub_type: props.cardSubType }

  emit('submit', fullPayload as AlarmCardData)
}

const handleCancel = () => emit('cancel')
const handlePrev = () => emit('prev')

const selectAllDays = () => {
  selectedDays.value = ['0', '1', '2', '3', '4', '5', '6']
}
const selectWorkDays = () => {
  selectedDays.value = ['1', '2', '3', '4', '5']
}
const selectWeekendDays = () => {
  selectedDays.value = ['0', '6']
}
const resetStartTime = () => {
  startTime.value = ''
}

// 计算属性
const isEditMode = computed(() => props.mode === 'edit')
const showPrev = computed(() => !isEditMode.value)

// 生命周期
onMounted(initializeEditData)
</script>

<style scoped>
.alarm-config-container {
  padding: 1rem;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.section-title {
  margin: 0 0 1rem 0;
  font-size: 1.1em;
  color: #2c3e50;
  font-weight: 600;
}

.time-section {
  .time-input-group {
    display: flex;
    align-items: center;
    gap: 1rem;

    .time-picker {
      padding: 0.8rem;
      font-size: 1.2em;
      border: 2px solid #42b983;
      border-radius: 8px;
      width: 140px;
    }

    .time-hint {
      color: #7f8c8d;
      font-size: 0.9em;
    }
  }
}

.repeat-section {
  flex: 1;

  .quick-select-buttons {
    display: flex;
    gap: 0.8rem;
    margin-bottom: 1rem;

    .quick-btn {
      padding: 0.5rem 1rem;
      background: #42b983;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.3s;

      &:hover {
        background: #3aa876;
      }
    }
  }

  .day-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(60px, 1fr));
    gap: 0.8rem;
  }

  .day-item {
    position: relative;
    border-radius: 8px;
    transition: all 0.3s;

    &.active {
      background: #42b983;

      .day-label {
        color: white;
      }
    }

    .day-label {
      display: block;
      width: 100%;
      padding: 0.8rem;
      text-align: center;
      cursor: pointer;
      border-radius: inherit;
      border: 1px solid #ddd;
      transition: inherit;
    }

    &:hover:not(.active) {
      background: #f8f9fa;
    }
  }
}
</style>
