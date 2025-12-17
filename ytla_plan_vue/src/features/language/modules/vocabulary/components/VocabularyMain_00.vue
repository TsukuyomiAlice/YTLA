<template>
  <h1>{{ $t('language.VocabularyMain_00_000') }}</h1>
  <div class="vocabulary-container">
    <!-- 创建区域 -->
    <div class="create-section">
      <button class="create-btn" @click="createNewBook">
        + {{ $t('language.VocabularyAddButton_001') }}
      </button>
    </div>

    <!-- 词汇本列表 -->
    <div v-if="vocabularyBooks.length" class="book-list">
      <div v-for="book in vocabularyBooks" :key="book.record_id" class="book-item">
        <div class="book-header">
          <h3>{{ book.vocabulary_book_name || $t('language.VocabularyMain_00_001') }}</h3>
          <span class="word-count">{{ book.word_list.length }} words</span>
        </div>
        <div class="book-actions">
          <button @click="openBook(book.record_id)">{{ $t('language.VocabularyOpenButton_001') }}</button>
        </div>
      </div>
    </div>

    <!-- 空状态 -->
    <div v-else class="empty-state">
      <p>{{ $t('language.VocabularyMain_00_002') }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onActivated, onMounted } from 'vue'
import { useLanguageVocabularyStore } from '@/features/language/modules/vocabulary/stores/languageVocabularyStore.ts'
import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'

const vocabularyStore = useLanguageVocabularyStore()
const moduleProcessStore = useModuleProcessStore()

// 从store直接获取上下文参数
const planId = moduleProcessStore.belongPlanId as number
const moduleId = moduleProcessStore.moduleId as number
const userName = 'Ann'


// 加载词汇本列表（提取为独立方法）
const loadBooks = async () => {
  try {
    await vocabularyStore.fetchAllBooks(planId, moduleId, userName)
  } catch (error) {
    console.error('加载词汇本失败:', error)
  }
}

// 组件挂载和激活时都刷新数据
onMounted(loadBooks)
onActivated(loadBooks)

// 使用计算属性获取实时状态
const vocabularyBooks = computed(() => vocabularyStore.vocabularyBooks)


// 创建新词汇本
const createNewBook = async () => {
  try {
    await vocabularyStore.createNewBook(planId, moduleId, userName)
    await vocabularyStore.fetchAllBooks(planId, moduleId, userName)
  } catch (error) {
    console.error('创建失败:', error)
  }
}
const emit = defineEmits(['nextStep', 'prevStep'])
// 打开词汇本
const openBook = (recordId: number) => {
  vocabularyStore.setCurrentBook(recordId)
  emit('nextStep')
}
</script>

<style scoped lang="scss">
.vocabulary-container {
  max-width: 800px;
  padding: 20px;

  .create-section {
    margin-bottom: 30px;

    .create-btn {
      padding: 12px 24px;
      background: #2e7d32;
      color: white;
      border: none;
      border-radius: 25px;
      cursor: pointer;
      transition: background 0.3s;

      &:hover {
        background: #225e26;
      }
    }
  }

  .book-list {
    display: grid;
    gap: 20px;

    .book-item {
      padding: 20px;
      border: 1px solid #e0e0e0;
      border-radius: 8px;

      .book-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;

        h3 {
          margin: 0;
          font-size: 1.2em;
        }

        .word-count {
          color: #757575;
          font-size: 0.9em;
        }
      }

      .book-actions {
        display: flex;
        gap: 10px;

        button {
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
      }
    }
  }

  .empty-state {
    text-align: center;
    color: #757575;
    padding: 40px 0;
  }
}
</style>
