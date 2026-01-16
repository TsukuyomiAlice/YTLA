import { nextTick, ref } from 'vue'
import { useModuleCardStore } from '@/core/classic/modules/moduleCard/stores/moduleCardStore.ts'
import { usePlanCardStore } from '@/core/classic/plans/planCard/stores/planCardStore.ts'
import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'


const moduleStore = useModuleCardStore()
const planStore = usePlanCardStore()
const moduleProcessStore = useModuleProcessStore()

export const useModuleGroup = (props: any, emit: any) => {

  const isEditing = ref(false)
  const tempName = ref('')

  const editingGroup = () => {
    isEditing.value = true
    tempName.value = props.groupName
    nextTick(() => {
      const el = document.querySelector('.editable-group-name') as HTMLElement
      el.focus()
    })
  }

  const handleNameBlur = (e: Event) => {
    const newName = (e.target as HTMLElement).innerText.trim()
    if (newName && newName !== props.groupName) {
      emit('update:groupName', newName)
    }
    isEditing.value = false
  }

  const cancelEditing = () => {
    isEditing.value = false
  }

  const handleDeleteGroup = async () => {
    if (!moduleProcessStore.belongPlanId) return

    try {
      // 将分组内所有模块移动到未分组
      const modulesInGroup = moduleStore.modules.filter(
        m => m.belong_plan_id === moduleProcessStore.belongPlanId &&
          m.belong_group_name === props.groupName
      )

      for (const module of modulesInGroup) {
        await moduleStore.updateModule(module.module_id, {
          ...module,
          belong_group_name: ''
        })
      }

      // 从计划中移除该分组
      const plan = planStore.plans.find(p => p.plan_id === moduleProcessStore.belongPlanId)
      if (plan) {
        const groups = plan.module_groups.split(',').filter(g => g !== props.groupName)
        await planStore.deletePlanModuleGroup(
          moduleProcessStore.belongPlanId,
          props.groupName
        )
      }

      emit('deleteGroup', props.groupName)

      await moduleStore.fetchModules(moduleProcessStore.belongPlanId as number)
    } catch (error) {
      console.error('删除分组失败:', error)
    }
  }

  return {
    isEditing, tempName,
    editingGroup, handleNameBlur, cancelEditing, handleDeleteGroup
  }
}
