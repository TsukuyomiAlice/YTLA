import { ref, computed, nextTick, watch } from 'vue'
import { useCardStore } from '@/core/sideCards/stores/cardStore.ts'
import { CardService } from '@/core/sideCards/services/cardService.ts'
import { parseTags, type TagArray } from '@/core/sideCards/types/cardTypes.ts'
import { usePersistence } from '@/core/frame/composables/usePersistence.ts'

const { getPersistence, setPersistence } = usePersistence()

export const useSideCard = (props: any, emit: any) => {
  const store = useCardStore()
  const API_BASE = import.meta.env.VITE_API_BASE
  const cardService = new CardService(API_BASE)

  // card_expand area
  const isExpanded = ref(
    props.cardId !== undefined
      ? getPersistence('cards', 'expanded')[props.cardId as string] || false
      : props.initialExpanded
  )

  watch(isExpanded, (newVal) => {
    if (props.cardId !== undefined) {
      setPersistence('cards', {
        expanded: {
          ...getPersistence('cards', 'expanded'),
          [props.cardId as string]: isExpanded.value
        }
      })
    }
    emit('toggle-expanded', newVal)
  })

  const toggleExpanded = () => {
    isExpanded.value = !isExpanded.value
  }

  // icon
  const fullIconPath = computed(() => ({
    iconImage: props.icon ? `${API_BASE}/uploads/${props.icon}` : ''
  }))

  const handleIconError = (e: Event) => {
    const img = e.target as HTMLImageElement
    img.style.display = 'none'

    // 添加重置监听器
    const resetDisplay = () => {
      img.style.display = ''
      img.removeEventListener('load', resetDisplay)
    }

    // 当新的src加载成功时自动重置显示
    img.addEventListener('load', resetDisplay)
  }

  // background
  const containerStyle = computed(() => ({
    backgroundImage: props.background ? `url(${API_BASE}/uploads/${props.background})` : '',
    backgroundSize: 'cover',
    backgroundPosition: 'center'
  }))

  // title
  const titleRef = ref<HTMLElement | null>(null)
  const isTitleEditable = ref(false)
  const originalTitle = ref(props.title)

  const handleTitleBlur = async (e: Event) => {
    const newTitle = (e.target as HTMLElement).innerText.trim()
    isTitleEditable.value = false

    if (newTitle !== originalTitle.value && props.cardId) {
      try {
        await store.updateCardTitle(props.cardId, newTitle)
        originalTitle.value = newTitle
      } catch (error) {
        if (titleRef.value) titleRef.value.innerText = originalTitle.value
      }
    }
  }

  // description
  const isDescriptionEditable = ref(false)
  const originalDescription = ref(props.description)

  const handleDescriptionBlur = async (e: Event) => {
    const newDescription = (e.target as HTMLElement).innerText.trim()
    isDescriptionEditable.value = false

    if (newDescription !== originalDescription.value && props.cardId) {
      try {
        await store.updateCardDescription(props.cardId, newDescription)
        originalDescription.value = newDescription
      } catch (error) {
        const el = document.querySelector('.editable-description') as HTMLElement
        el.innerText = originalDescription.value
      }
    }
  }

  // edit title and description
  const selectText = (element: Element | null) => {
    if (!element) return
    const range = document.createRange()
    range.selectNodeContents(element)
    const sel = window.getSelection()
    sel?.removeAllRanges()
    sel?.addRange(range)
  }

  const startEditing = (type: 'title' | 'description') => {
    if (type === 'title') {
      isTitleEditable.value = true
      nextTick(() => {
        if (titleRef.value) {
          titleRef.value.focus()
          selectText(titleRef.value)
        }
      })
    } else {
      isDescriptionEditable.value = true
      nextTick(() => {
        const el = document.querySelector('.editable-description') as HTMLElement | null
        el?.focus()
      })
    }
  }

  const cancelEdit = (type: 'title' | 'description') => {
    if (type === 'title') {
      isTitleEditable.value = false
      if (titleRef.value) {
        titleRef.value.innerText = originalTitle.value
      }
    } else {
      isDescriptionEditable.value = false
      const el = document.querySelector('.editable-description') as HTMLElement
      el.innerText = originalDescription.value
    }
  }

  // tags
  const tagsArray = ref<TagArray>(parseTags(props.tags))
  const isAddingTag = ref(false)
  const newTag = ref('')
  const tagInput = ref<HTMLInputElement | null>(null)

  watch(() => props.tags, (newVal) => {
    tagsArray.value = parseTags(newVal)
  })

  const startAddingTag = () => {
    isAddingTag.value = true
    nextTick(() => {
      tagInput.value?.focus()
    })
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

  const shouldShowAddButton = computed(() => {
    return tagsArray.value.length === 0 && !isAddingTag.value
  })

  const showAddButton = computed(() => {
    return !isAddingTag.value
  })

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

  const cancelAddTag = () => {
    isAddingTag.value = false
    newTag.value = ''
  }

  // icon and background
  const iconUploadInput = ref<HTMLInputElement | null>(null)
  const bgUploadInput = ref<HTMLInputElement | null>(null)

  const triggerIconUpload = () => {
    iconUploadInput.value?.click()
  }

  const triggerBgUpload = () => {
    bgUploadInput.value?.click()
  }

  const handleIconUpload = async (event: Event) => {
    await handleFileUpload(event, 'icon')
  }

  const handleBgUpload = async (event: Event) => {
    await handleFileUpload(event, 'background')
  }

  const handleFileUpload = async (event: Event, type: 'icon' | 'background') => {
    const input = event.target as HTMLInputElement
    const file = input.files?.[0]
    if (!file || !props.cardId) return

    try {
      const uploadResult = await cardService.uploadFile(type, file)

      if (type === 'icon') {
        await store.updateCardIcon(props.cardId, uploadResult.filename)
        fullIconPath.value.iconImage = `${API_BASE}/uploads/${uploadResult.filename}`
      } else {
        await store.updateCardBackground(props.cardId, uploadResult.filename)
        containerStyle.value.backgroundImage = `url(${API_BASE}/uploads/${uploadResult.filename})`
      }
    } catch (error) {
      console.error('上传失败:', error)
    } finally {
      input.value = ''
    }
  }

  const removeIcon = async () => {
    if (!props.cardId) return

    try {
      await store.updateCardIcon(props.cardId, '')
      fullIconPath.value.iconImage = ''
    } catch (error) {

    }
  }

  // buttons
  const handleDeactivate = async () => {
    if (props.cardId) {
      try {
        await store.deactivateCard(props.cardId)
        emit('deactivate', props.cardId)
      } catch (error) {

      }
    }
  }

  const handleClose = async () => {
    if (props.cardId) {
      try {
        await store.deleteCard(props.cardId)
        emit('close', props.cardId)
      } catch (error) {

      }
    }
  }

  const handleLeftAction = (action: string) => {
    emit('left-action', action)
  }

  // dragging
  const isDragging = ref(false)
  const isPinned = ref(
    props.cardId !== undefined
      ? getPersistence('cards', 'pinned')[props.cardId as string] || false
      : false
  )

  // 拖动处理函数
  const handleDragStart = (e: DragEvent) => {
    if (isPinned.value) {
      e.preventDefault()
      return
    }
    isDragging.value = true
    e.dataTransfer?.setData('text/plain', props.cardId?.toString() || '')
    document.body.classList.add('dragging-active')
  }

  const handleDragEnd = () => {
    isDragging.value = false
    document.body.classList.remove('dragging-active')
  }

  // 固定按钮点击处理
  const togglePin = () => {
    isPinned.value = !isPinned.value
    setPersistence('cards', {
      pinned: {
        ...getPersistence('cards', 'pinned'),
        [props.cardId as string]: isPinned.value
      }
    })
  }

  return {
    isExpanded,
    titleRef,
    isTitleEditable,
    isDescriptionEditable,
    originalTitle,
    originalDescription,
    tagsArray,
    isAddingTag,
    newTag,
    tagInput,
    fullIconPath,
    containerStyle,
    shouldShowAddButton,
    showAddButton,
    handleIconError,
    handleDeactivate,
    handleClose,
    toggleExpanded,
    handleLeftAction,
    startEditing,
    cancelEdit,
    handleTitleBlur,
    handleDescriptionBlur,
    startAddingTag,
    addNewTag,
    removeTag,
    cancelAddTag,
    triggerIconUpload,
    triggerBgUpload,
    iconUploadInput,
    bgUploadInput,
    handleIconUpload,
    handleBgUpload,
    removeIcon,
    isDragging,
    isPinned,
    handleDragStart,
    handleDragEnd,
    togglePin
  }
}
