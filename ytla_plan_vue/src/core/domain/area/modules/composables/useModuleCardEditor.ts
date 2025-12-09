import { ref, computed, nextTick, watch } from 'vue'
import { useModuleCardStore } from '@/core/domain/area/modules/stores/moduleCardStore.ts'
import { ModuleService } from '@/core/domain/area/modules/services/moduleService.ts'
import { parseTags, type BaseModule } from '@/core/domain/area/modules/types/moduleTypes.ts'
import { useModuleProcessStore } from '@/core/domain/area/modules/stores/moduleProcessStore.ts'

export const useModuleCardEditor = (props: any, emit: any) => {
  const store = useModuleCardStore()
  const API_BASE = import.meta.env.VITE_API_BASE
  const moduleService = new ModuleService(API_BASE)

  const initializeEditData = (module: BaseModule) => {
    tagsArray.value = parseTags(module.tags || '')
    fullIconPath.value.iconImage = module.icon_path ? `${API_BASE}/uploads/${module.icon_path}` : ''
    containerStyle.value.backgroundImage = module.background_path ? `url(${API_BASE}/uploads/${module.background_path})` : ''
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

    if (newTitle !== originalTitle.value && props.moduleId) {
      try {
        await store.updateModuleTitle(props.moduleId, newTitle)
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

    if (newDescription !== originalDescription.value && props.moduleId) {
      try {
        await store.updateModuleDescription(props.moduleId, newDescription)
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
  const tagsArray = ref<string[]>(parseTags(props.tags) || '')
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
    if (!tagValue || !props.moduleId) return

    const originalTags = [...tagsArray.value]
    const newTags = [...originalTags, tagValue]
    tagsArray.value = newTags
    emit('update:tags', newTags.join(','))

    try {
      await store.updateModuleTags(props.moduleId, newTags.join(','))
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
    if (!props.moduleId) return

    const originalTags = [...tagsArray.value]
    const removedTag = originalTags.splice(index, 1)[0]
    tagsArray.value = originalTags
    emit('update:tags', originalTags.join(','))

    try {
      await store.deleteModuleTag(props.moduleId, removedTag)
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
    if (!file || !props.moduleId) return

    try {
      const uploadResult = await moduleService.uploadFile(type, file)

      if (type === 'icon') {
        await store.updateModuleIcon(props.moduleId, uploadResult.filename)
        fullIconPath.value.iconImage = `${API_BASE}/uploads/${uploadResult.filename}`
      } else {
        await store.updateModuleBackground(props.moduleId, uploadResult.filename)
        containerStyle.value.backgroundImage = `url(${API_BASE}/uploads/${uploadResult.filename})`
      }
    } catch (error) {
      console.error('上传失败:', error)
    } finally {
      input.value = ''
    }
  }

  const removeIcon = async () => {
    if (!props.moduleId) return

    try {
      await store.updateModuleIcon(props.moduleId, '')
      fullIconPath.value.iconImage = ''
    } catch (error) {
      // Handle error
    }
  }

  // buttons
  const handleDeactivate = async () => {
    if (props.moduleId) {
      try {
        await store.deactivateModule(props.moduleId)
        props.active_flag.value = false
        emit('deactivate', props.moduleId)
      } catch (error) {
        // Handle error
      }
    }
  }
  const handleReactivate = async () => {
    if (props.moduleId) {
      try {
        await store.activateModule(props.moduleId)
        props.active_flag.value = true
        emit('activate', props.moduleId)
      } catch (error) {
        // Handle error
      }
    }
  }

  const handleClose = async () => {
    if (props.moduleId) {
      try {
        await store.deleteModule(props.moduleId)
        emit('close', props.moduleId)

      } catch (error) {
        // Handle error
      }
    }
  }

  const handleCloseEditor = () => {
    const moduleProcessStore = useModuleProcessStore()
    moduleProcessStore.clearEditingModule()
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
