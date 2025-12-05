import type { BaseModule } from '@/core/modules/_type/types/moduleTypes.ts';

export class ModuleService {
  constructor(private readonly API_BASE: string) {}

  async fetchModules(planId: number): Promise<BaseModule[]> {
    const response = await fetch(`${this.API_BASE}/get_modules/${planId}`)
    if (!response.ok) throw new Error('Failed to get module')
    const data = await response.json()
    return data.success ? data.modules : []
  }

  async addModule(moduleData: Omit<BaseModule, 'module_id'>): Promise<BaseModule> {
    const response = await fetch(`${this.API_BASE}/add_module`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(moduleData)
    })
    if (!response.ok) throw new Error('Failed to add module')
    return response.json()
  }

  async deleteModule(moduleId: number): Promise<boolean> {
    const response = await fetch(`${this.API_BASE}/delete_module/${moduleId}`, {
      method: 'POST'
    })
    if (!response.ok) throw new Error('Failed to delete module')
    return response.ok
  }

  async deactivateModule(moduleId: number): Promise<boolean> {
    const response = await fetch(`${this.API_BASE}/deactivate_module/${moduleId}`, {
      method: 'POST'
    })
    if (!response.ok) throw new Error('Failed to deactivate module')
    return response.ok
  }

  async activateModule(moduleId: number): Promise<boolean> {
    const response = await fetch(`${this.API_BASE}/activate_module/${moduleId}`, {
      method: 'POST'
    })
    if (!response.ok) throw new Error('Failed to activate module')
    return response.ok
  }

  async updateModuleTitle(moduleId: number, newTitle: string): Promise<BaseModule> {
    const response = await fetch(`${this.API_BASE}/update_module/${moduleId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: newTitle })
    })
    if (!response.ok) throw new Error('Failed to update module')
    return response.json()
  }

  async updateModuleBelongGroupName(moduleId: number, belongGroupName: string): Promise<BaseModule> {
    const response = await fetch(`${this.API_BASE}/update_module/${moduleId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ belong_group_name: belongGroupName })
    })
    if (!response.ok) throw new Error('Failed to update module')
    return response.json()
  }

  async updateModuleDescription(moduleId: number, description: string): Promise<BaseModule> {
    const response = await fetch(`${this.API_BASE}/update_module/${moduleId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ description: description })
    })
    if (!response.ok) throw new Error('Failed to update module')
    return response.json()
  }

  async uploadFile(type: 'icon' | 'background', file: File): Promise<{
    success: boolean;
    filename: string
  }> {
    const formData = new FormData()
    formData.append('file', file)

    const response = await fetch(`${this.API_BASE}/upload/${type}`, {
      method: 'POST',
      body: formData
    })

    if (!response.ok) throw new Error('文件上传失败')
    return response.json()
  }

  async updateModuleIcon(moduleId: number, iconName: string): Promise<BaseModule> {
    const response = await fetch(`${this.API_BASE}/update_module/${moduleId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ icon: iconName })
    })
    if (!response.ok) throw new Error('Failed to update module')
    return response.json()
  }

  async updateModuleBackground(moduleId: number, backgroundName: string): Promise<BaseModule> {
    const response = await fetch(`${this.API_BASE}/update_module/${moduleId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ background: backgroundName })
    })
    if (!response.ok) throw new Error('Failed to update module')
    return response.json()
  }

  async updateModuleTags(moduleId: number, tags: string): Promise<BaseModule> {
    const response = await fetch(`${this.API_BASE}/update_module/${moduleId}/tags`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ tags })
    })
    if (!response.ok) throw new Error('标签更新失败')
    return response.json()
  }

  async deleteModuleTag(moduleId: number, tag: string): Promise<boolean> {
    const response = await fetch(`${this.API_BASE}/update_module/${moduleId}/tags`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ tag })
    })
    if (!response.ok) throw new Error('标签删除失败')
    return response.ok
  }

  async updateModule(moduleId: number, moduleData: Omit<BaseModule, 'module_id'>): Promise<BaseModule> {
    const response = await fetch(`${this.API_BASE}/update_module_detail/${moduleId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(moduleData)
    })
    if (!response.ok) throw new Error('Failed to update module')
    return response.json()
  }
}
