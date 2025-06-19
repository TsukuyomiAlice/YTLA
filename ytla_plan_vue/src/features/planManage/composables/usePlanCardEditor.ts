import { ref, computed, nextTick, watch } from 'vue'
import { usePlanCardStore } from '@/features/planManage/stores/planCardStore.ts'
import { PlanService } from '@/core/plans/services/planService.ts'
import { parseTags, type Plan, type TagArray } from '@/core/plans/types/planTypes.ts'
import { usePanelStore } from '@/core/frame/services/panelStore.ts'

export const usePlanCardEditor = (props: any, emit: any) => {
  const store = usePlanCardStore()
  const API_BASE = import.meta.env.VITE_API_BASE
  const planService = new PlanService(API_BASE)

  const initializeEditData = (plan: Plan) => {
    tagsArray.value = parseTags(plan.tags || '')
    fullIconPath.value.iconImage = plan.icon_path ? `${API_BASE}/uploads/${plan.icon_path}` : ''
    containerStyle.value.backgroundImage = plan.background_path ? `url(${API_BASE}/uploads/${plan.background_path})` : ''
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

    if (newTitle !== originalTitle.value && props.planId) {
      try {
        await store.updatePlanTitle(props.planId, newTitle)
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

    if (newDescription !== originalDescription.value && props.planId) {
      try {
        await store.updatePlanDescription(props.planId, newDescription)
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

  const startEditing = async (type: 'title' | 'description') => {
    if (type === 'title') {
      isTitleEditable.value = true
      await nextTick(() => {
        if (titleRef.value) {
          titleRef.value.focus()
          selectText(titleRef.value)
        }
      })
    } else {
      isDescriptionEditable.value = true
      await nextTick(() => {
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
  const tagsArray = ref<TagArray>(parseTags(props.tags) || '')
  const isAddingTag = ref(false)
  const newTag = ref('')
  const tagInput = ref<HTMLInputElement | null>(null)

  watch(() => props.tags, (newVal) => {
    tagsArray.value = parseTags(newVal)
  })

  const startAddingTag = async () => {
    isAddingTag.value = true
    await nextTick(() => {
      tagInput.value?.focus()
    })
  }

  const addNewTag = async () => {
    const tagValue = newTag.value.trim()
    if (!tagValue || !props.planId) return

    const originalTags = [...tagsArray.value]
    const newTags = [...originalTags, tagValue]
    tagsArray.value = newTags
    emit('update:tags', newTags.join(','))

    try {
      await store.updatePlanTags(props.planId, newTags.join(','))
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
    if (!props.planId) return

    const originalTags = [...tagsArray.value]
    const removedTag = originalTags.splice(index, 1)[0]
    tagsArray.value = originalTags
    emit('update:tags', originalTags.join(','))

    try {
      await store.deletePlanTag(props.planId, removedTag)
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
    if (!file || !props.planId) return

    try {
      const uploadResult = await planService.uploadFile(type, file)

      if (type === 'icon') {
        await store.updatePlanIcon(props.planId, uploadResult.filename)
        fullIconPath.value.iconImage = `${API_BASE}/uploads/${uploadResult.filename}`
      } else {
        await store.updatePlanBackground(props.planId, uploadResult.filename)
        containerStyle.value.backgroundImage = `url(${API_BASE}/uploads/${uploadResult.filename})`
      }
    } catch (error) {
      console.error('上传失败:', error)
    } finally {
      input.value = ''
    }
  }

  const removeIcon = async () => {
    if (!props.planId) return

    try {
      await store.updatePlanIcon(props.planId, '')
      fullIconPath.value.iconImage = ''
    } catch (error) {
      // Handle error
    }
  }

  // buttons
  const handleDeactivate = async () => {
    if (props.planId) {
      try {
        await store.deactivatePlan(props.planId)
        props.active_flag.value = false
        emit('deactivate', props.planId)
      } catch (error) {
        // Handle error
      }
    }
  }
  const handleReactivate = async () => {
    if (props.planId) {
      try {
        await store.activatePlan(props.planId)
        props.active_flag.value = true
        emit('activate', props.planId)
      } catch (error) {
        // Handle error
      }
    }
  }

  const handleClose = async () => {
    if (props.planId) {
      try {
        await store.deletePlan(props.planId)
        emit('close', props.planId)

        const panelStore = usePanelStore()
        panelStore.switchPanel('plan_manage', 'planManage')
      } catch (error) {
        // Handle error
      }
    }
  }

  const handleCloseEditor = () => {
    const panelStore = usePanelStore()
    panelStore.switchPanel('plan_manage', 'planManage')
  }

  return {
    initializeEditData,
    fullIconPath, handleIconError,
    containerStyle,
    titleRef, isTitleEditable, handleTitleBlur,
    tagsArray,
    isAddingTag,
    shouldShowAddButton,
    showAddButton,
    newTag,
    tagInput,
    startEditing,
    cancelEdit,
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
    handleDeactivate, handleReactivate, handleClose, handleCloseEditor,
  }
}
