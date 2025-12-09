<template>
  <div class="sphere-container" ref="container">
    <div class="angle-info" v-if="sphereStore">
      <div>
        固定轴角度 <br />
        Θ: {{ radString(sphereStore.theta) }} or {{ dmsString(sphereStore.theta) }}<br />
        φ: {{ radString(sphereStore.phi) }} or {{ dmsString(sphereStore.phi) }}
      </div>
      <div>
        球面轴角度 <br />
        Θ': {{ radString(sphereStore.thetaPrime) }} or {{ dmsString(sphereStore.thetaPrime) }}<br />
        φ': {{ radString(sphereStore.phiPrime) }} or {{ dmsString(sphereStore.phiPrime) }}
      </div>
      <div>
        角度差 <br />
        ΔΘ: {{ radString(sphereStore.deltaTheta) }} or {{ dmsString(sphereStore.deltaTheta) }}<br />
        Δφ: {{ radString(sphereStore.deltaPhi) }} or {{ dmsString(sphereStore.deltaPhi) }}
      </div>
    </div>
    <canvas ref="canvas"></canvas>
  </div>
</template>

<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'
import * as THREE from 'three'
import { useSphere } from '@/features/mathematics/modules/sphere/composables/useSphere.ts'
import { useStaticAxes } from '@/features/mathematics/modules/sphere/composables/useStaticAxes.ts'

const container = ref<HTMLElement | null>(null)
const canvas = ref<HTMLCanvasElement | null>(null)

import { useSphereStore } from '@/features/mathematics/modules/sphere/stores/sphereStore.ts'

const sphereStore = useSphereStore()

const radString = (rad: number) => `${rad.toFixed(4)} rad`
const dmsString = (rad: number) => {
  const deg = THREE.MathUtils.radToDeg(rad) // 先转换为角度
  const degrees = Math.abs(deg)
  const d = Math.floor(degrees)
  const m = Math.floor((degrees - d) * 60)
  const s = ((degrees - d - m / 60) * 3600).toFixed(3)
  return `${deg < 0 ? '-' : ''}${d}°${m.toString().padStart(2, '0')}'${s.padStart(6, '0')}"`
}

onMounted(() => {
  if (!container.value || !canvas.value) return

  // 初始化尺寸适配
  const setSize = () => {
    if (!container.value) return
    camera.aspect = container.value.clientWidth / container.value.clientHeight
    camera.updateProjectionMatrix()
    renderer.setSize(container.value.clientWidth, container.value.clientHeight)
  }

  // 创建 ResizeObserver 监听容器尺寸变化
  const resizeObserver = new ResizeObserver(() => {
    setSize()
    renderer.render(scene, camera)
  })

  // 初始化 Three.js 场景
  const scene = new THREE.Scene()
  const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000) // 初始比例设为1:1
  camera.position.set(0, 0, 15) // 保持Z轴观察方向
  camera.lookAt(0, 0, 0) // 明确指定观察原点

  const renderer = new THREE.WebGLRenderer({
    canvas: canvas.value,
    antialias: true,
    alpha: true, // 添加透明背景
  })

  // 立即设置初始尺寸
  setSize()

  // 开始观察容器
  resizeObserver.observe(container.value)

  // Create sphere and axes
  const { rotate: rotateSphere } = useSphere(scene, sphereStore)
  const { rotate: rotateStaticAxes } = useStaticAxes(scene, sphereStore)

  // Mouse interaction logic
  let isDragging = false
  let previousMousePosition = { x: 0, y: 0 }
  let isOnSphere = false

  const raycaster = new THREE.Raycaster()
  const mouse = new THREE.Vector2()

  const checkIntersection = (clientX: number, clientY: number) => {
    if (!canvas.value) return false

    const rect = canvas.value.getBoundingClientRect()
    mouse.x = ((clientX - rect.left) / rect.width) * 2 - 1
    mouse.y = -((clientY - rect.top) / rect.height) * 2 + 1

    raycaster.setFromCamera(mouse, camera)
    const intersects = raycaster.intersectObjects(scene.children)

    return intersects.some(
      (obj) =>
        obj.object instanceof THREE.Mesh && obj.object.geometry instanceof THREE.SphereGeometry,
    )
  }

  const onMouseDown = (e: MouseEvent) => {
    isDragging = true
    previousMousePosition = { x: e.clientX, y: e.clientY }
    isOnSphere = checkIntersection(e.clientX, e.clientY)
  }

  const onMouseMove = (e: MouseEvent) => {
    if (!isDragging) return

    const deltaX = e.clientX - previousMousePosition.x
    const deltaY = e.clientY - previousMousePosition.y

    rotateSphere(deltaX, deltaY)
    if (!isOnSphere) {
      rotateStaticAxes(deltaX, deltaY)
    }

    previousMousePosition = { x: e.clientX, y: e.clientY }
    renderer.render(scene, camera)
  }

  const onMouseUp = () => {
    isDragging = false
  }

  canvas.value.addEventListener('mousedown', onMouseDown)
  window.addEventListener('mousemove', onMouseMove)
  window.addEventListener('mouseup', onMouseUp)

  // Handle window resize
  const onResize = () => {
    if (!container.value) return

    camera.aspect = container.value.clientWidth / container.value.clientHeight
    camera.updateProjectionMatrix()
    renderer.setSize(container.value.clientWidth, container.value.clientHeight)
    renderer.render(scene, camera)
  }

  window.addEventListener('resize', onResize)

  // Initial render
  renderer.render(scene, camera)

  // Cleanup
  onUnmounted(() => {
    resizeObserver.disconnect()
    canvas.value?.removeEventListener('mousedown', onMouseDown)
    window.removeEventListener('mousemove', onMouseMove)
    window.removeEventListener('mouseup', onMouseUp)
    window.removeEventListener('resize', onResize)
  })
})
</script>

<style scoped lang="scss">
@use '@/features/mathematics/modules/sphere/styles/sphere-container';

.angle-info {
  position: absolute;
  top: 10px;
  left: 10px;
  background: rgba(255, 255, 255, 0.8);
  padding: 8px;
  border-radius: 4px;
  z-index: 1;
  font-family: monospace;

  div {
    margin-bottom: 4px;
    line-height: 1.3;
    font-size: 0.9em;
  }
}
</style>
