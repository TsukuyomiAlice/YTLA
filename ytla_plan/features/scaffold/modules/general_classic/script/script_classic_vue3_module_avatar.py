from pathlib import Path


def first_letter_upper(s):
    if s:
        return s[0].upper() + s[1:]
    return s


def create_avatar_file(base_path, module_type, module_sub_type):
    """
    生成 Module 具体功能实现目录的 Avatar.vue 文件

    参数：
        base_path: str - 基础路径
        module_type: str - 模块类型
        module_sub_type: str - 模块子类型
    """
    file_path = Path(base_path) / module_type / "modules" / module_sub_type / "avatar" / "Avatar.vue"

    file_path.parent.mkdir(parents=True, exist_ok=True)

    content = '''<template>
  
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">

</style>
'''

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"已生成: {file_path}")



