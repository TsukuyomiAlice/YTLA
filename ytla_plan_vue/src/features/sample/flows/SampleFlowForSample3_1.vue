<template>
  <SideCardEditorFlowNavigator
    :is-editing="isEditMode"
    :show-prev="showPrev"
    :show-next="showNext"
    @cancelEdit="handleCancel"
    @prev="handlePrev"
    @next="handleNext"
    @submit="handleSubmit"
  >
    <div>This is a test page to show sample card 3 (flow for sample card 3, step 1)</div>
    <div><input v-model="sampleData1"></div>
  </SideCardEditorFlowNavigator>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import SideCardEditorFlowNavigator from '@/core/cards/layouts/SideCardEditorFlowNavigator.vue'
import type { Sample3CardData, SampleCardSubType } from '@/features/sample/types/sampleCardTypes'
import { useFormStore } from '@/core/cards/stores/cardEditorFormStore.ts'

const props = defineProps<{
  mode: 'create' | 'edit'
  initialData?: Sample3CardData
  cardSubType: SampleCardSubType
}>()

const isEditMode = computed(() => props.mode === 'edit')
const showPrev = computed(() => !isEditMode.value)
const showNext = true

const formStore = useFormStore()
const sampleData1 = ref(formStore.formData.sample_data_1 || '' )
const initializeFormData = () => {
  if (!formStore.isInitialized) {
    formStore.initializeForm<Record<string, unknown>>({
      mode: props.mode,
      initialData: (props.initialData as unknown) as Record<string, unknown>,
      defaultData: {
        sample_data_1: '',
        sample_data_2: '',
        sample_data_3: '',
        ...(props.mode === 'create' ? {
          name: '',
          tags: '',
          description: ''
        } : {})
      }
    })
    formStore.isInitialized = true
    if (isEditMode) {
      formStore.isEditing = true
    }
  }
}


const updateFormData = () => {
  formStore.updateFormField({ field: 'sample_data_1', value: sampleData1.value })
}

const emit = defineEmits<{
  (e: 'submit', payload: Sample3CardData): void
  (e: 'cancel'): void
  (e: 'prev'): void
  (e: 'next', cardSubType: SampleCardSubType): void
}>()

const handleCancel = () => {
  formStore.resetForm()
  emit('cancel')
}
const handlePrev = () => {
  formStore.resetForm()
  emit('prev')
}
const handleNext = () => {
  updateFormData()
  emit('next', 'sample3')
}

const buildPayload = () => ({
  sample_data_1: formStore.formData.sample_data_1,
  sample_data_2: formStore.formData.sample_data_2,
  sample_data_3: formStore.formData.sample_data_3,
  ...(props.mode === 'create' ? {
    name: `新的${props.cardSubType}`,
    tags: '',
    description: ''
  } : {})
})

const canSubmit = true

const handleSubmit = () => {
  if (!canSubmit) return
  updateFormData()
  const basePayload = buildPayload()
  const fullPayload = props.mode === 'edit'
    ? { ...props.initialData, ...basePayload }
    : { ...basePayload, card_sub_type: props.cardSubType }

  emit('submit', fullPayload as Sample3CardData)
}

// 生命周期
onMounted(() => {
  initializeFormData()
  sampleData1.value = formStore.formData.sample_data_1 as string
})
</script>

<style scoped>

</style>
