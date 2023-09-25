import cv2
import numpy as np

# 打开视频文件
video_capture = cv2.VideoCapture("output.avi")

# 创建窗口
cv2.namedWindow('All in One', cv2.WINDOW_NORMAL)

while True:
    # 读取视频帧
    ret, frame = video_capture.read()
    if not ret:
        break

    # 转换为灰度图像
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Canny边缘检测
    canny_frame = cv2.Canny(gray_frame, 100, 200)

    # 获取窗口的大小
    height, width, _ = frame.shape

    # 将窗口分成三个部分
    third_width = width // 3
    third_height = height

    # 定义ROI
    roi1 = frame[0:third_height, 0:third_width]
    roi2 = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)
    roi3 = cv2.cvtColor(canny_frame, cv2.COLOR_GRAY2BGR)

    # 将每个ROI的宽度和高度都设置为相等的第三宽度和第三高度
    roi1 = cv2.resize(roi1, (third_width, third_height))
    roi2 = cv2.resize(roi2, (third_width, third_height))
    roi3 = cv2.resize(roi3, (third_width, third_height))

    # 将ROI组合成一个图像
    combined_frame = np.hstack((roi1, roi2, roi3))

    # 动态计算文本位置
    text_height = 30  # 文本的高度位置
    text_thickness = 2  # 文本的线条厚度
    text_scale = 1  # 文本的缩放
    text_color = (255, 255, 255)  # 文本颜色

    # 计算每个文本的位置，确保它们位于各自的部分中央
    text1_x = third_width // 2 - 50
    text2_x = third_width + third_width // 2 - 40
    text3_x = 2 * third_width + third_width // 2 - 50

    # 在"All in One"窗口中显示组合图像并添加文本标签
    cv2.putText(combined_frame, 'Original', (text1_x, text_height), cv2.FONT_HERSHEY_SIMPLEX, text_scale, text_color, text_thickness)
    cv2.putText(combined_frame, 'Gray', (text2_x, text_height), cv2.FONT_HERSHEY_SIMPLEX, text_scale, text_color, text_thickness)
    cv2.putText(combined_frame, 'Canny', (text3_x, text_height), cv2.FONT_HERSHEY_SIMPLEX, text_scale, text_color, text_thickness)

    # 在"All in One"窗口中显示组合图像
    cv2.imshow('All in One', combined_frame)

    # 按下'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源并销毁窗口
video_capture.release()
cv2.destroyAllWindows()
