import { ref, computed, watch } from 'vue'
import { parseTags, type TagArray } from '@/core/classic/plans/planCard/definitions/planTypes.ts'
import { usePersistence } from '@/core/classic/frame/main/composables/usePersistence.ts'

const { getPersistence, setPersistence } = usePersistence()

export const usePlanCard = (props: any, emit: any) => {
  const API_BASE = import.meta.env.VITE_API_BASE

  // icon
  const fullIconPath = computed(() => ({
    iconImage: props.icon ? `${API_BASE}/uploads/${props.icon}` : ''
  }))

  const handleIconError = (e: Event) => {
    (e.target as HTMLImageElement).style.display = 'none'
  }

  // background
  const containerStyle = computed(() => ({
    backgroundImage: props.background ? `url(${API_BASE}/uploads/${props.background})` : '',
    backgroundSize: 'cover',
    backgroundPosition: 'center'
  }))


  // tags
  const tagsArray = ref<TagArray>(parseTags(props.tags))

  watch(() => props.tags, (newVal) => {
    tagsArray.value = parseTags(newVal)
  })


  // dragging
  const isDragging = ref(false)
  const isPinned = ref(
    props.planId !== undefined
      ? getPersistence('planCards', 'pinned')[props.planId as string] || false
      : false
  )

  const handleDragStart = (e: DragEvent) => {
    if (isPinned.value) {
      e.preventDefault()
      return
    }
    isDragging.value = true
    e.dataTransfer?.setData('text/plain', props.planId?.toString() || '')
    document.body.classList.add('dragging-active')
  }

  const handleDragEnd = () => {
    isDragging.value = false
    document.body.classList.remove('dragging-active')
  }

  const togglePin = () => {
    isPinned.value = !isPinned.value
    setPersistence('planCards', {
      pinned: {
        ...getPersistence('planCards', 'pinned'),
        [props.planId as string]: isPinned.value
      }
    })
  }

  return {
    fullIconPath, handleIconError,
    containerStyle,
    tagsArray,
    isPinned, handleDragStart, handleDragEnd, togglePin
  }
}
