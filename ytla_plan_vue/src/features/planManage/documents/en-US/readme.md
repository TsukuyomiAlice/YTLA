<p>
 Language 
 <a href="../zh-CN/readme.md"> 简体中文 </a>
 <a href="../en-US/readme.md"> English </a>
</p>

# Plan Management

### YTLA Key Application

### Official

version 1.0

Backend Language and Framework: Python-Flask  
Frontend Language and Framework: Vue3, typescript  
Applicable YTLA core version: **classic**  
File Update Date: 2026-2-12

## This is a YTLA Standard Framework Application

This application is a dedicated application under the YTLA framework.  
Please note the frontend and backend development languages and frameworks.  
This application only guarantees normal loading and operation on the basis of meeting the YTLA ontology project.  
For customized YTLA project copies, please check the configuration and compatibility.

### Important: Key Application

This application is a key application.  
For frontend pages, other applications need to be scheduled through this application.  
If multiple key applications are enabled at the same time, please make sure there are no conflicts between different key applications.

## Concepts

Plan Management will be responsible for the important functions of users creating, browsing, managing plans, and module management on browser pages.

### Plan Manager

Displays all active plans for users, creates and manages plans, etc.

### Plan Dashboard

Displays the specific details of user plans.
Add modules, create module categories.

### Add Module

Users can select modules they want to add to the current plan.

### Settings

All settings related to plans and modules.

### Welcome

YTLA's introduction page.

## Application Package Directory

- planManage
    - docs (readme.md)
    - cards
        - _type (default)
    - modules
        - _type (default)
        - addModule
        - planDashboard
        - planManager
        - settings
        - welcome
          readme.md
