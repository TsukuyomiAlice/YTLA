import { ref, shallowRef } from 'vue'
import type { Component } from 'vue'
import { getCardEditorFlowManager, getDefaultCardEditorFlowManager } from '@/core/classic/cards/sideCard/flows/cardEditorFlowRegistry.ts'
import { useCardStore } from '@/core/classic/cards/sideCard/stores/cardStore.ts'
import type { CardData } from '@/core/classic/cards/sideCard/types/cardDataType.ts'
import type { CardSubType, CardType } from '@/core/classic/cards/sideCard/types/cardType.ts'

const editorState = ref({
  mode: null as 'create' | 'edit' | null,
  currentStep: shallowRef<Component | null>(null),
  editCardData: null as CardData | null,
  currentCardType: null as CardType | null,
  currentCardSubType: null as CardSubType | null,
  visible: false,
  currentStepIndex: 0
})

export function useSideCardEditor(cardContainer?: {
  cards: CardData[]
}) {
  const cardStore = useCardStore()

  const resetEditor = () => {
    editorState.value = {
      mode: null,
      currentStep: null,
      editCardData: null,
      currentCardType: null,
      currentCardSubType: null,
      visible: false,
      currentStepIndex: 0
    }
  }

  const loadStepComponent = (cardType: CardType) => {
    const manager = getCardEditorFlowManager(cardType) || getDefaultCardEditorFlowManager()

    if (!editorState.value.currentCardSubType) {
      editorState.value.currentStep = manager.initialStep
      return
    }

    const steps = manager.getSteps(editorState.value.currentCardSubType)

    editorState.value.currentStep = steps[0] || null
  }

  const showCreation = (cardType: CardType, subType?: CardSubType) => {
    resetEditor()
    editorState.value.mode = 'create'
    editorState.value.currentCardType = cardType
    editorState.value.currentCardSubType = subType || null
    editorState.value.visible = true
    loadStepComponent(cardType)
  }

  const showEdit = (card: CardData) => {
    resetEditor()
    editorState.value.mode = 'edit'
    editorState.value.editCardData = { ...card }
    editorState.value.currentCardType = card.card_type
    editorState.value.currentCardSubType = card.card_sub_type
    editorState.value.visible = true
    loadStepComponent(card.card_type)
  }

  const handleStepChange = (direction: 'next' | 'prev') => {

    if (!editorState.value.currentCardType || !editorState.value.currentCardSubType) return

    const manager = getCardEditorFlowManager(editorState.value.currentCardType)
    const steps = manager?.getSteps(editorState.value.currentCardSubType) || []

    if (steps.length === 0) return

    const currentIndex = steps.findIndex(step => step === editorState.value.currentStep)
    let newIndex = direction === 'next' ? currentIndex + 1 : currentIndex - 1

    if (newIndex === -1) {
      if (editorState.value.mode === 'create') {
        editorState.value.currentStep = manager?.initialStep || null
      }
      return
    }
    if (newIndex > steps.length) {
      newIndex = currentIndex
    }

    editorState.value.currentStep = steps[newIndex]
  }

  const handlePrev = () => {
    handleStepChange('prev')
  }

  const handleNext = (selectedSubType: CardSubType) => {
    editorState.value.currentCardSubType = selectedSubType
    handleStepChange('next')
  }

  const handleSubmit = async (payload: CardData | Omit<CardData, 'card_id'>) => {
    try {
      if (editorState.value.mode === 'create') {
        await cardStore.addCard(payload as Omit<CardData, 'card_id'>)
      } else {
        await cardStore.updateCard(
          (payload as CardData).card_id,
          payload
        )
      }
      if (cardContainer) {
        await cardStore.fetchCards()
      }
      resetEditor()
      return true
    } catch (error) {

      return false
    }
  }

  const closeEditor = () => {
    resetEditor()
  }

  return {
    editorState,
    resetEditor,
    showCreation,
    showEdit,
    loadStepComponent,
    handleStepChange,
    handlePrev,
    handleNext,
    handleSubmit,
    closeEditor
  }
}
