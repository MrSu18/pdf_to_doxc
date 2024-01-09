import cv2

def video2images(Video_Dir):
    """
    function: video to pictures
    author: AIJun
    date:2021/3/17
    """
    cap = cv2.VideoCapture(Video_Dir)
    c = 1  # 帧数起点
    index = 1  # 图片命名起点，如1.jpg

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        # 逐帧捕获
        ret, frame = cap.read()
        # 如果正确读取帧，ret为True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        if c % 10 == 0:
            cv2.imwrite('E:/nodeanddata/Python/Gesture_Detect/train/images/biu_3_' + str(index) + '.jpg', frame)
            index += 1
        c += 1
        cv2.waitKey(1)
        # 按键停止
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()

Video_Dir = "E:/nodeanddata/Python/OpenCV/Video_To_Image/result.mp4"
video2images(Video_Dir)

