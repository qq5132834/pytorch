import matplotlib.pyplot as plt
import numpy as np

# 读取图片并将像素转换为黑白
image = plt.imread("D:/AAAAAAAAAAAAAAAAAAAA/github/chrome_plugin_run_localProgram/chrome/src/test/resources/test.bmp")
# bw_image = np.mean(image, axis=2)  # 转为灰度图像

zHeight, xWidth, _a = image.shape

# 将黑色像素转换为高100像素的立体几何
yHeight = 50
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 获取图片的尺寸
# height, width = bw_image.shape

# 遍历像素值，并根据灰度值设置立体效果
for z in range(zHeight):
    print(z)
    for x in range(xWidth):
        if image[z, x, 0] == 0:  # 将黑色像素转换为立体几何
            ax.bar3d(x, z, 0, 1, 1, yHeight, color='b')

# 设置坐标轴范围
ax.set_xlim(0, xWidth)
ax.set_ylim(0, yHeight)
ax.set_zlim(0, zHeight)  # 立体几何高度范围

# 显示立体图
plt.show()
