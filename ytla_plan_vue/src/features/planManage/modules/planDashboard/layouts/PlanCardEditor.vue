<template>
  <div
    class="plan-container"
    :style="containerStyle"
  >

    <div class="main-content">
      <div class="action-column-top-big --top-left">
        <button
          class="action-button"
          @click.stop="triggerIconUpload"
          aria-label="修改图标"
          title="修改图标">
          <svg viewBox="0 0 24 24" fill="currentColor" class="icon-upload">
            <rect x="3" y="3" width="18" height="18" rx="3" ry="3" stroke="currentColor"
                  stroke-width="2" fill="none" />
            <circle cx="9" cy="10" r="1.5" fill="currentColor" />
            <circle cx="15" cy="10" r="1.5" fill="currentColor" />
            <path d="M8 15a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1" stroke="currentColor" stroke-width="1.5"
                  fill="none" stroke-linecap="round" />
          </svg>
        </button>
        <input
          ref="iconUploadInput"
          type="file"
          accept="image/*"
          hidden
          @change="handleIconUpload"
        >

        <button
          class="action-button"
          @click.stop="triggerBgUpload"
          aria-label="修改背景"
          title="修改背景">
          <svg viewBox="0 0 24 24" fill="currentColor" class="bg-upload">
            <path
              d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14zm-4-4v-2h-2v2h-2v2h2v2h2v-2h2v-2h-2zM13 7v2h2v2h-2v2H9v-2H7v-2h2V7z" />
          </svg>
        </button>
        <input
          ref="bgUploadInput"
          type="file"
          accept="image/*"
          hidden
          @change="handleBgUpload"
        >

      </div>

      <div class="action-column-top-big --top-right">
        <button
          class="action-button"
          @click="handleCloseEditor"
          aria-label="关闭编辑"
          title="关闭编辑"
        >
          <svg class="close-icon" viewBox="0 0 24 24" fill="currentColor">
            <path stroke="currentColor" stroke-width="2" d="M18 6L6 18M6 6l12 12" />
          </svg>
        </button>
      </div>


      <div class="content-wrapper">

        <div class="header">
          <div class="icon-container">
            <img
              :src="fullIconPath.iconImage"
              class="icon-big"
              @error="handleIconError"
              alt="">
            <button
              class="icon-remove-btn"
              @click.stop="removeIcon"
            >×
            </button>
          </div>
          <div class="title-wrapper">
            <h3>
              <div
                :ref="el => titleRef = el as HTMLElement | null"
                class="editable-title-large"
                :contenteditable="isTitleEditable"
                @click="startEditing('title')"
                @blur="handleTitleBlur"
                @keydown.enter="handleTitleBlur($event)"
                @keydown.esc="cancelEdit('title')"
                :data-placeholder="!name ? '...' : ''"
              >{{ name }}
              </div>
            </h3>
          </div>
        </div>

        <div class="tags-container-big"
             v-if="(tagsArray.length > 0 || isAddingTag || shouldShowAddButton)">
          <span class="tag-big" v-for="(tag, index) in tagsArray" :key="index">
            {{ tag }}
            <button class="tag-remove" @click.stop="removeTag(index)">×</button>
          </span>

          <button
            v-if="showAddButton"
            class="tag-add-button-big"
            @click.stop="startAddingTag"
          >
            +
          </button>

          <input
            v-if="isAddingTag"
            ref="tagInput"
            v-model="newTag"
            class="tag-input-big"
            type="text"
            placeholder="输入标签"
            @keydown.enter="addNewTag"
            @keydown.esc="cancelAddTag"
            @blur="addNewTag"
          >
        </div>

        <div class="description-text-large">
          <strong>
            <div
              class="editable-description-large"
              :contenteditable="true"
              @click="startEditing('description')"
              @blur="handleDescriptionBlur"
              @keydown.enter="handleDescriptionBlur($event)"
              @keydown.esc="cancelEdit('description')"
              :data-placeholder="!description ? '...' : ''"
            >{{ description }}
            </div>
          </strong>
        </div>

        <div class="action-column-bottom">
          <button
            v-if="activeFlag === '1'"
            class="rect-button gray"
            @click="handleDeactivate"
          >
            {{ $t('planManage.planDashboard.sub_00_100') }}
          </button>
          <button
            v-if="activeFlag === '0'"
            class="rect-button green"
            @click="handleReactivate"
          >
            {{ $t('planManage.planDashboard.sub_00_101') }}
          </button>
          <button
            class="rect-button red"
            @click="handleClose"
          >
            {{ $t('planManage.planDashboard.sub_00_102') }}
          </button>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Plan, TagString } from '@/core/domain/area/plans/types/planTypes.ts'

const props = withDefaults(defineProps<{
  mode: 'create' | 'edit'
  planId?: number
  tags?: TagString
  order?: number
  activeFlag?: string
}>(), {
  spanColumns: 1,
  tags: ''
})

import { ref } from 'vue'

const name = ref('')
const description = ref('')
const icon = ref('')
const background = ref('')
const activeFlag = ref('0')

const emit = defineEmits<{
  (e: 'activate', id?: number): void
  (e: 'deactivate', id?: number): void
  (e: 'close', id?: number): void
  (e: 'update:tags', tags: string): void
  (e: 'edit', id: number): void
}>()

// 加载plan数据
import { usePlanCardStore } from '@/core/domain/area/plans/stores/planCardStore.ts'

const planStore = usePlanCardStore()
const currentPlan = ref<Plan | null>(null)
const loadPlanData = async (planId: number) => {
  try {
    const plan = planStore.plans.find(p => p.plan_id === planId)
    if (plan) {
      currentPlan.value = plan
      name.value = plan.name
      description.value = plan.description
      icon.value = plan.icon_path as string
      background.value = plan.background_path as string
      activeFlag.value = plan.active_flag as string
      initializeEditData(plan)
    }
  } catch (error) {
    console.error('加载计划数据失败:', error)
  }
}

// 监听editingPlanId变化
import { onMounted, watch } from 'vue'
import { useModuleProcessStore } from '@/core/domain/area/modules/stores/moduleProcessStore.ts'

const moduleProcessStore = useModuleProcessStore()
onMounted(() => {
  loadPlanData(moduleProcessStore.belongPlanId as number)
})

watch(
  () => planStore.plans.find(p => p.plan_id === props.planId),
  (newPlan) => {
    if (newPlan) {
      name.value = newPlan.name
      description.value = newPlan.description
      icon.value = newPlan.icon_path || ''
      background.value = newPlan.background_path || ''
      activeFlag.value = newPlan.active_flag || '1'
      initializeEditData(newPlan)
    }
  },
  { deep: true }
)

// 初始化编辑数据
import { usePlanCardEditor } from '@/core/domain/area/plans/composables/usePlanCardEditor.ts'

const {
  initializeEditData,
  titleRef,
  isTitleEditable,
  tagsArray,
  isAddingTag,
  shouldShowAddButton,
  showAddButton,
  newTag,
  tagInput,
  fullIconPath,
  containerStyle,
  handleIconError,
  handleDeactivate,
  handleReactivate,
  handleClose,
  startEditing,
  cancelEdit,
  handleTitleBlur,
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
  handleCloseEditor
} = usePlanCardEditor(props, emit)

</script>

<style lang="scss" scoped>
@use '@/core/domain/area/plans/styles/plan-card-editor';
@use '@/core/domain/area/cards/styles/card-component-button';
@use '@/core/domain/area/cards/styles/card-component-icon';
@use '@/core/domain/area/cards/styles/card-component-tags';
@use '@/core/domain/area/cards/styles/card-component-text';
</style>
