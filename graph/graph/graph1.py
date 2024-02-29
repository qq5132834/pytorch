import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建一个立方体的顶点坐标
vertices = np.array([
    [1, 1, 1],  # V0
    [-1, 1, 1], # V1
    [-1, -1, 1],# V2
    [1, -1, 1], # V3
    [1, -1, -1],# V4
    [1, 1, -1], # V5
    [-1, 1, -1],# V6
    [-1, -1, -1]# V7
])

# 创建一个立方体的面
faces = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],  # 正面
    [vertices[0], vertices[5], vertices[4], vertices[3]],  # 顶面
    [vertices[0], vertices[5], vertices[6], vertices[1]],  # 右面
    [vertices[1], vertices[6], vertices[7], vertices[2]],  # 底面
    [vertices[2], vertices[7], vertices[4], vertices[3]],  # 左面
    [vertices[4], vertices[5], vertices[6], vertices[7]]   # 背面
]

# 将面的顶点坐标展开为一维数组
x = np.array([point[0] for face in faces for point in face])
y = np.array([point[1] for face in faces for point in face])
z = np.array([point[2] for face in faces for point in face])

# 创建 3D 图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制 3D 点云
ax.scatter(x, y, z, c='b', marker='o')

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
