import * as THREE from 'three'
import { useSphereStore } from '@/core/functions/stores/sphereStore'

const sphereStore = useSphereStore()

export function useStaticAxes(scene: THREE.Scene, sphereStore: any) {
  // 创建虚线轴
  const axes = new THREE.Group()

  // 创建三个轴向的虚线
  const createDashedLine = (color: number, direction: 'x' | 'y' | 'z') => {
    const points = []
    const geometry = new THREE.BufferGeometry()

    // 设置轴线长度
    points.push(new THREE.Vector3(0, 0, 0))
    points.push(
      new THREE.Vector3(
        direction === 'x' ? 10 : 0,
        direction === 'y' ? 10 : 0,
        direction === 'z' ? 10 : 0,
      ),
    )

    geometry.setFromPoints(points)

    const material = new THREE.LineDashedMaterial({
      color: color,
      dashSize: 0.5,
      gapSize: 0.3,
      linewidth: 1,
    })

    const line = new THREE.LineSegments(geometry, material)
    line.computeLineDistances() // 必须调用这个方法才能显示虚线
    axes.add(line)
  }

  createDashedLine(0xff0000, 'x') // X轴红色
  createDashedLine(0x00ff00, 'y') // Y轴绿色
  createDashedLine(0x0000ff, 'z') // Z轴蓝色

  scene.add(axes)

  const rotate = (deltaX: number, deltaY: number) => {
    axes.rotation.z += deltaX * 0.01 // 方位角
    axes.rotation.x += deltaY * 0.01 // 极角

    const euler = new THREE.Euler().setFromQuaternion(axes.quaternion, 'ZXY')
    const theta = THREE.MathUtils.radToDeg(euler.x)
    const phi = THREE.MathUtils.radToDeg(euler.z)

    sphereStore.updateAngles(euler.x, euler.z)
  }

  return {
    rotate,
  }
}
