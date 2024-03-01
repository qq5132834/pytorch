
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy

a1 = numpy.array([[1,2],
                  [3,4],
                  [5,6]])
height, width = a1.shape
a2 = numpy.zeros([3,2,2], dtype="int")

for i in range(height):
    for j in range(width):
        v = a1[i][j]
        for k in range(width):
            a2[i][j][k] = v
            print(a2[i][j][k])




# 读
xzImg = mpimg.imread('D:/AAAAAAAAAAAAAAAAAAAA/github/chrome_plugin_run_localProgram/chrome/src/test/resources/person.jpg')
xzHeight, xzWidth, _a = xzImg.shape
print("width:", xzWidth)
print("height:", xzHeight)
print("_a:", _a)
print(type(xzImg))
print(type(xzImg[0][0][0]))
print(type(xzImg[0]))
print(type(xzImg[0]))
print(len(xzImg))
print(len(xzImg[0]))

xzy = numpy.empty([xzHeight, xzWidth, xzWidth], dtype="int")
print(len(xzy))
print(len(xzy[0]))
print(len(xzy[0][0]))

for z in range(xzHeight):
    print(z)
    for x in range(xzWidth):
        p = xzImg[z][x][0]
        for y in range(xzWidth):
            xzy[z][x][y]=p
            # print(xzy[x][z][y])


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
