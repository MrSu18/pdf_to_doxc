import cv2
import time

cap = cv2.VideoCapture(0)  # 打开摄像头
cap.set(3,640)# width=640
cap.set(4, 480)# height=480

fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # 视频编解码器
fps = cap.get(cv2.CAP_PROP_FPS)  # 帧数
width, height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 宽高
out = cv2.VideoWriter('result.mp4', fourcc, fps, (width, height))  # 写入视频

begin_cap=0

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # 把围绕Y轴翻转的图像
    if ret == True:
        if begin_cap == 1:
            out.write(frame)  # 写入帧
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # q退出
            break
        elif cv2.waitKey(1) & 0xFF == ord('r'):  # r开始录制
            begin_cap=1
            print('开始录制')
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

