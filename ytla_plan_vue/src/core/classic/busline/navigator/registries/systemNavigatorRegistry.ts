import type { SystemConfig, SystemButtonConfig, SystemContext } from '@/core/classic/busline/navigator/definitions/systemTypes.ts'

let systemConfig: SystemConfig | null = null

const buttonRegistry = new Map<string, SystemButtonConfig>()

export function initSystem(config: SystemConfig): void {
  systemConfig = config
}

export function registerSystemButton(config: SystemButtonConfig): void {
  buttonRegistry.set(config.buttonId, config)
}

export function getSystemConfig(): SystemConfig | null {
  return systemConfig
}

export function getVisibleSystemButtons(context: SystemContext): SystemButtonConfig[] {
  const visibleButtons: SystemButtonConfig[] = []
  for (const button of buttonRegistry.values()) {
    const isVisible = button.visibleWhen ? button.visibleWhen(context) : true
    if (isVisible) {
      visibleButtons.push(button)
    }
  }
  return visibleButtons.sort((a, b) => (a.order ?? 0) - (b.order ?? 0))
}

export function getAllSystemButtons(): SystemButtonConfig[] {
  return Array.from(buttonRegistry.values()).sort((a, b) => (a.order ?? 0) - (b.order ?? 0))
}
