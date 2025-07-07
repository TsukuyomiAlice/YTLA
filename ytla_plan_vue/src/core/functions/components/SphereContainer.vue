<template>
  <div class="sphere-container" ref="container">
    <canvas ref="canvas"></canvas>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue';
import * as THREE from 'three';
import { useSphere } from '@/core/functions/composables/useSphere.ts';
import { useStaticAxes } from '@/core/functions/composables/useStaticAxes';

export default defineComponent({
  name: 'SphereContainer',
  setup() {
    const container = ref<HTMLElement | null>(null);
    const canvas = ref<HTMLCanvasElement | null>(null);

    onMounted(() => {
      if (!container.value || !canvas.value) return;

      // 初始化Three.js场景
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(
        75,
        container.value.clientWidth / container.value.clientHeight,
        0.1,
        1000
      );
      camera.position.z = 15;

      const renderer = new THREE.WebGLRenderer({ canvas: canvas.value });
      renderer.setSize(container.value.clientWidth, container.value.clientHeight);

      // 使用球体和轴
      const { rotate: rotateSphere } = useSphere(scene);
      const { rotate: rotateStaticAxes } = useStaticAxes(scene);

      // 鼠标交互
      let isDragging = false;
      let previousMousePosition = { x: 0, y: 0 };
      let isOnSphere = false;

      const raycaster = new THREE.Raycaster();
      const mouse = new THREE.Vector2();

      const checkIntersection = (clientX: number, clientY: number) => {
        if (!canvas.value) return false;

        const rect = canvas.value.getBoundingClientRect();
        mouse.x = ((clientX - rect.left) / rect.width) * 2 - 1;
        mouse.y = -((clientY - rect.top) / rect.height) * 2 + 1;

        raycaster.setFromCamera(mouse, camera);
        const intersects = raycaster.intersectObjects(scene.children);

        return intersects.some(obj => obj.object instanceof THREE.Mesh && obj.object.geometry instanceof THREE.SphereGeometry);
      };

      const onMouseDown = (e: MouseEvent) => {
        isDragging = true;
        previousMousePosition = { x: e.clientX, y: e.clientY };
        isOnSphere = checkIntersection(e.clientX, e.clientY);
      };

      const onMouseMove = (e: MouseEvent) => {
        if (!isDragging) return;

        const deltaX = e.clientX - previousMousePosition.x;
        const deltaY = e.clientY - previousMousePosition.y;

        rotateSphere(deltaX, deltaY);
        if (!isOnSphere) {
          rotateStaticAxes(deltaX, deltaY);
        }

        previousMousePosition = { x: e.clientX, y: e.clientY };
        renderer.render(scene, camera);
      };

      const onMouseUp = () => {
        isDragging = false;
      };

      canvas.value.addEventListener('mousedown', onMouseDown);
      window.addEventListener('mousemove', onMouseMove);
      window.addEventListener('mouseup', onMouseUp);

      // 处理窗口大小变化
      const onResize = () => {
        if (!container.value) return;

        camera.aspect = container.value.clientWidth / container.value.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.value.clientWidth, container.value.clientHeight);
        renderer.render(scene, camera);
      };

      window.addEventListener('resize', onResize);

      // 初始渲染
      renderer.render(scene, camera);

      // 清理
      return () => {
        canvas.value?.removeEventListener('mousedown', onMouseDown);
        window.removeEventListener('mousemove', onMouseMove);
        window.removeEventListener('mouseup', onMouseUp);
        window.removeEventListener('resize', onResize);
      };
    });

    return {
      container,
      canvas
    };
  }
});
</script>

<style scoped lang="scss">
@use '@/core/functions/styles/sphere-container';
</style>
