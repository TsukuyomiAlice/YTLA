<p>
Language
<a href="../zh-CN/readme.md"> 简体中文 </a>
<a href="../en-US/readme.md"> English </a>
</p>

# Scaffold

### YTLA Application

### Official

version 1.0

Backend Language and Framework: Python-Flask  
Frontend Language and Framework: Vue3  
Applicable YTLA core version: **classic**  
File Update Date: 2026-2-11

## This is a YTLA Standard Framework Application

This application is a dedicated application under the YTLA framework.  
Please note the frontend and backend development languages and frameworks.  
This application only guarantees normal loading and operation on the basis of meeting the YTLA ontology project.  
For customized YTLA project copies, please check the configuration and compatibility.

## Concepts

Scaffold can be used to generate basic frameworks and automated code to support rapid development and expansion.  
In the scaffold, there are different types of packages that follow different rule definitions.

### frontend_lang_framework

Frontend configuration generation framework.  
**lang** represents the language used by the frontend.  
**framework** represents the frontend development framework.

### backend_lang_framework

Backend configuration generation framework.  
**lang** and **framework** represent the backend language and framework respectively.

### general_version

Core version generation framework.  
**version** represents the version name of "core" applicable in the project.

## Application Package Directory

- YTLA (project)
    - ytla_plan (backend)
        - features
            - scaffold
                - docs (readme.md)
                - modules
                    - _type
                    - backend_python_flask
                    - frontend_vue3
                    - general_classic
                    - __init__.py
                - __init__.py
                - readme.md
    - ytla_plan_vue (frontend)
        - src
            - features
                - scaffold
                    - docs (readme.md)
                    - modules
                        - _type
                - readme.md

## Add This Application

### Important

1. Please ensure your YTLA project is the original version.  
2. Applicable core version: **classic**.  
3. Neither frontend nor backend in your YTLA project contains a directory with the feature name "scaffold".

If the above conditions are met, you can directly copy this project to the YTLA project directory.

#### If there are customizations?

It is recommended to check the differences between the customized configuration and the original configuration before carefully adding this application.
