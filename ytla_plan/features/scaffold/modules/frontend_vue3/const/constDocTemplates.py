# encode = utf-8

# Define language-specific templates
templates = {
    'zh-CN': {
        'base_readme': f"""
<p>
 语言
 <a href="./documents/readme/zh-CN/readme.md"> 简体中文 </a>
 <a href="./documents/readme/en-US/readme.md"> English </a>
</p>

""",
        'doc_readme': f"""
<p>
 语言
 <a href="../zh-CN/readme.md"> 简体中文 </a>
 <a href="../en-US/readme.md"> English </a>
</p>

""",
        'type_level': {
            'title': "YTLA应用",
            'author': "(你的作者名称)",
            'version': "version 1.0",
            'tech_stack': """前端语言及开发框架: Vue3, typescript  
适用YTLA core版本: **classic**  
文件更新日期: {date_string}""",
            'standard_app': "## 这是一个YTLA标准框架应用",
            'standard_app_desc': """本应用为YTLA框架下的专用应用.  
请注意前端的开发语言和框架.  
本应用仅保障在满足YTLA本体项目基础上可正常加载并运行.  
对已产生定制化的YTLA项目副本，请检查配置和兼容性.""",
            'concepts': "## 概念",
            'concepts_desc': "(在此描述你要开发的功能)",
            'dir_structure': "## 应用包目录",
            'dir_structure_text': "(在此描述目录结构)",
            'usage': "## 添加本应用",
            'usage_text': "(在此描述使用方法)"
        },
        'subtype_level': {
            'general_title': "YTLA 功能公用",
            'feature_title': "YTLA 特性",
            'author': "(你的作者名称)",
            'version': "version 1.0",
            'tech_stack': """前端语言及开发框架: Vue3, typescript  
适用YTLA core版本: **classic**  
文件更新日期: {date_string}""",
            'concepts': "## 概念",
            'concepts_desc': "(在此描述你要开发的功能)",
            'dir_structure': "## 应用包目录",
            'dir_structure_text': "(在此描述目录结构)",
        }
    },
    'en-US': {
        'base_readme': f"""
<p>
 language
 <a href="./docs/readme/zh-CN/readme.md"> 简体中文 </a>
 <a href="./docs/readme/en-US/readme.md"> English </a>
</p>

""",
        'doc_readme': f"""
<p>
 language
 <a href="../zh-CN/readme.md"> 简体中文 </a>
 <a href="../en-US/readme.md"> English </a>
</p>

""",
        'type_level': {
            'title': "YTLA Application",
            'author': "(Your Author Name)",
            'version': "version 1.0",
            'tech_stack': """Frontend Language and Framework: Vue3, typescript  
Applicable YTLA core version: **classic**  
File Update Date: {date_string}""",
            'standard_app': "## This is a YTLA Standard Framework Application",
            'standard_app_desc': """This application is a dedicated application under the YTLA framework.  
Please note the frontend development languages and frameworks.  
This application only guarantees normal loading and operation on the basis of meeting the YTLA ontology project.  
For customized YTLA project copies, please check the configuration and compatibility.""",
            'concepts': "## Concepts",
            'concepts_desc': "(Describe the feature you're going to make here)",
            'dir_structure': "## Application Package Directory",
            'dir_structure_text': "(Describe the directory structure here)",
            'usage': "## Add This Application",
            'usage_text': "(Describe how to use the Application here)"
        },
        'subtype_level': {
            'general_title': "YTLA Application General",
            'feature_title': "YTLA Application Feature",
            'author': "(Your Author Name)",
            'version': "version 1.0",
            'tech_stack': """Frontend Language and Framework: Vue3, typescript  
Applicable YTLA core version: **classic**  
File Update Date: {date_string}""",
            'concepts': "## Concepts",
            'concepts_desc': "(Describe the feature you're going to make here)",
            'dir_structure': "## Feature Package Directory",
            'dir_structure_text': "(Describe the directory structure here)",
        }
    }
}
