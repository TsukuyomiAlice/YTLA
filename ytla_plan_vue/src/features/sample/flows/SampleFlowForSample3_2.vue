<template>
  <EditorFlowNavigator
    :is-editing="isEditMode"
    :show-prev="showPrev"
    :show-next="showNext"
    @cancelEdit="handleCancel"
    @prev="handlePrev"
    @next="handleNext"
    @submit="handleSubmit"
  >
    <div>This is a test page to show sample card 3 (flow for sample card 3, step 2)</div>
    <div><input v-model="sampleData2"></div>
  </EditorFlowNavigator>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import EditorFlowNavigator from '@/core/sideCards/layouts/SideCardEditorFlowNavigator.vue'
import type { Sample3CardData, SampleCardSubType } from '@/features/sample/types/sampleCardTypes'
import { useFormStore } from '@/core/sideCards/stores/cardEditorFormStore.ts'

const props = defineProps<{
  mode: 'create' | 'edit'
  initialData?: Sample3CardData
  cardSubType: SampleCardSubType
}>()

const isEditMode = computed(() => props.mode === 'edit')
const showPrev = true;
const showNext = true;

const formStore = useFormStore()

const sampleData2 = ref(formStore.formData.sample_data_2|| '')


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

// 更新表单数据到 formStore
const updateFormData = () => {
  formStore.updateFormField({ field: 'sample_data_2', value: sampleData2.value })
}

const handlePrev = () => {
  updateFormData()
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
const canSubmit = true;

const handleSubmit = () => {
  if (!canSubmit) return
  updateFormData()
  const basePayload = buildPayload()
  const fullPayload = props.mode === 'edit'
    ? { ...props.initialData, ...basePayload }
    : { ...basePayload, card_sub_type: props.cardSubType }

  emit('submit', fullPayload as Sample3CardData)
  formStore.resetForm()
}

</script>

<style scoped>

</style>
