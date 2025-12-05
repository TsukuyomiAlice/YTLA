import { defineStore } from 'pinia'
import { usePersistence } from '@/core/frame/_type/composables/usePersistence.ts'

const { getPersistence, setPersistence } = usePersistence()

export const useLayoutStore = defineStore('layout', {
  state: () => ({
    isSideBarSwapped: false,
    isRightSideBarVisible: false,
    mainContentDisplayMode: 1,
    isRightSideBarExpanded: false,
  }),
  actions: {
    // Initialize main layout state from persistence, or use default values if not found
    initialize() {
      const savedLayout = getPersistence('layout', 'layoutSwapped')
      const savedSidebar = getPersistence('layout', 'sidebarVisible')

      this.isSideBarSwapped = savedLayout ? savedLayout : false
      this.isRightSideBarVisible = savedSidebar ? savedSidebar : false
    },

    // Toggle the visibility of the right sidebar
    toggleRightSidebar() {
      this.isRightSideBarVisible = !this.isRightSideBarVisible
      const savedSidebar = this.isRightSideBarVisible
      setPersistence('layout', {'sidebarVisible': savedSidebar})
    },

    // Toggle the swap state of the main layout between left and right
    toggleSwap() {
      this.isSideBarSwapped = !this.isSideBarSwapped
      const savedLayout = this.isSideBarSwapped
      setPersistence('layout', {'layoutSwapped': savedLayout})

      if (this.isRightSideBarVisible) {
        setTimeout(() => {
          this.isRightSideBarVisible = true
        }, 0)
      }
    },

    // Toggle the expand state of the main layout for the subframe
    // Default is false and the subFrame is shown
    toggleExpand() {
      this.isRightSideBarExpanded = !this.isRightSideBarExpanded
    }
  },
  getters: {
    // Determine the label for the toggle button based on the current state of the main layout
    // and whether the right sidebar is visible
    toggleButtonLabel: (state) => {
      const arrow = state.isRightSideBarVisible ?
        (state.isSideBarSwapped ? '◀' : '▶') :
        (state.isSideBarSwapped ? '▶' : '◀')
      return `${arrow}`
    },

    // Determine the style for the toggle button based on the current state of the main layout
    toggleButtonStyle: (state) => {
      const baseOffset = 0
      const dynamicOffset = state.isRightSideBarVisible
        ? `calc(max(200px, 38.2vw) + ${baseOffset}rem)`
        : `${baseOffset}rem`

      return {
        [state.isSideBarSwapped ? 'left' : 'right']: dynamicOffset
      }
    },

    // Determine the style for the mainframe area based on the current state of the main layout
    showSubFrame: (state) => {
      const modeRules = {
        1: false,
        2: true,
        3: !state.isRightSideBarExpanded,
        4: !state.isRightSideBarExpanded,
        5: !state.isRightSideBarExpanded,
        6: !state.isRightSideBarExpanded,
        7: !state.isRightSideBarExpanded
      };
      const modeKey = state.mainContentDisplayMode as keyof typeof modeRules;
      return modeRules[modeKey] ?? false;
    },

    // Determine the style for the position of the subframe area based on the current state of the main layout
    swapSubFrame: (state) => {
      const modeRules = {
        1: false,
        2: false,
        3: true,
        4: false,
        5: true,
        6: false,
        7: true,
      };
      const modeKey = state.mainContentDisplayMode as keyof typeof modeRules;
      return modeRules[modeKey] ?? false;
    }
  }
})
