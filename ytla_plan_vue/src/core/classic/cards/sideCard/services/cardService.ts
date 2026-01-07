import type { CardData } from '@/core/classic/cards/sideCard/definitions/cardDataType.ts';

export class CardService {
  constructor(private readonly API_BASE: string) {}

  async fetchCards(): Promise<CardData[]> {
    const response = await fetch(`${this.API_BASE}/get_cards`)
    if (!response.ok) throw new Error('Failed to get card')
    const data = await response.json()
    return data.success ? data.cards : []
  }

  async addCard(cardData: Omit<CardData, 'card_id'>): Promise<CardData> {
    const response = await fetch(`${this.API_BASE}/add_card`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(cardData)
    })
    if (!response.ok) throw new Error('Failed to add card')
    return response.json()
  }

  async deleteCard(cardId: number): Promise<boolean> {
    const response = await fetch(`${this.API_BASE}/delete_card/${cardId}`, {
      method: 'POST'
    })
    if (!response.ok) throw new Error('Failed to delete card')
    return response.ok
  }

  async deactivateCard(cardId: number): Promise<boolean> {
    const response = await fetch(`${this.API_BASE}/deactivate_card/${cardId}`, {
      method: 'POST'
    })
    if (!response.ok) throw new Error('Failed to deactivate card')
    return response.ok
  }

  async updateCardTitle(cardId: number, newTitle: string): Promise<CardData> {
    const response = await fetch(`${this.API_BASE}/update_card/${cardId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: newTitle })
    })
    if (!response.ok) throw new Error('Failed to update card')
    return response.json()
  }

  async updateCardDescription(cardId: number, description: string): Promise<CardData> {
    const response = await fetch(`${this.API_BASE}/update_card/${cardId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ description: description })
    })
    if (!response.ok) throw new Error('Failed to update card')
    return response.json()
  }

  async uploadFile(type: 'icon' | 'background', file: File): Promise<{
    success: boolean;
    filename: string
  }> {
    const formData = new FormData()
    formData.append('file', file)

    const response = await fetch(`${this.API_BASE}/upload/${type}`, {
      method: 'POST',
      body: formData
    })

    if (!response.ok) throw new Error('文件上传失败')
    return response.json()
  }

  async updateCardIcon(cardId: number, iconName: string): Promise<CardData> {
    const response = await fetch(`${this.API_BASE}/update_card/${cardId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ icon: iconName })
    })
    if (!response.ok) throw new Error('Failed to update card')
    return response.json()
  }

  async updateCardBackground(cardId: number, backgroundName: string): Promise<CardData> {
    const response = await fetch(`${this.API_BASE}/update_card/${cardId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ background: backgroundName })
    })
    if (!response.ok) throw new Error('Failed to update card')
    return response.json()
  }

  async updateCardTags(cardId: number, tags: string): Promise<CardData> {
    const response = await fetch(`${this.API_BASE}/update_card/${cardId}/tags`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ tags })
    })
    if (!response.ok) throw new Error('标签更新失败')
    return response.json()
  }

  async deleteCardTag(cardId: number, tag: string): Promise<boolean> {
    const response = await fetch(`${this.API_BASE}/update_card/${cardId}/tags`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ tag })
    })
    if (!response.ok) throw new Error('标签删除失败')
    return response.ok
  }

  async updateCard(cardId: number, cardData: Omit<CardData, 'card_id'>): Promise<CardData> {
    const response = await fetch(`${this.API_BASE}/update_card_detail/${cardId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(cardData)
    })
    if (!response.ok) throw new Error('Failed to update card')
    return response.json()
  }
}
