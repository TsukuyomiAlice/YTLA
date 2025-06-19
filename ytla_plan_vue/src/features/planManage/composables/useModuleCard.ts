import { ref, computed, watch } from 'vue'
import { useModuleProcessStore } from '@/core/modules/stores/moduleProcessStore.ts'
import { usePanelStore } from '@/core/frame/services/panelStore.ts'
import { useModuleCardStore } from '@/features/planManage/stores/moduleCardStore.ts'

export const useModuleCard = (props: any, emit: any) => {
  const API_BASE = import.meta.env.VITE_API_BASE

  // icon
  const fullIconPath = computed(() => ({
    iconImage: props.icon_path ? `${API_BASE}/uploads/${props.icon_path}` : ''
  }))

  const handleIconError = (e: Event) => {
    (e.target as HTMLImageElement).style.display = 'none'
  }

  // background
  const containerStyle = computed(() => ({
    backgroundImage: props.background_path ? `url(${API_BASE}/uploads/${props.background_path})` : '',
    backgroundSize: 'cover',
    backgroundPosition: 'center'
  }))


  // dragging
  const isDragging = ref(false)

  const handleDragStart = (e: DragEvent) => {
    isDragging.value = true
    e.dataTransfer?.setData('moduleId', props.moduleId.toString())
  }

  const handleDragEnd = () => {
    isDragging.value = false
  }

  // click and edit module property
  const handleModuleClick = (moduleId: number) => {
    if (isDragging.value) return
    const moduleProcessStore = useModuleProcessStore()
    const panelStore = usePanelStore()
    const moduleStore = useModuleCardStore()
    // 获取模块的 subType
    const module = moduleStore.modules.find(m => m.module_id === moduleId)
    if (!module) return
    if (module.active_flag === '0') startEditing(moduleId)
    else {
      // 设置当前模块
      moduleProcessStore.setModule(moduleId, moduleProcessStore.belongPlanId!)
      // 切换面板到当前模块
      panelStore.switchPanel(`plan_${moduleProcessStore.belongPlanId}`, moduleId)
    }
  }


  const startEditing = (moduleId: number) => {
    const moduleProcessStore = useModuleProcessStore()
    moduleProcessStore.setEditingModule(moduleId)
  }

  return {
    fullIconPath, handleIconError,
    containerStyle,
    isDragging, handleDragStart, handleDragEnd,
    handleModuleClick, startEditing
  }
}
