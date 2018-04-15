import face_recognition
import cv2
import time

# 载入程序的目录下自己的人脸图片并encoding
me_image = face_recognition.load_image_file("0.jpg")
me_face_encoding = face_recognition.face_encodings(me_image)[0]
known_face_encodings = [me_face_encoding, ]


# 检测摄像头传来的图片中是否包含自己，是则返回True
def detect_self(img):
    # Resize frame of video to 1/4 size for faster face recognition processing
    # 缩小图片尺寸，加快速度
    small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    # BGR格式 TO RGB格式
    rgb_small_frame = small_frame[:, :, ::-1]

    # 获得图片中人脸的位置list
    face_locations = face_recognition.face_locations(rgb_small_frame)
    # 若检测到人脸
    if face_locations:
        # 获得检测到的人脸encoding list
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        for face_encoding in face_encodings:
            # known_face_encodings 中是否存在face_encoding 并返回一个对应的True/False的list
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            if True in matches:
                # 匹配到本人
                print("Welcome!")
                return True
            else:
                # 非本人
                return False


def main():
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read()
        # 将图像与y轴对称
        frame = cv2.flip(frame, 1)

        if not detect_self(frame):
            # 非本人，开启十秒录像
            # 定义解码器并创建VideoWrite对象
            # linux: XVID、X264; windows:DIVX
            # 20.0指定一分钟的帧数
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            filename = '/home/xianzhixianzhixian/ ' + str(int(time.time())) + ".avi"
            out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))
            now = time.time()
            while True:
                if (time.time() - now) < 10:
                    ret2, frame2 = video_capture.read()
                    frame2 = cv2.flip(frame2, 1)
                    out.write(frame2)
                else:
                    print("ending.,.")
                    video_capture.release()
                    cv2.destroyAllWindows()
                    exit(1)
        else:
            exit(1)

    print("ending.,.")
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()