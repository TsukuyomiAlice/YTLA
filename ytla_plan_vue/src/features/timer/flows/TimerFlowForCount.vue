<template>
  <EditorFlowNavigator
    :is-editing="isEditMode"
    :show-prev="showPrev"
    :submit-disabled="!canSubmit"
    @cancel="handleCancel"
    @prev="handlePrev"
    @submit="handleSubmit"
  >
    <div class="count-config-container">
      <!-- 计时模式选择 -->
      <section class="mode-section">
        <div class="mode-select">
          <label v-for="mode in countModes" :key="mode.value">
            <input
              type="radio"
              v-model="countData.mode"
              :value="mode.value"
            >
            {{ mode.label }}
          </label>
        </div>
      </section>

      <!-- 到指定时间后停止 -->
      <div v-if="countData.mode === 'count-until-specific-time'" class="input-wrapper">
        <label>到期时间</label>
        <input
          v-model="countData.end_time"
          type="datetime-local"
          placeholder="不指定时间默认15分钟后"
        >
        <button type="button" @click="countData.end_time = ''">清空</button>
      </div>

      <!-- 经过指定时长后停止 -->
      <div v-if="countData.mode === 'count-until-time-across'">
        <div class="radio-group">
          <label>周期单位</label>
          <label v-for="unit in timeUnits" :key="unit.value">
            <input
              type="radio"
              v-model="countData.duration.unit"
              :value="unit.value"
            >
            {{ unit.label }}
          </label>
        </div>
        <div class="form-group">
          <label>周期值</label>
          <input
            v-model="countData.duration.value"
            type="number"
            min="1"
            value="15"
          >
        </div>
      </div>

      <section class="time-section">
        <h3 class="section-title">开始时间</h3>
        <div class="input-wrapper">
          <input
            v-model="startTime"
            type="datetime-local"
          >
          <button type="button" @click="startTime = ''">清空</button>
        </div>
      </section>
    </div>
  </EditorFlowNavigator>
</template>

<script setup lang="ts">
import { ref, reactive, computed, onMounted } from 'vue'
import EditorFlowNavigator from '@/core/cards/layouts/SideCardEditorFlowNavigator.vue'
import type { CountCardData, TimerCardSubType } from '@/features/timer/types/timerCardTypes'
import { formatDateTime, formatDateTimeNoSecs, currentDateTime } from '@/core/frame/utils/timeUtils.ts'

const props = defineProps<{
  mode: 'create' | 'edit'
  initialData?: CountCardData
  cardSubType: TimerCardSubType
}>()

const emit = defineEmits<{
  (e: 'cancel'): void
  (e: 'prev'): void
  (e: 'submit', payload: CountCardData | Omit<CountCardData, 'card_id'>): void
}>()

// 计时模式选项
const countModes = [
  { value: 'count-nonstop', label: '不停止计时' },
  { value: 'count-until-specific-time', label: '到指定时间后停止' },
  { value: 'count-until-time-across', label: '经过指定时长后停止' }
]

// 时间单位选项
const timeUnits = [
  { value: 'minute', label: '分钟' },
  { value: 'hour', label: '小时' },
  { value: 'day', label: '天' }
]

// 数据模型
const startTime = ref('')
const countData = reactive({
  mode: 'count-nonstop',
  end_time: '',
  duration: {
    unit: 'minute',
    value: 15
  }
})

// 初始化编辑数据
const initializeEditData = () => {
  if (props.mode === 'edit' && props.initialData) {
    countData.mode = props.initialData.count_mode
    countData.end_time = props.initialData.end_time || ''
    countData.duration = {
      unit: props.initialData.count_single_length_unit || 'minute',
      value: props.initialData.count_single_length_value || 15
    }
    startTime.value = formatDateTimeNoSecs(props.initialData.start_time) || ''
  }
}

onMounted(initializeEditData)

// 计算属性
const isEditMode = computed(() => props.mode === 'edit')
const showPrev = computed(() => !isEditMode.value)
const canSubmit = computed(() => {
  return countData.mode !== 'count-until-specific-time' ||
         (countData.mode === 'count-until-specific-time' && countData.end_time)
})

// 事件处理
const handleCancel = () => emit('cancel')
const handlePrev = () => emit('prev')

const handleSubmit = () => {
  const basePayload = {
    card_sub_type: props.cardSubType,
    count_mode: countData.mode,
    start_time: startTime.value ? formatDateTime(startTime.value) : currentDateTime(),
    ...(countData.mode === 'count-until-specific-time' && {
      end_time: formatDateTime(countData.end_time)
    }),
    ...(countData.mode === 'count-until-time-across' && {
      count_single_length_unit: countData.duration.unit,
      count_single_length_value: countData.duration.value
    })
  }

  const fullPayload = isEditMode.value
    ? { ...props.initialData, ...basePayload }
    : {
        ...basePayload,
        name: `新的计时`,
        tags: '',
        description: '',
        icon_path: '',
        background_path: ''
      }

  emit('submit', fullPayload as CountCardData)
}
</script>

<style scoped>
/* 保持原有样式不变 */
.count-config-container {
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

.mode-select, .radio-group {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;

  label {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
}

.input-wrapper {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;

  button {
    padding: 0.3rem 0.6rem;
    background: #e74c3c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
}

.form-group {
  margin-bottom: 1rem;

  input {
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    width: 200px;
  }
}
</style>
