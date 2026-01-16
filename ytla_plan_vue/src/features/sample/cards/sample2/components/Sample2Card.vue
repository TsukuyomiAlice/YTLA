<template>
  <SideCard
    :span-columns="2"
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
import type { Sample2CardData } from '@/features/sample/cards/sample2/definitions/cardDataType.ts'

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
  } as Sample2CardData)
}

</script>
<style scoped lang="scss">

</style>
