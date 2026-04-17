from pathlib import Path

def first_letter_upper(s):
    if s:
        return s[0].upper() + s[1:]
    return s

def create_components_file(base_path, module_type, module_sub_type):
    """
    生成 SideCard 具体功能实现目录的主组件文件

    参数：
        base_path: str - 基础路径
        module_type: str - 模块类型
        module_sub_type: str - 模块子类型
    """
    module_sub_type_upper = first_letter_upper(module_sub_type)

    file_path = Path(base_path) / module_type / "cards" / module_sub_type / "components" / f"{module_sub_type_upper}Card.vue"

    file_path.parent.mkdir(parents=True, exist_ok=True)

    content = f'''<template>
  <SideCard
    :card-id="cardId"
    :name="name"
    :icon="iconPath"
    :background="background"
    :tags="tags"
    :description="description"
    :show-icon="true"
    :show-title="true"
    :show-tags="true"
    :showSettings="true"
    :showDeactivate="true"
    :showClose="true"
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
import SideCard from '@/core/classic/cards/sideCard/components/SideCard.vue'
import {{ use{module_sub_type_upper} }} from '@/features/{module_type}/cards/{module_sub_type}/composables/use{module_sub_type_upper}.ts'
import type {{ {module_sub_type_upper}CardData }} from '@/features/{module_type}/cards/{module_sub_type}/definitions/cardDataType.ts'

const props = defineProps({{
  cardId: Number,
  name: String,
  tags: String,
  description: String,
  iconPath: String,
  background: String,
}})

const emit = defineEmits<{{

}}>()

const {{ handleEdit }} = use{module_sub_type_upper}(props, emit)
</script>

<style scoped lang="scss">

</style>
'''

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"已生成: {file_path}")



