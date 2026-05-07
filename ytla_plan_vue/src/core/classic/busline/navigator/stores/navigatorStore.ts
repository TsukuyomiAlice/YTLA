import { defineStore } from 'pinia'
import type { SystemContext, SystemButtonConfig } from '@/core/classic/busline/navigator/definitions/systemTypes.ts'
import { getAllSystemButtons, getVisibleSystemButtons } from '@/core/classic/busline/navigator/registries/systemNavigatorRegistry.ts'

export const useNavigatorStore = defineStore('navigator', {
  state: () => ({
    activeButtonIds: [] as string[]
  }),

  getters: {
    activeButtons: (state) => (context: SystemContext): SystemButtonConfig[] => {
      const visibleButtons = getVisibleSystemButtons(context)
      return visibleButtons.filter(button => state.activeButtonIds.includes(button.buttonId))
    }
  },

  actions: {
    setActiveButtons(buttonIds: string[]) {
      this.activeButtonIds = [...buttonIds]
    },

    addButton(buttonId: string) {
      if (!this.activeButtonIds.includes(buttonId)) {
        this.activeButtonIds.push(buttonId)
      }
    },

    removeButton(buttonId: string) {
      this.activeButtonIds = this.activeButtonIds.filter(id => id !== buttonId)
    },

    clearButtons() {
      this.activeButtonIds = []
    },

    activateAllButtons() {
      const allButtons = getAllSystemButtons()
      this.activeButtonIds = allButtons.map(button => button.buttonId)
    }
  }
})
