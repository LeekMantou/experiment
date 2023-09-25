from PIL import Image

# 创建一个100x100的黑色图像
width, height = 100, 100
image = Image.new("RGB", (width, height), (0, 0, 0))

# 获取图像的像素数据
pixels = image.load()

# 定义矩形的顶点坐标
top_left = (20, 5)
bottom_right = (40, 20)

# 绘制绿色矩形
for x in range(top_left[0], bottom_right[0]):
    for y in range(top_left[1], bottom_right[1]):
        pixels[x, y] = (0, 255, 0)  # 设置像素颜色为绿色

# 保存图像
image.save("green_rectangle.png")

# 显示图像（可选）
image.show()
