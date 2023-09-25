import cv2

# 打开AVI视频文件
cap = cv2.VideoCapture('2.avi')

# 创建窗口
cv2.namedWindow('Video Frame', cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()

    # 检查视频是否结束
    if not ret:
        break

    # 在窗口中显示帧
    cv2.imshow('Video Frame', frame)

    frame_rate = 30  # 设置视频的帧速率（例如30帧/秒）

    # 在等待时间中使用帧速率来控制显示时长
    if cv2.waitKey(int(1000 / frame_rate)) & 0xFF == ord('q'):
        break

# 释放视频捕捉对象和关闭窗口
cap.release()
cv2.destroyAllWindows()
