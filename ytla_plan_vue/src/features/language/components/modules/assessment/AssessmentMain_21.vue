<template>
  <h1>{{ $t('language.AssessmentMain_21_000') }}</h1>
  <assessment-retake-button @jump-to-step="handleRetake"/>
  <br>
  <div v-if="currentQuestionIndex < 10" class="question-container">
    <h3>{{ $t('language.AssessmentMain_21_001') }}</h3>
    <p>{{ currentQuestion }}</p>
    <div class="options">
      <button
        v-for="(option, index) in currentOptions"
        :key="index"
        @click="handleOptionSelect(index)"
        class="option-btn"
      >
        {{ option }}
      </button>
    </div>
  </div>
</template>
<script setup lang="ts">
import { computed, ref } from 'vue'
import { useLanguageAssessmentStore } from '@/features/language/stores/languageAssessmentStore.ts'
import AssessmentRetakeButton from '@/features/language/components/ui/assessment/AssessmentRetakeButton.vue'
import { useModuleProcessStore } from '@/core/modules/stores/moduleProcessStore.ts'

// 定义事件发射器（保持原有逻辑）
const emit = defineEmits(['nextStep', 'jumpToStep'])
const handleRetake = (index: number) => emit('jumpToStep', index)

// 获取store数据
const assessmentStore = useLanguageAssessmentStore()
const moduleProcessStore = useModuleProcessStore()
const planId = moduleProcessStore.belongPlanId as number
const moduleId = moduleProcessStore.moduleId as number

// 当前问题索引（0-9）
const currentQuestionIndex = ref(0)

const currentQuestion = computed(() => {
  const questionItem = assessmentStore.step2Questions[currentQuestionIndex.value]
  // 对象的键即为问题描述（假设每个对象只有一个键）
  return questionItem ? Object.keys(questionItem)[0] : ''
})

const currentOptions = computed(() => {
  const questionItem = assessmentStore.step2Questions[currentQuestionIndex.value]
  // 对象的值即为选项数组（假设每个对象只有一个值）
  return questionItem ? Object.values(questionItem)[0] : []
})


// 处理选项选择
const handleOptionSelect = async (answerIndex: number) => {
  // 保存答案到store
  assessmentStore.step2Answers.push(answerIndex)

  // 检查是否完成所有问题
  if (currentQuestionIndex.value < 9) {
    currentQuestionIndex.value++
  } else {
    // 完成所有问题后调用最终评估
    await assessmentStore.assessmentFinal(planId, moduleId, assessmentStore.step2Answers)
    assessmentStore.step2Answers = []
    // 触发下一步（跳转到结果页）
    if (!assessmentStore.step2NotFinished) {
      currentQuestionIndex.value = 0
      emit('nextStep')
    } else {
      currentQuestionIndex.value = 0
    }
  }
}
</script>

<style scoped lang="scss">
.question-container {
  margin: 20px 0;

  h3 {
    margin-bottom: 15px;
  }

  .options {
    display: grid;
    gap: 10px;
    margin-top: 15px;

    .option-btn {
      padding: 8px 12px;
      background: #f0f0f0;
      border: 1px solid #ddd;
      border-radius: 4px;
      cursor: pointer;
      transition: background 0.3s;

      &:hover {
        background: #e0e0e0;
      }
    }
  }
}
</style>
