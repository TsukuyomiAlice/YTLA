<template>
  <EditorFlowNavigator
    :is-editing="isEditMode"
    :show-prev="showPrev"
    :submit-disabled="!canSubmit"
    @cancel="handleCancel"
    @prev="handlePrev"
    @submit="handleSubmit"
  >
    <div>This is a test page to show sample card 2 (flow for sample card 2, step 1)</div>
    <div><input v-model="sampleData1"></div>
    <div><input v-model="sampleData2"></div>
    <div><input v-model="sampleData3"></div>
  </EditorFlowNavigator>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import EditorFlowNavigator from '@/core/sideCards/_type/layouts/SideCardEditorFlowNavigator.vue'
import type { Sample2CardData, SampleCardSubType } from '@/features/sample/types/sampleCardTypes.ts'

const props = defineProps<{
  mode: 'create' | 'edit'
  initialData?: Sample2CardData
  cardSubType: SampleCardSubType
}>()

const emit = defineEmits<{
  (e: 'submit', payload: Sample2CardData | Omit<Sample2CardData, 'card_id'>): void
  (e: 'cancel'): void
  (e: 'prev'): void
}>()

const handleCancel = () => emit('cancel')
const handlePrev = () => emit('prev')

const isEditMode = computed(() => props.mode === 'edit')
const showPrev = computed(() => !isEditMode.value)

const sampleData1 = ref('')
const sampleData2 = ref('')
const sampleData3 = ref('')

const initializeEditData = () => {
  if (props.mode === 'edit' && props.initialData) {
    sampleData1.value = props.initialData.sample_data_1 || ''
    sampleData2.value = props.initialData.sample_data_2 || ''
    sampleData3.value = props.initialData.sample_data_3 || ''
  }
}

const buildPayload = () => ({
  sample_data_1: sampleData1.value,
  sample_data_2: sampleData2.value,
  sample_data_3: sampleData3.value,
  ...(props.mode === 'create' ? {
    name: `新的${props.cardSubType}`,
    tags: '',
    description: ''
  } : {})
})

const validateCanSubmit = () => {
  if (!sampleData1.value) {
    return false
  }
  return true
}

const canSubmit = computed(() => validateCanSubmit())

const handleSubmit = () => {
  if (!canSubmit.value) return

  const basePayload = buildPayload()
  const fullPayload = props.mode === 'edit'
    ? { ...props.initialData, ...basePayload }
    : { ...basePayload, card_sub_type: props.cardSubType }

  emit('submit', fullPayload as Sample2CardData | Omit<Sample2CardData, 'card_id'>)
}


// 生命周期
onMounted(initializeEditData)
</script>

<style scoped>

</style>
