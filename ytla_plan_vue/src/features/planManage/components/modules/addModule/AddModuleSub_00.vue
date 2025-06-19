<template>
  <div class="sub-container">
    <div v-if="!selectedModule">
      <h1>{{ $t(`planManage.AddModuleSub_00_000`) }}</h1>
    </div>

    <div v-else>
      <h1>{{ $t('planManage.AddModuleSub_00_100') }}&nbsp{{ $t(`${selectedModule.moduleType}.${selectedModule.moduleSubType}_subtype_name`) }}</h1>
      <div class="form-container">
        <div class="input-group">
          <input v-model="moduleName" :placeholder="$t('planManage.AddModuleSub_00_002')"
                 class="form-input">
          <textarea v-model="moduleDescription" :placeholder="$t('planManage.AddModuleSub_00_003')"
                    class="form-textarea"></textarea>
        </div>

        <div class="action-column-bottom">
          <button class="rect-button gray" @click="handleCancel">
            {{ $t('planManage.AddModuleSub_00_101') }}
          </button>
          <button class="rect-button green" @click="handleSubmit">
            {{ $t('planManage.AddModuleSub_00_100') }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useModuleCardStore } from '@/features/planManage/stores/moduleCardStore.ts'
import { useModuleProcessStore } from '@/core/modules/stores/moduleProcessStore.ts'

const moduleStore = useModuleCardStore()
const processStore = useModuleProcessStore()

const moduleName = ref('')
const moduleDescription = ref('')

const selectedModule = computed(() => moduleStore.selectedModule)

const handleCancel = () => {
  moduleStore.clearSelectedModule()
  resetForm()
}

const handleSubmit = async () => {
  if (!selectedModule.value || !moduleName.value) return

  try {
    await moduleStore.addModule({
      belong_plan_id: processStore.belongPlanId!,
      belong_group_name: '',
      module_type: selectedModule.value.moduleType,
      module_sub_type: selectedModule.value.moduleSubType,
      name: moduleName.value,
      description: moduleDescription.value,
      message: '',
      tags: '',
      active_flag: '1',
      delete_flag: '0'
    })
    resetForm()
    moduleStore.clearSelectedModule()
    await moduleStore.fetchModules(processStore.belongPlanId!)
  } catch (error) {
    console.error('添加模块失败:', error)
  }
}

const resetForm = () => {
  moduleName.value = ''
  moduleDescription.value = ''
}
</script>

<style scoped lang="scss">
@use '@/core/frame/styles/card-component-button';

.form-container {
  padding: 1rem;
  max-width: 500px;

  .input-group {
    margin: 1.5rem 0;

    .form-input {
      width: 100%;
      padding: 0.8rem;
      margin-bottom: 1rem;
      border: 1px solid #e0e0e0;
      border-radius: 4px;
    }

    .form-textarea {
      width: 100%;
      height: 100px;
      padding: 0.8rem;
      border: 1px solid #e0e0e0;
      border-radius: 4px;
      resize: vertical;
    }
  }
}
</style>
