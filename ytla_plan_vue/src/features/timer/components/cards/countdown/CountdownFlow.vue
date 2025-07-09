<template>
  <EditorFlowNavigator
    :is-editing="isEditMode"
    :show-prev="showPrev"
    :submit-disabled="!canSubmit"
    @cancel="handleCancel"
    @prev="handlePrev"
    @submit="handleSubmit"
  >
    <div class="countdown-config-container">
      <!-- 倒计时模式选择 -->
      <section class="mode-section">
        <div class="mode-select">
          <label v-for="mode in countdownModes" :key="mode.value">
            <input
              type="radio"
              v-model="countdownData.mode"
              :value="mode.value"
              :disabled="isSubmitting"
            >
            {{ mode.label }}
          </label>
        </div>
      </section>

      <!-- 单次模式配置 -->
      <template v-if="countdownData.mode === 'single'">
        <section class="submode-section">
          <div class="radio-group">
            <label v-for="smode in countdownSingleModes" :key="smode.value">
              <input
                type="radio"
                v-model="countdownData.single.mode"
                :value="smode.value"
                :disabled="isSubmitting"
              >
              {{ smode.label }}
            </label>
          </div>

          <div v-if="countdownData.single.mode === 'countdown-until-specific-time'"
               class="input-wrapper">
            <label>到期时间</label>
            <input
              v-model="countdownData.single.end_time"
              type="datetime-local"
              :disabled="isSubmitting"
            >
            <button
              type="button"
              @click="countdownData.single.end_time = ''"
              :disabled="isSubmitting"
            >
              清空
            </button>
          </div>

          <div v-if="countdownData.single.mode === 'countdown-time-limit'">
            <div class="radio-group">
              <label>时间单位</label>
              <label v-for="unit in timeUnits" :key="unit.value">
                <input
                  type="radio"
                  v-model="countdownData.single.unit"
                  :value="unit.value"
                  :disabled="isSubmitting"
                >
                {{ unit.label }}
              </label>
            </div>
            <div class="form-group">
              <label>时长</label>
              <input
                v-model.number="countdownData.single.value"
                type="number"
                min="1"
                :disabled="isSubmitting"
              >
            </div>
          </div>
        </section>
      </template>

      <!-- 重复模式配置 -->
      <template v-if="countdownData.mode === 'repeat'">
        <section class="submode-section">
          <div class="radio-group">
            <label>周期单位</label>
            <label v-for="unit in timeUnits" :key="unit.value">
              <input
                type="radio"
                v-model="countdownData.repeat.unit"
                :value="unit.value"
                :disabled="isSubmitting"
              >
              {{ unit.label }}
            </label>
          </div>
          <div class="form-group">
            <label>周期值</label>
            <input
              v-model.number="countdownData.repeat.value"
              type="number"
              min="1"
              :disabled="isSubmitting"
            >
          </div>
          <div class="input-wrapper">
            <label>下一个到期时间</label>
            <input
              v-model="countdownData.repeat.end_time"
              type="datetime-local"
              :disabled="isSubmitting"
            >
            <button
              type="button"
              @click="countdownData.repeat.end_time = ''"
              :disabled="isSubmitting"
            >
              清空
            </button>
          </div>
        </section>
      </template>

      <section class="time-section">
        <h3 class="section-title">开始时间</h3>
        <div class="input-wrapper">
          <input
            v-model="startTime"
            type="datetime-local"
            :disabled="isSubmitting"
          >
          <button
            type="button"
            @click="startTime = ''"
            :disabled="isSubmitting"
          >
            清空
          </button>
        </div>
      </section>
    </div>
  </EditorFlowNavigator>
</template>

<script setup lang="ts">
import { ref, reactive, computed, onMounted } from 'vue'
import EditorFlowNavigator from '@/core/sideCards/layouts/SideCardEditorFlowNavigator.vue'
import { formatDateTime, formatDateTimeNoSecs, currentDateTime } from '@/core/frame/utils/timeUtils.ts'
import type { CountdownCardData, TimerCardSubType } from '@/features/timer/types/timerCardTypes.ts'

const props = defineProps<{
  mode: 'create' | 'edit'
  initialData?: CountdownCardData
  cardSubType: TimerCardSubType
}>()

const emit = defineEmits<{
  (e: 'submit', payload: CountdownCardData | Omit<CountdownCardData, 'card_id'>): void
  (e: 'cancel'): void
  (e: 'prev'): void
}>()

// 状态管理
const isSubmitting = ref(false)
const startTime = ref('')

// 配置选项
const countdownModes = [
  { value: 'single', label: '单次' },
  { value: 'repeat', label: '重复' }
]

const countdownSingleModes = [
  { value: 'countdown-until-specific-time', label: '到指定时间' },
  { value: 'countdown-time-limit', label: '指定时长' }
]

const timeUnits = [
  { value: 'minute', label: '分钟' },
  { value: 'hour', label: '小时' },
  { value: 'day', label: '天' }
]

// 核心数据模型
const countdownData = reactive({
  mode: 'single',
  single: {
    mode: 'countdown-until-specific-time',
    end_time: '',
    unit: 'minute',
    value: 15
  },
  repeat: {
    unit: 'minute',
    value: 15,
    end_time: ''
  }
})

// 计算属性
const isEditMode = computed(() => props.mode === 'edit')
const showPrev = computed(() => !isEditMode.value)
const canSubmit = computed(() => {
  if (countdownData.mode === 'single') {
    return countdownData.single.mode !== 'countdown-until-specific-time' ||
           !!countdownData.single.end_time
  }
  return true
})

// 初始化数据
const initializeData = () => {
  if (!isEditMode.value || !props.initialData) return

  const data = props.initialData
  startTime.value = formatDateTimeNoSecs(data.start_time) || ''

  countdownData.mode = data.countdown_mode || 'single'

  if (data.countdown_mode === 'single') {
    countdownData.single = {
      mode: data.countdown_single_mode || 'countdown-until-specific-time',
      end_time: formatDateTimeNoSecs(data.end_time) || '',
      unit: data.countdown_single_length_unit || 'minute',
      value: data.countdown_single_length_value || 15
    }
  } else {
    countdownData.repeat = {
      unit: data.countdown_repeat_period_unit || 'minute',
      value: data.countdown_repeat_period_value || 15,
      end_time: formatDateTimeNoSecs(data.end_time) || ''
    }
  }
}

// 事件处理
const handleCancel = () => emit('cancel')
const handlePrev = () => emit('prev')

const handleSubmit = () => {
  if (isSubmitting.value || !canSubmit.value) return

  isSubmitting.value = true
  try {
    const payload = buildPayload()
    emit('submit', payload as CountdownCardData)
  } finally {
    isSubmitting.value = false
  }
}

// 数据构建
const buildPayload = () => {
  const baseData = {
    card_sub_type: props.cardSubType,
    countdown_mode: countdownData.mode,
    start_time: startTime.value ? formatDateTime(startTime.value) : currentDateTime(),
    ...(countdownData.mode === 'single' ? {
      countdown_single_mode: countdownData.single.mode,
      ...(countdownData.single.mode === 'countdown-until-specific-time' ? {
        end_time: formatDateTime(countdownData.single.end_time)
      } : {
        countdown_single_length_unit: countdownData.single.unit,
        countdown_single_length_value: countdownData.single.value
      })
    } : {
      countdown_repeat_period_unit: countdownData.repeat.unit,
      countdown_repeat_period_value: countdownData.repeat.value,
      end_time: formatDateTime(countdownData.single.end_time)
    })
  }

  return isEditMode.value ? {
    ...props.initialData,
    ...baseData
  } : {
    ...baseData,
    name: `新的倒计时`,
    tags: '',
    description: '',
    icon_path: '',
    background_path: ''
  }
}

// 生命周期
onMounted(initializeData)
</script>

<style scoped>
/* 保持原有样式不变 */
.countdown-config-container {
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
}

.mode-select label, .radio-group label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.input-wrapper {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.input-wrapper button {
  padding: 0.3rem 0.6rem;
  background: #e74c3c;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group input {
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  width: 200px;
}
</style>
