import face_recognition
import cv2
import datetime

class Face:

    # 载入程序的目录下自己的人脸图片并encoding
    me_image = face_recognition.load_image_file("/home/xianzhixianzhixian/图片/摄像头/0.jpg")
    me_face_encoding = face_recognition.face_encodings(me_image)[0]
    known_face_encodings = [me_face_encoding, ]

    #比较是否为本人
    @staticmethod
    def detect_self(img):
        # 缩小图片尺寸，加快速度
        small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        # BGR格式 TO RGB格式
        rgb_small_frame = small_frame[:, :, ::-1]

        # 获得图片中人脸的位置list
        face_locations = face_recognition.face_locations(rgb_small_frame)
        # 若检测到人脸
        if face_locations:
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(Face.known_face_encodings, face_encoding)
                if True in matches:
                    # 匹配到本人
                    return True
                else:
                    # 非本人
                    return False

    #从照相机中获取照片
    @staticmethod
    def getImageResult():
        now = datetime.datetime.now()
        cap = cv2.VideoCapture(0)
        while (True):
            #读取摄像头输入的视频流
            ret, frame = cap.read()
            #显示摄像头视频
            cv2.imshow("capture", frame)
            #每秒刷新一次
            cv2.waitKey(1)

            if (datetime.datetime.now() - now).seconds > 5:
                # 读取摄像头输入的视频流
                ret, frame = cap.read()
                # 将图像与y轴对称
                frame = cv2.flip(frame, 1)
                if(Face.detect_self(frame)):
                    cap.release()
                    cv2.destroyAllWindows()
                    return True
                else:
                    cap.release()
                    cv2.destroyAllWindows()
                    return False