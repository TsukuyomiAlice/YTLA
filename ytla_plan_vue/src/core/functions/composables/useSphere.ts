import * as THREE from 'three'
import { useSphereStore } from '@/core/functions/stores/sphereStore'

const sphereStore = useSphereStore()

export function useSphere(scene: THREE.Scene, sphereStore: any) {
  // 创建球体
  const geometry = new THREE.SphereGeometry(5, 32, 32)
  const material = new THREE.MeshBasicMaterial({
    color: 0x2194ce, // 修改为蓝色（可根据需要调整）
    transparent: true, // 添加透明属性
    opacity: 0.3, // 设置透明度
  })
  const sphere = new THREE.Mesh(geometry, material)
  scene.add(sphere)

  // 创建球面轴
  const axes = new THREE.AxesHelper(7)
  scene.add(axes)

  // 旋转函数
  const rotate = (deltaX: number, deltaY: number) => {
    sphere.rotation.z += deltaX * 0.01 // 方位角绕Z轴旋转
    sphere.rotation.x += deltaY * 0.01 // 极角绕X轴旋转
    axes.rotation.z += deltaX * 0.01
    axes.rotation.x += deltaY * 0.01

    // 使用ZXY旋转顺序获取欧拉角
    const euler = new THREE.Euler().setFromQuaternion(sphere.quaternion, 'ZXY')
    const theta = THREE.MathUtils.radToDeg(euler.x) // 极角（与Z轴夹角）
    const phi = THREE.MathUtils.radToDeg(euler.z) // 方位角（XY平面旋转）

    sphereStore.updatePrimeAngles(euler.x, euler.z)
  }

  return {
    rotate,
  }
}
