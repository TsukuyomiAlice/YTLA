<template>
  <SideCard
    :span-columns="3"
    :card-id="cardId"
    :name="name"
    :icon="iconPath"
    :background="background"
    :tags="tags"
    :description="description"
    :showIcon=true
    :showTitle=true
    :showTags=true
    :showSettings=true
    :showDeactivate=true
    :showClose=true
    @settings="handleEdit"
  >

    <template #top-left-actions></template>
    <template #top-actions></template>

    <template #card-content>
      <div class="card-content">
        <div class="card-content-item">
          <span class="card-content-item-title">Sample Data 1:</span>
          <span class="card-content-item-value">{{ sampleData1 }}</span>
        </div>
        <div class="card-content-item">
          <span class="card-content-item-title">Sample Data 2:</span>
          <span class="card-content-item-value">{{ sampleData2 }}</span>
        </div>
        <div class="card-content-item">
          <span class="card-content-item-title">Sample Data 3:</span>
          <span class="card-content-item-value">{{ sampleData3 }}</span>
        </div>
      </div>
    </template>

    <template #left-actions-buttons>

    </template>

    <template #right-actions></template>

    <template #secondary-content>

    </template>

  </SideCard>
</template>
<script setup lang="ts">
import { useSideCardEditor } from '@/core/classic/cards/sideCardEditor/composables/useSideCardEditor.ts'
import SideCard from '@/core/classic/cards/sideCard/components/SideCard.vue'
import type { Sample3CardData } from '@/features/sample/cards/sample3/definitions/cardDataType.ts'

const props = defineProps({
  cardId: Number,
  name: String,
  tags: String,
  description: String,
  iconPath: String,
  background: String,

  sampleData1: String,
  sampleData2: String,
  sampleData3: String
})



const handleEdit = () => {
  const { showEdit } = useSideCardEditor()
  showEdit({
    card_id: props.cardId,
    name: props.name,
    tags: props.tags,
    description: props.description,
    card_sub_type: 'sample1',
    sample_data_1: props.sampleData1,
    sample_data_2: props.sampleData2,
    sample_data_3: props.sampleData3,
  } as Sample3CardData)
}

</script>
<style scoped lang="scss">

</style>
