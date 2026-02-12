<p>
 Language 
 <a href="../zh-CN/readme.md"> 简体中文 </a>
 <a href="../en-US/readme.md"> English </a>
</p>

# YTLA - Your T&L Assistant

### An Application Platform Framework with Web OS Vision

### Official

version 1.0

File Update Date: 2026-2-11

## Open Code, Free Addition

The project is completely open source, all code is publicly available in source code form.  
Therefore, you can customize it according to your needs.  
Before doing so, please read this document to ensure you have a sufficient understanding of the project's framework.

## Concepts

### Self-driven, Autonomous, Free

This is a self-driven platform framework.  
With the help of generative AI and combined with mature engineering standards, it reliably adds and extends the functions users want.  
The 'T' and 'L' in the product name are not defined — this is left for users to actively define.  
Thus, this platform will provide users with highly free application scenarios.

### Highly Modular

Functions under the framework will be provided to users in two different modules.  
**Modules** provide users with complete functions  
**Cards** provide users with convenient, instant interactions  
Modules can be combined in one or more **Plans** to provide users with exclusive workbenches for various needs.

### Highly Customizable

The framework separates front-end and back-end, with detailed and flexible architectural design.  
Combined with semantic definitions, the framework can be implemented in multiple programming languages.  
Specific architectural split definitions can ensure that the framework can have the same running effect in different programming languages.

## Framework Directory

- YTLA (this framework)
    - docs (readme.md)
    - frontend
        - docs
        - core
        - features
    - backend
        - docs
        - core
        - features
    - readme.md

## Using This Framework

#### Tip

Currently, this framework uses vue3 and python-flask. More languages are expected to be used in the future.

```bash
# Clone the project
git clone https://github.com/TsukuyomiAlice/YTLA

# Backend dependency installation
cd ytla_plan
pip install -r requirements.txt

# Frontend dependency installation
cd ../ytla_plan_vue
npm install

# Start development environment
npm run dev & flask run
```
