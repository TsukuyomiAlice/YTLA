from pathlib import Path


def first_letter_upper(s):
    if s:
        return s[0].upper() + s[1:]
    return s


def create_components_files(base_path, module_type, module_sub_type):
    """
    生成 Module 具体功能实现目录的 components 文件

    参数：
        base_path: str - 基础路径
        module_type: str - 模块类型
        module_sub_type: str - 模块子类型
    """
    module_sub_type_upper = first_letter_upper(module_sub_type)
    dir_path = Path(base_path) / module_type / "modules" / module_sub_type / "components"
    dir_path.mkdir(parents=True, exist_ok=True)

    main_content = f'''<template>
  <{module_sub_type_upper}Main_00 />
</template>

<script setup lang="ts">
import {module_sub_type_upper}Main_00 from '@/features/{module_type}/modules/{module_sub_type}/components/{module_sub_type_upper}Main_00.vue'
</script>

<style scoped lang="scss">

</style>
'''

    with open(dir_path / f"{module_sub_type_upper}Main.vue", "w", encoding="utf-8") as f:
        f.write(main_content)
    print(f"已生成: {dir_path / f'{module_sub_type_upper}Main.vue'}")

    main_00_content = '''<template>
  
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">

</style>
'''

    with open(dir_path / f"{module_sub_type_upper}Main_00.vue", "w", encoding="utf-8") as f:
        f.write(main_00_content)
    print(f"已生成: {dir_path / f'{module_sub_type_upper}Main_00.vue'}")

    sub_content = f'''<template>
  <{module_sub_type_upper}Sub_00 />
</template>

<script setup lang="ts">
import {module_sub_type_upper}Sub_00 from '@/features/{module_type}/modules/{module_sub_type}/components/{module_sub_type_upper}Sub_00.vue'
</script>

<style scoped lang="scss">

</style>
'''

    with open(dir_path / f"{module_sub_type_upper}Sub.vue", "w", encoding="utf-8") as f:
        f.write(sub_content)
    print(f"已生成: {dir_path / f'{module_sub_type_upper}Sub.vue'}")

    sub_00_content = '''<template>
  
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">

</style>
'''

    with open(dir_path / f"{module_sub_type_upper}Sub_00.vue", "w", encoding="utf-8") as f:
        f.write(sub_00_content)
    print(f"已生成: {dir_path / f'{module_sub_type_upper}Sub_00.vue'}")



