import { ref, computed, nextTick, watch } from 'vue'
import { useCardStore } from '@/core/classic/cards/sideCard/stores/cardStore.ts'
import type { SideCardProps, SideCardEmits } from '@/core/classic/cards/sideCard/definitions/sideCardType.ts'
import { parseTags } from '@/core/classic/cards/sideCard/definitions/cardDataType.ts'

export const useContainerTags = (props: SideCardProps, emit: SideCardEmits) => {
  const store = useCardStore()

  const tagsArray = ref<string[]>(parseTags(props.tags || ''))
  const isAddingTag = ref(false)
  const newTag = ref('')
  const tagInput = ref<HTMLInputElement | null>(null)

  watch(
    () => props.tags || '',
    (newVal) => {
      tagsArray.value = parseTags(newVal)
    },
  )

  watch(
    () => isAddingTag.value,
    (newVal) => {
      if (newVal) {
        newTag.value = ''
      }
    }
  )

  const shouldShowAddButton = computed(() => {
    return tagsArray.value.length === 0 && !isAddingTag.value
  })

  const showAddButton = computed(() => {
    return !isAddingTag.value
  })

  const startAddingTag = async () => {
    isAddingTag.value = true
    await nextTick()
    tagInput.value?.focus()
  }

  const addNewTag = async () => {
    const tagValue = newTag.value.trim()
    if (!tagValue || !props.cardId) return

    const originalTags = [...tagsArray.value]
    const newTags = [...originalTags, tagValue]
    tagsArray.value = newTags
    emit('update:tags', newTags.join(','))

    try {
      await store.updateCardTags(props.cardId, newTags.join(','))
    } catch (error) {
      tagsArray.value = originalTags
      emit('update:tags', originalTags.join(','))
    } finally {
      cancelAddTag()
    }
  }

  const removeTag = async (index: number) => {
    if (!props.cardId) return

    const originalTags = [...tagsArray.value]
    const removedTag = originalTags.splice(index, 1)[0]
    tagsArray.value = originalTags
    emit('update:tags', originalTags.join(','))

    try {
      await store.deleteCardTag(props.cardId, removedTag)
    } catch (error) {
      tagsArray.value = [...originalTags, removedTag]
      emit('update:tags', [...originalTags, removedTag].join(','))
    }
  }

  const handleTagInput = (e: Event) => {
    const target = e.target as HTMLInputElement
    newTag.value = target.value
  }

  const cancelAddTag = () => {
    isAddingTag.value = false
    newTag.value = ''
  }

  return {
    tagsArray, isAddingTag, newTag, tagInput, shouldShowAddButton, showAddButton, startAddingTag, addNewTag, removeTag, handleTagInput, cancelAddTag }
}
