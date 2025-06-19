import { defineStore } from 'pinia'
import type { BaseCard } from '@/core/cards/types/cardTypes.ts'
import { CardService } from '@/core/cards/services/cardService.ts'

// 依赖注入配置
const API_BASE = import.meta.env.VITE_API_BASE
const cardService = new CardService(API_BASE)

export const useCardStore = defineStore('card', {
  state: () => ({
    cards: [] as BaseCard[],
    isLoading: false,
    error: null as string | null,
    cardFilter: '',
  }),
  actions: {
    async fetchCards() {
      this.isLoading = true
      try {
        this.cards = await cardService.fetchCards()
      } catch (error) {
        this._handleError(error, 'Failed to fetch cards')
      } finally {
        this.isLoading = false
      }
    },

    async addCard(cardData: Omit<BaseCard, 'card_id'>) {
      this.isLoading = true
      try {
        const newCard = await cardService.addCard(cardData)
        this.cards.push(newCard)
        return { ok: true, data: newCard }
      } catch (error) {
        this._handleError(error, 'Failed to add card')
      } finally {
        this.isLoading = false
      }
    },

    async updateCard(cardId: number, cardData: Omit<BaseCard, 'card_id'>) {
      this.isLoading = true
      try {
        const updatedCard = await cardService.updateCard(cardId, cardData)
        const index = this.cards.findIndex(c => c.card_id === cardId)
        if (index !== -1) this.cards[index] = updatedCard
        return updatedCard
      } catch (error) {
        this._handleError(error, 'Failed to update card')
      } finally {
        this.isLoading = false
      }
    },

    async deleteCard(cardId: number) {
      this.isLoading = true
      try {
        await cardService.deleteCard(cardId)
        this.cards = this.cards.filter(card => card.card_id !== cardId)
      } catch (error) {
        this._handleError(error, 'Failed to delete card')
      } finally {
        this.isLoading = false
      }
    },

    async deactivateCard(cardId: number) {
      this.isLoading = true
      try {
        await cardService.deactivateCard(cardId)
        const index = this.cards.findIndex(c => c.card_id === cardId)
        if (index !== -1) this.cards[index].active_flag = '0'
      } catch (error) {
        this._handleError(error, 'Failed to deactivate card')
      } finally {
        this.isLoading = false
      }
    },

    async updateCardTitle(cardId: number, newTitle: string) {
      this.isLoading = true
      try {
        const updatedCard = await cardService.updateCardTitle(cardId, newTitle)
        const index = this.cards.findIndex(c => c.card_id === cardId)
        if (updatedCard) {
          this.cards[index] = {
            ...this.cards[index],
            name: newTitle
          }
        }
      } catch (error) {
        this._handleError(error, 'Failed to update card')
      } finally {
        this.isLoading = false
      }
    },

    async updateCardDescription(cardId: number, newDescription: string) {
      this.isLoading = true
      try {
        const updatedCard = await cardService.updateCardDescription(cardId, newDescription)
        const index = this.cards.findIndex(c => c.card_id === cardId)
        if (updatedCard) {
          this.cards[index] = {
            ...this.cards[index],
            description: newDescription
          }
        }
      } catch (error) {
        this._handleError(error, 'Failed to update card')
      } finally {
        this.isLoading = false
      }
    },

    async updateCardIcon(cardId: number, iconName: string) {
      this.isLoading = true
      try {
        const updatedCard = await cardService.updateCardIcon(cardId, iconName)
        const index = this.cards.findIndex(c => c.card_id === cardId)
        if (index !== -1) {
          this.cards[index] = { ...this.cards[index], icon_path: iconName }
        }
      } catch (error) {
        this._handleError(error, '图标更新失败')
      } finally {
        this.isLoading = false
      }
    },

    async updateCardBackground(cardId: number, backgroundName: string) {
      this.isLoading = true
      try {
        const updatedCard = await cardService.updateCardBackground(cardId, backgroundName)
        const index = this.cards.findIndex(c => c.card_id === cardId)
        if (index !== -1) {
          this.cards[index] = { ...this.cards[index], background_path: backgroundName }
        }
      } catch (error) {
        this._handleError(error, '背景更新失败')
      } finally {
        this.isLoading = false
      }
    },

    async updateCardTags(cardId: number, tags: string) {
      this.isLoading = true
      try {
        const success = await cardService.updateCardTags(cardId, tags)
        if (success) {
          const index = this.cards.findIndex(c => c.card_id === cardId)
          if (index !== -1) {
            this.cards[index] = {
              ...this.cards[index],
              tags: tags
            }
          }
        }
      } catch (error) {
        this._handleError(error, '标签更新失败')
      } finally {
        this.isLoading = false
      }
    },

    async deleteCardTag(cardId: number, tag: string) {
      this.isLoading = true
      try {
        await cardService.deleteCardTag(cardId, tag)
        const index = this.cards.findIndex(c => c.card_id === cardId)
        if (index !== -1) {
          this.cards[index].tags = this.cards[index].tags
            .split(',')
            .filter(t => t !== tag)
            .join(',')
        }
      } catch (error) {
        this._handleError(error, '标签删除失败')
      } finally {
        this.isLoading = false
      }
    },

    _handleError(error: unknown, defaultMsg: string) {
      this.error = error instanceof Error ? error.message : defaultMsg
      console.error(this.error)
      throw error
    },

    updateFilter(value: string) {
      this.cardFilter = value
    }
  },
  getters: {
    activeCards(state): BaseCard[] {
      return state.cards.filter(card =>
        card.delete_flag === '0' && card.active_flag === '1'
      )
    },

    filteredCards(state): BaseCard[] {
      const filter = state.cardFilter.toLowerCase()
      return this.activeCards.filter(card => {
        const tags = card.tags?.toLowerCase().split(',') || []
        return tags.some(tag => tag.includes(filter)) ||
          card.card_type?.toLowerCase().includes(filter) ||
          card.card_sub_type?.toLowerCase().includes(filter)
      })
    },
  }
})
