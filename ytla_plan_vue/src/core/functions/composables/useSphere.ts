import * as THREE from 'three';

export function useSphere(scene: THREE.Scene) {
  // 创建球体
  const geometry = new THREE.SphereGeometry(5, 32, 32);
  const material = new THREE.MeshBasicMaterial({
    color: 0x00ff00,
    wireframe: true
  });
  const sphere = new THREE.Mesh(geometry, material);
  scene.add(sphere);

  // 创建球面轴
  const axes = new THREE.AxesHelper(7);
  scene.add(axes);

  // 旋转函数
  const rotate = (deltaX: number, deltaY: number) => {
    sphere.rotation.y += deltaX * 0.01;
    sphere.rotation.x += deltaY * 0.01;
    axes.rotation.y += deltaX * 0.01;
    axes.rotation.x += deltaY * 0.01;
  };

  return {
    rotate
  };
}
