<template>
  <div class="vocabulary-detail">
    <!-- 返回按钮 -->
    <button class="back-btn" @click="handleBack">
      ← {{ $t('language.modules.vocabulary.return_button_001') }}
    </button>

    <!-- 单词列表 -->
    <div v-if="currentBook" class="word-list">
      <div v-for="(word, index) in currentBook.word_list" :key="index" class="word-item">
        {{ word }}
      </div>
    </div>

    <!-- 空状态 -->
    <div v-else class="empty-state">
      <p>{{ $t('language.modules.vocabulary.main_01_001') }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useLanguageVocabularyStore } from '@/features/language/modules/vocabulary/stores/languageVocabularyStore.ts'
import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'

const vocabularyStore = useLanguageVocabularyStore()
const moduleProcessStore = useModuleProcessStore()

// 获取当前词汇本
const currentBook = computed(() => {
  return vocabularyStore.vocabularyBooks.find(
    b => b.record_id === vocabularyStore.currentBookId
  )
})
const emit = defineEmits(['nextStep', 'prevStep'])
// 返回主列表
const handleBack = () => {
  moduleProcessStore.clearEditingModule()
  emit('prevStep')
}
</script>

<style scoped lang="scss">
.vocabulary-detail {
  max-width: 800px;
  padding: 20px;

  .back-btn {
    margin-bottom: 20px;
    padding: 8px 16px;
    background: #f5f5f5;
    border: 1px solid #ddd;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s;

    &:hover {
      background: #e0e0e0;
    }
  }

  .word-list {
    display: grid;
    gap: 12px;

    .word-item {
      padding: 12px;
      border: 1px solid #e0e0e0;
      border-radius: 4px;
      background: white;
    }
  }

  .empty-state {
    text-align: center;
    color: #757575;
    padding: 40px 0;
  }
}
</style>
