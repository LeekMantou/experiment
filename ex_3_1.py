import cv2
import numpy as np

# 步骤1: 加载图像并分割为红绿蓝通道
image = cv2.imread('1.jpg')
blue, green, red = cv2.split(image)

# 步骤2: 显示原始绿通道图像
cv2.imshow('Original Green Channel', green)

# 步骤3: 克隆绿通道图像两次
clone1 = green.copy()
clone2 = green.copy()

# 步骤4: 计算绿通道的最小值和最大值
min_value = np.min(green)
max_value = np.max(green)

# 步骤5: 将clone1的所有元素赋值为(thresh/2)
thresh = (max_value - min_value) / 2.0
clone1[:] = thresh

# 步骤6: 将clone2的所有元素赋值为0
clone2[:] = 0

# 步骤7: 使用cv2.compare比较图像
comparison_result = cv2.compare(green, clone1, cv2.CMP_GE)

# 步骤8: 使用cv2.subtract进行减法操作
processed_green = cv2.subtract(green, thresh / 2, green, comparison_result)

# 显示处理后的绿通道图像
cv2.imshow('Processed Green Channel', processed_green)

# 等待用户按下任意键，然后关闭所有窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
