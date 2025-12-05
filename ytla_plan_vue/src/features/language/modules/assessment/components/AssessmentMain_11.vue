<template>
  <h1>{{ $t('language.AssessmentMain_11_000') }}</h1>
  <assessment-retake-button @jump-to-step="handleRetake"/>
  <br>
  <p>{{ $t('language.AssessmentMain_11_001') }}</p>

  <div class="word-list">
    <div v-for="(word, index) in step1Wordlist" :key="index" class="word-item">
      <input
        type="checkbox"
        :value="word"
        v-model="selectedWords"
      >
      <span @click="toggleWord(word)">{{ word }}</span>
    </div>
  </div>

  <assessment-next-button @next-step="handleNext"/>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useLanguageAssessmentStore } from '@/features/language/modules/assessment/stores/languageAssessmentStore.ts'
import { useModuleProcessStore } from '@/core/modules/_type/stores/moduleProcessStore.ts'

import AssessmentNextButton from '@/features/language/modules/assessment/components/ui/AssessmentNextButton.vue'
import AssessmentRetakeButton from '@/features/language/modules/assessment/components/ui/AssessmentRetakeButton.vue'

// 定义事件发射器
const emit = defineEmits(['nextStep', 'jumpToStep'])
const handleNext = async () => {
  try {
    // 调用assessment1B并传递勾选的单词
    await assessmentStore.assessment1B(planId, moduleId, selectedWords.value)
    // 调用成功后触发下一步事件
    emit('nextStep')
  } catch (error) {
    console.error('下一步操作失败:', error)
  }
}
const handleRetake = (index: number) => {
  emit('jumpToStep', index)
}

// 获取store和模块信息
const assessmentStore = useLanguageAssessmentStore()
const moduleProcessStore = useModuleProcessStore()
const planId = moduleProcessStore.belongPlanId as number
const moduleId = moduleProcessStore.moduleId as number

// 勾选的单词数组
const selectedWords = ref<string[]>([])
const toggleWord = (word: string) => {
  if (selectedWords.value.includes(word)) {
    // 已选中则移除
    selectedWords.value = selectedWords.value.filter(w => w !== word)
  } else {
    // 未选中则添加
    selectedWords.value.push(word)
  }
}
// 获取store中的单词列表
const step1Wordlist = assessmentStore.step1Wordlist

</script>

<style scoped lang="scss">
.word-list {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 每行4个单词 */
  gap: 10px;
  margin: 20px 0;
}

.word-item {
  display: flex;
  align-items: center;
  gap: 8px;
}
</style>
