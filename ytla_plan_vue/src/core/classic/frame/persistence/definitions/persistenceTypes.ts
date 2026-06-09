//// PanelContentState
export type PanelContentState = {
  displayMode: number
  moduleType: string
  globalFrame: {
    currentStep: number
    componentState: Record<string, unknown>
  }
  mainFrame: {
    currentStep: number
    componentState: Record<string, unknown>
  }
  subFrame: {
    currentStep: number
    componentState: Record<string, unknown>
  }
}

export type PersistenceNamespace<T = any> = {
  namespace: string
  version: number
  defaultState: T
  /** set 时的自定义逻辑（如 plans 的 key 删除） */
  onBeforeSet?: (updates: Record<string, any>, currentState: T) => Partial<T>
}
