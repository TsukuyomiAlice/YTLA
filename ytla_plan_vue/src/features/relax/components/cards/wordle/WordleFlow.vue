<template>
  <EditorFlowNavigator
    :is-editing="isEditMode"
    :show-prev="showPrev"
    :submit-disabled="!canSubmit"
    @cancel="handleCancel"
    @prev="handlePrev"
    @submit="handleSubmit"
  >
    <div>Click submit to add game wordle</div>
  </EditorFlowNavigator>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import EditorFlowNavigator from '@/core/sideCards/_type/layouts/SideCardEditorFlowNavigator.vue'
import type { WordleCardData, RelaxCardSubType } from '@/features/relax/types/relaxCardTypes.ts'

const props = defineProps<{
  mode: 'create' | 'edit'
  initialData?: WordleCardData
  cardSubType: RelaxCardSubType
}>()

const emit = defineEmits<{
  (e: 'submit', payload: WordleCardData | Omit<WordleCardData, 'card_id'>): void
  (e: 'cancel'): void
  (e: 'prev'): void
}>()

const handleCancel = () => emit('cancel')
const handlePrev = () => emit('prev')

const isEditMode = computed(() => props.mode === 'edit')
const showPrev = computed(() => !isEditMode.value)

const initializeEditData = () => {
  if (props.mode === 'edit' && props.initialData) {
  }
}

const buildPayload = () => ({
  ...(props.mode === 'create' ? {
    name: `新的${props.cardSubType}`,
    tags: '',
    description: ''
  } : {})
})

const validateCanSubmit = () => {
  return true
}

const canSubmit = computed(() => validateCanSubmit())

const handleSubmit = () => {
  if (!canSubmit.value) return

  const basePayload = buildPayload()
  const fullPayload = props.mode === 'edit'
    ? { ...props.initialData, ...basePayload }
    : { ...basePayload, card_sub_type: props.cardSubType }

  emit('submit', fullPayload as WordleCardData | Omit<WordleCardData, 'card_id'>)
}


// 生命周期
onMounted(initializeEditData)
</script>

<style scoped>

</style>
