import { defineStore } from 'pinia'

interface SphereState {
  theta: number // 弧度值
  phi: number // 弧度值
  thetaPrime: number
  phiPrime: number
}

export const useSphereStore = defineStore('sphere', {
  state: (): SphereState => ({
    theta: 0, // 固定轴极角（与Z轴夹角）
    phi: 0, // 固定轴方位角（XY平面旋转）
    thetaPrime: 0, // 球面轴极角（与Z轴夹角）
    phiPrime: 0, // 球面轴方位角（XY平面旋转）
  }),

  getters: {
    deltaTheta: (state) => {
      const diff = Math.abs(state.theta - state.thetaPrime)
      return Math.min(diff % (2 * Math.PI), 2 * Math.PI - (diff % (2 * Math.PI)))
    },
    deltaPhi: (state) => {
      const diff = Math.abs(state.phi - state.phiPrime)
      return Math.min(diff % (2 * Math.PI), 2 * Math.PI - (diff % (2 * Math.PI)))
    },
  },

  actions: {
    updateAngles(theta: number, phi: number) {
      this.theta = theta
      this.phi = phi
    },
    updatePrimeAngles(thetaPrime: number, phiPrime: number) {
      this.thetaPrime = thetaPrime
      this.phiPrime = phiPrime
    },
  },
})
