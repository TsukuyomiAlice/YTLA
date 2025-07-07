import * as THREE from 'three';

export function useStaticAxes(scene: THREE.Scene) {
  // 创建固定轴
  const axes = new THREE.AxesHelper(10);
  axes.position.set(0, 0, 0);
  scene.add(axes);

  // 旋转函数
  const rotate = (deltaX: number, deltaY: number) => {
    axes.rotation.y += deltaX * 0.01;
    axes.rotation.x += deltaY * 0.01;
  };

  return {
    rotate
  };
}
