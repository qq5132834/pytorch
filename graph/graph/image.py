
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy

# 读
xzImg = mpimg.imread('D:/AAAAAAAAAAAAAAAAAAAA/github/chrome_plugin_run_localProgram/chrome/src/test/resources/person.jpg')
xzHeight, xzWidth, _ = xzImg.shape
print("width:", xzWidth)
print("height:", xzHeight)
print(type(xzImg))
print(type(xzImg[0][0][0]))
print(type(xzImg[0]))
print(type(xzImg[0]))
print(len(xzImg))
print(len(xzImg[0]))

xzy = numpy.empty([xzWidth, xzHeight, xzWidth], dtype="int")
print(len(xzy))
print(len(xzy[0]))
print(len(xzy[0][0]))

for z in range(xzHeight):
    for x in range(xzWidth):
        p = xzImg[x][z][0]
        for y in range(xzWidth):
            v = xzy[x][z][y]
            xzy[x][z][y]= p




# print(xzImg)

yzImg = mpimg.imread('D:/AAAAAAAAAAAAAAAAAAAA/github/chrome_plugin_run_localProgram/chrome/src/test/resources/loong.jpg')
yzHeight, yzWidth, _ = yzImg.shape
print("图片的宽度为:", yzWidth)
print("图片的高度为:", yzHeight)
print(type(yzImg))


# 显示图片
# plt.imshow(img)
# plt.axis('off')  # 关闭坐标轴
# plt.show()
#
# # 打印图片的像素值
# print("图片的像素值矩阵：")
# print(img)
