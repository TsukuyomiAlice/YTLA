export interface SideCardProps {
  cardId?: number
  cardType?: string
  icon?: string
  background?: string
  name?: string
  tags?: string
  description?: string
  spanColumns?: number
  initialExpanded?: boolean
  showIcon?: boolean
  showTitle?: boolean
  showTags?: boolean
  showSettings?: boolean
  showDeactivate?: boolean
  showClose?: boolean
  order?: number
}


export type SideCardEmits = {
  (e: 'toggle-expanded', state: boolean): void
  (e: 'settings'): void
  (e: 'deactivate', id?: number): void
  (e: 'close', id?: number): void
  (e: 'left-action', action: string): void
  (e: 'update:tags', tags: string): void
  (e: 'edit', id: number): void
}


export type SideCardEmitFn = {
  <K extends keyof SideCardEmits>(event: string, ...args: Parameters<SideCardEmits[K]>): void
}
