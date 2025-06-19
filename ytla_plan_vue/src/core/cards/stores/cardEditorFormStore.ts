import { defineStore } from 'pinia'

type FormState<T extends Record<string, unknown> = Record<string, unknown>> = {
  formData: Partial<T>
  isEditing: boolean
  isInitialized: boolean
  currentStep: number
}

export const useFormStore = defineStore('cardEditorForm', {
  state: () => ({
    formData: {},
    isEditing: false,
    isInitialized: false,
    currentStep: 1
  } as FormState),

  actions: {
    initializeForm<T extends Record<string, unknown>>(config: {
      mode: 'create' | 'edit'
      initialData?: Partial<T>
      defaultData: T
    }) {
      this.resetForm()
      this.isEditing = config.mode === 'edit'
      this.isInitialized = true
      this.formData = {
        ...config.defaultData,
        ...(config.initialData || {})
      }
    },

    updateFormField<K extends keyof FormState['formData']>(
      payload: { field: K; value: FormState['formData'][K] }
    ) {
      this.formData[payload.field] = payload.value
    },

    resetForm() {
      this.formData = {}
      this.isEditing = false
      this.isInitialized = false
      this.currentStep = 1
    }
  }
})
