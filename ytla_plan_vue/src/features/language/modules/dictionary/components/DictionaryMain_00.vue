<template>
  <div class="dictionary-container">
    <!-- 搜索区域 -->
    <div class="search-section">
      <input
        type="text"
        v-model="localWord"
        placeholder="..."
        @keyup.enter="search"
      >
      <button @click="search">→</button>
    </div>

    <!-- 搜索结果 -->
    <div v-if="meaning" class="result-section" v-html="meaning"></div>
  </div>
</template>

<script setup lang="ts">
import { useLanguageDictionaryStore } from '@/features/language/modules/dictionary/stores/languageDictionaryStore.ts'
import { nextTick, ref, watch } from 'vue'

const dictionaryStore = useLanguageDictionaryStore()
const { searchDictionary } = dictionaryStore

const localWord = ref('')
const meaning = ref('')

const search = async () => {
  if (localWord.value.trim()) {
     meaning.value = ''
    await searchDictionary(localWord.value.trim())
    await nextTick()
    meaning.value = dictionaryStore.searchResult
  }
}
watch(() => dictionaryStore.searchResult, (newVal) => {
  meaning.value = newVal
}, { immediate: true, deep: true })

</script>

<style scoped lang="scss">

.dictionary-container {
  max-width: 800px;
  padding: 20px;

  .search-section {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;

    input {
      flex: 1;
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }

    button {
      padding: 8px 16px;
      background: #2e7d32;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;

      &:hover {
        background: #225e26;
      }
    }
  }
}

:deep(.entry) {

  // 确保基础样式应用
  font-family: inherit;
  line-height: 1.6;

  /* 以下样式需要与MDX原始结构匹配 */
  .h-g {
    display: block;
    line-height: 1.6;
    margin: 1em 0;
  }

  .sense-g {
    display: block;
    line-height: 1.6;
    margin: 1em 0;
  }


  /* 主词条标题 */
  .h {
    display: block;
    font-size: 1.8em;
    font-weight: 600;
    color: #212121; /* 深黑色 */
    margin-right: 0.3em;
  }

  .id {
    display: block;
    font-size: 1.8em;
    font-weight: 600;
    color: #212121; /* 深黑色 */
    margin-right: 0.3em;
  }


  .top-g {
    display: block;
    line-height: 1.6;
    margin: 1em 0;
  }


  .def-g {
    display: block;
    line-height: 1.6;
    margin: 1em 0;
  }

  .label-g {
    font-size: 0.85em;
    color: #888;
    margin-right: 0.5em;
  }

  .infml {
    color: #d32f2f;
    font-style: italic;
    background: #fce4ec;
    padding: 0.2em 0.4em;
    border-radius: 3px;
  }

  .d {
    display: block;
    color: #333;
    font-weight: 500;
    margin: 0.5em 0;

    &:not(:last-child) {
      margin-bottom: 1em;
    }
  }

  .x-g {
    display: block;
    border-left: 3px solid #e0e0e0;
    padding-left: 1em;
    margin: 1em 0;
  }

  .x {
    display: block;
    font-style: italic;
    color: #2e7d32;
  }

  .tx {
    display: block;
    color: #757575;
    margin-top: 0.5em;
  }


  /* 核心符号（★） */
  .symbols-coresym {
    color: #ff9800; /* 橙色突出 */
    margin-right: 0.3em;
  }

  .symbols-small_coresym {
    color: #ff9800;
    font-size: 0.8em;
    margin-right: 0.2em;
  }

  /* 例句符号（◆） */
  .symbols-xsym {
    color: #64b5f6; /* 蓝色区分 */
    margin-right: 0.5em;
  }

  /* 参见符号（☞） */
  .symbols-xrsym {
    color: #78909c; /* 灰蓝色 */
    margin-right: 0.3em;
  }

  /* 段落方块符号（■） */
  .symbols-para_square {
    color: #4caf50; /* 绿色 */
    margin-right: 0.5em;
  }

  /* 词性标注（exclamation/noun等） */
  .pos {
    font-style: italic;
    color: #546e7a;
    font-size: 0.9em;
    margin: 0 0.2em;
  }

  /* 中文翻译 */
  .chn {
    color: #424242;
    font-size: 0.95em;
    margin-top: 0.3em;
  }

  /* 非正式表达（如Hi） */
  .unfm {
    color: #d32f2f;
    font-weight: 500;
  }

  /* 说明性文字（如less formal） */
  .unei {
    color: #757575;
    font-size: 0.9em;
    font-style: italic;
  }

  /* 词形变化（如复数） */
  .inflection {
    color: #616161;
    margin: 0 0.2em;
  }

  /* 分隔符类（如音标分隔符、括号等） */
  .z {
    display: inline;
    color: #757575; /* 与现有灰色系统一 */
  }

  .z_ei-g {
    display: inline;
    color: #757575;
    font-family: monospace; /* 等宽字体更符合音标分隔符的视觉 */
  }

  /* 音标类（英音/美音） */
  .phon-gb, .phon-us {
    font-family: monospace; /* 等宽字体更符合音标排版 */
    color: #616161; /* 深灰色，比正文稍浅 */
    font-size: 0.9em; /* 略小于正文 */
  }

  /* 标签文本（如 "especially in BrE"） */
  .g {
    font-size: 0.85em; /* 与 .label-g 统一 */
    color: #888; /* 与 .label-g 统一 */
  }

  /* 定义内容主体（如 "used as a greeting..."） */
  .ud {
    line-height: 1.6; /* 与 .def-g 行高统一 */
    color: #333; /* 与 .d 颜色统一 */
  }

  /* 非定义词汇（可点击的扩展词汇） */
  .ndv {
    font-style: italic;
    color: #2e7d32; /* 与例句英文颜色统一 */
    cursor: pointer; /* 提示可点击 */

    &:hover {
      text-decoration: underline; /* 交互反馈 */
    }
  }

  /* 解释性词汇（如 "(= said hello to each other)"） */
  .gl {
    font-style: italic;
    color: #757575; /* 与 .tx 颜色统一 */
    font-size: 0.9em; /* 略小 */
  }

  /* 重点符号（如 *） */
  .ast {
    color: #d32f2f; /* 与 .infml 红色统一 */
    font-weight: bold; /* 突出显示 */
    margin: 0 0.1em; /* 轻微间距 */
  }

  /* 参见链接文本（如 "see also" 后的内容） */
  .xh {
    color: #2196F3; /* 品牌色（参考 .language-manage-btn 蓝色） */
    cursor: pointer; /* 提示可点击 */

    &:hover {
      text-decoration: underline; /* 交互反馈 */
    }
  }


}
</style>
