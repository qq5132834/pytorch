import matplotlib.pyplot as plt
import numpy as np

# 读取图片并将像素转换为黑白
image = plt.imread("D:/AAAAAAAAAAAAAAAAAAAA/github/chrome_plugin_run_localProgram/chrome/src/test/resources/person.jpg")
bw_image = np.mean(image, axis=2)  # 转为灰度图像

# 将黑色像素转换为高100像素的立体几何
height = 100
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 获取图片的尺寸
height, width = bw_image.shape

# 遍历像素值，并根据灰度值设置立体效果
for y in range(height):
    print(y)
    for x in range(width):
        if bw_image[y, x] < 0.1:  # 将黑色像素转换为立体几何
            ax.bar3d(x, y, 0, 1, 1, height, color='b')

# 设置坐标轴范围
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_zlim(0, height)  # 立体几何高度范围

# 显示立体图
plt.show()
