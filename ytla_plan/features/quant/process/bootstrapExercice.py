import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'  # 设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 假设原始数据是这样的100个居民月收入
data = np.random.normal(5000, 1200, 100)
print(data)

# 进行1000次Bootstrap重抽样
bootstrap_means = []
for _ in range(1000):
    sample = np.random.choice(data, size=100, replace=True)
    bootstrap_means.append(np.mean(sample))

# 计算95%置信区间
lower = np.percentile(bootstrap_means, 2.5)
upper = np.percentile(bootstrap_means, 97.5)

print(f"估计的平均月收入: {np.mean(bootstrap_means):.2f} 元")
print(f"95% 置信区间: ({lower:.2f}, {upper:.2f}) 元")

# 绘制结果
plt.hist(bootstrap_means, bins=30, alpha=0.7, color='blue')
plt.axvline(x=lower, color='red', linestyle='--', label='2.5百分位数')
plt.axvline(x=upper, color='green', linestyle='--', label='97.5百分位数')
plt.title('Bootstrap平均月收入估计')
plt.xlabel('平均月收入（元）')
plt.ylabel('频次')
plt.legend()
plt.show()