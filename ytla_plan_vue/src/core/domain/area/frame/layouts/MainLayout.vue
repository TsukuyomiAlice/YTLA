<template>
  <div class="app-container" :class="{ 'right-visible': isRightSideBarVisible, 'swapped': isSideBarSwapped }">
    <!-- 左侧功能侧边栏 -->

    <aside class="sidebar left-sidebar">
      <nav class="left-nav">
        <button class="swap-btn" @click="toggleSwap">
          <span class="swap-icon">⇄</span>
          <span class="swap-text">
            {{ isSideBarSwapped ? $t(`domain.frame.MainLayout_swap_btn_to_left`) : $t(`domain.frame.MainLayout_swap_btn_to_right`) }}
          </span>
        </button>

        <div class="language-floating" @mouseover="hoverLanguage = true"
             @mouseleave="hoverLanguage = false">
          <button class="lang-trigger">
            🌐 {{ currentLanguage }}
          </button>
          <transition name="slide-fade">
            <div v-show="hoverLanguage" class="lang-menu">
              <button @click="switchLanguage('en')">English</button>
              <button @click="switchLanguage('zh')">中文</button>
            </div>
          </transition>
        </div>

        <PanelLayer />

      </nav>
    </aside>

    <!-- 主内容区域 -->
    <main class="main-content">
      <button
        class="toggle-right"
        @click="toggleRightSidebar"
        :style="toggleButtonStyle"
        aria-label="侧边栏开关"
      >
        {{ toggleButtonLabel }}
      </button>

      <ModuleLayer />
    </main>

    <!-- 右侧信息侧边栏 -->
    <aside class="sidebar right-sidebar">
      <SideCardLayer />
    </aside>


  </div>
</template>

<script setup lang="ts">
import PanelLayer from '@/core/domain/area/frame/layouts/PanelLayer.vue'
import SideCardLayer from '@/core/domain/area/cards/layouts/SideCardLayer.vue'
import ModuleLayer from '@/core/domain/area/modules/layouts/ModuleLayer.vue'
import { usePersistence } from '@/core/domain/area/frame/composables/usePersistence.ts'

const { getPersistence, setPersistence } = usePersistence()

import { useLayoutStore } from '@/core/domain/area/frame/services/layoutStore.ts'

const layoutStore = useLayoutStore()

import { storeToRefs } from 'pinia'

const {
  isRightSideBarVisible,
  isSideBarSwapped,
  toggleButtonLabel,
  toggleButtonStyle
} = storeToRefs(layoutStore)

import { computed, onMounted, ref } from 'vue'

onMounted(() => {
  layoutStore.initialize()
})

import { useLayoutMode } from '@/core/domain/area/frame/composables/useLayoutMode.ts'
useLayoutMode()

const toggleRightSidebar = () => {
  layoutStore.toggleRightSidebar()
}

const toggleSwap = () => {
  layoutStore.toggleSwap()
}


import { useI18n } from 'vue-i18n'
const { locale } = useI18n()

const switchLanguage = (lang: string) => {
  locale.value = lang
  setPersistence('layout', {'userLanguage': lang})
}

onMounted(() => {
  const savedLang = getPersistence('layout', 'userLanguage') || navigator.language.slice(0, 2)
  locale.value = ['en', 'zh'].includes(savedLang) ? savedLang : 'en'
})

const hoverLanguage = ref(false)
const currentLanguage = computed(() => locale.value === 'en' ? 'EN' : '中文')

</script>

<style lang="scss" scoped>
@use '../styles/layout';
@use '../styles/layout-variables' as layout-variables;

.language-container {
  position: relative;
  margin: 12px 0;

  .lang-trigger {
    width: 100%;
    padding: 8px 16px;
    background: rgba(255, 255, 255, 0.9);
    border: 1px solid #ddd;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s ease;

    &:hover {
      background: white;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
  }

  .lang-menu {
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background: white;
    border-radius: 4px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    margin-top: 8px;

    button {
      padding: 8px 16px;
      width: 100%;
      text-align: left;

      &:hover {
        background: #f5f5f5;
      }
    }
  }

  // 过渡动画
  .slide-fade-enter-active {
    transition: all 0.3s ease-out;
  }

  .slide-fade-leave-active {
    transition: all 0.2s cubic-bezier(1, 0.5, 0.8, 1);
  }

  .slide-fade-enter-from,
  .slide-fade-leave-to {
    transform: translateY(10px);
    opacity: 0;
  }
}



@media (max-width: 768px) {
  .app-container {
    --left-width: #{layout-variables.$layout-mobile-left-width};
    --right-width: #{layout-variables.$layout-mobile-right-width};
  }
}
</style>
