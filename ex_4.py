import cv2
import numpy as np

# 加载两张图片
src1 = cv2.imread('src1.jpg')
src2 = cv2.imread('src2.jpg')

# 缩小图像尺寸
src1 = cv2.resize(src1, (400, 200))
src2 = cv2.resize(src2, (400, 200))

# 检查图片是否加载成功
if src1 is None or src2 is None:
    print("无法加载图片")
else:
    # a. 计算diff12并显示
    diff12 = cv2.absdiff(src1, src2)

    # b. 对diff12进行腐蚀和膨胀操作
    kernel = np.ones((5, 5), np.uint8)
    cleandiff = cv2.erode(diff12, kernel, iterations=1)
    cleandiff = cv2.dilate(cleandiff, kernel, iterations=1)

    # c. 对diff12进行膨胀和腐蚀操作
    dirtydiff = cv2.dilate(diff12, kernel, iterations=1)
    dirtydiff = cv2.erode(dirtydiff, kernel, iterations=1)

    combined_image = np.hstack((diff12, cleandiff,dirtydiff))

    # 显示拼接后的图像
    cv2.imshow('Combined Image', combined_image)

    # 等待按键，然后关闭窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()
