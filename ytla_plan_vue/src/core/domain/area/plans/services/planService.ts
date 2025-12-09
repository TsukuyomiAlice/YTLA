import type { Plan } from '@/core/domain/area/plans/types/planTypes.ts'

export class PlanService {
  constructor(private readonly API_BASE: string) {
  }

  async fetchPlans(): Promise<Plan[]> {
    const response = await fetch(`${this.API_BASE}/get_plans`)
    if (!response.ok) throw new Error('Failed to get plan')
    const data = await response.json()
    return data.success ? data.plans : []
  }

  async addPlan(planData: Omit<Plan, 'plan_id'>): Promise<Plan> {
    const response = await fetch(`${this.API_BASE}/add_plan`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(planData)
    })
    if (!response.ok) throw new Error('Failed to add plan')
    return response.json()
  }

  async deletePlan(planId: number): Promise<boolean> {
    const response = await fetch(`${this.API_BASE}/delete_plan/${planId}`, {
      method: 'POST'
    })
    if (!response.ok) throw new Error('Failed to delete plan')
    return response.ok
  }

  async deactivatePlan(planId: number): Promise<boolean> {
    const response = await fetch(`${this.API_BASE}/deactivate_plan/${planId}`, {
      method: 'POST'
    })
    if (!response.ok) throw new Error('Failed to deactivate plan')
    return response.ok
  }

  async activatePlan(planId: number): Promise<boolean> {
    const response = await fetch(`${this.API_BASE}/activate_plan/${planId}`, {
      method: 'POST'
    })
    if (!response.ok) throw new Error('Failed to activate plan')
    return response.ok
  }

  async updatePlanTitle(planId: number, newTitle: string): Promise<Plan> {
    const response = await fetch(`${this.API_BASE}/update_plan/${planId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: newTitle })
    })
    if (!response.ok) throw new Error('Failed to update plan')
    return response.json()
  }

  async updatePlanDescription(planId: number, description: string): Promise<Plan> {
    const response = await fetch(`${this.API_BASE}/update_plan/${planId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ description: description })
    })
    if (!response.ok) throw new Error('Failed to update plan')
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

  async updatePlanIcon(planId: number, iconName: string): Promise<Plan> {
    const response = await fetch(`${this.API_BASE}/update_plan/${planId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ icon: iconName })
    })
    if (!response.ok) throw new Error('Failed to update plan')
    return response.json()
  }

  async updatePlanBackground(planId: number, backgroundName: string): Promise<Plan> {
    const response = await fetch(`${this.API_BASE}/update_plan/${planId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ background: backgroundName })
    })
    if (!response.ok) throw new Error('Failed to update plan')
    return response.json()
  }

  async updatePlanTags(planId: number, tags: string): Promise<Plan> {
    const response = await fetch(`${this.API_BASE}/update_plan/${planId}/tags`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ tags })
    })
    if (!response.ok) throw new Error('标签更新失败')
    return response.json()
  }

  async deletePlanTag(planId: number, tag: string): Promise<boolean> {
    const response = await fetch(`${this.API_BASE}/update_plan/${planId}/tags`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ tag })
    })
    if (!response.ok) throw new Error('标签删除失败')
    return response.ok
  }

  async updatePlanModuleGroups(planId: number, moduleGroups: string, belong_module_group_old: string, belong_module_group_new: string): Promise<Plan> {
    const response = await fetch(`${this.API_BASE}/update_plan/${planId}/module_groups`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ module_groups: moduleGroups, old_module_group_name: belong_module_group_old, new_module_group_name: belong_module_group_new })
    })
    if (!response.ok) throw new Error('模块组更新失败')
    return response.json()
  }

  async deletePlanModuleGroup(planId: number, group: string): Promise<boolean> {
    const response = await fetch(`${this.API_BASE}/update_plan/${planId}/module_groups`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ module_group: group })
    })
    if (!response.ok) throw new Error('模块组删除失败')
    return response.ok
  }
}

