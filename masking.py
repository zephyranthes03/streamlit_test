import cv2
import os
import argparse # for command args

###
# pipx run --spec opencv-python python masking.py [source file path]
###

def process_video(input_file:str, min_face_size_ratio:float=0.05):

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # 비디오 읽기
    file_name, file_extension = os.path.splitext(input_file)  # 파일 이름과 확장자 분리

    # 확장자에 따라 코덱 선택
    if file_extension.lower() == ".avi":
        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # AVI용 코덱
    elif file_extension.lower() == ".mpg":
        fourcc = cv2.VideoWriter_fourcc(*'PIM1')  # MPEG-1 코덱
    elif file_extension.lower() == ".mkv":
        fourcc = cv2.VideoWriter_fourcc(*'X264')  # MKV용 코덱
    else:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 기본 코덱 (MP4)


d

    # 비디오 읽기
    cap = cv2.VideoCapture(input_file)

    # 출력 파일 설정
    output_file = f"{file_name}_processed{file_extension}"

    # 비디오 저장 설정 (코덱, FPS, 프레임 크기)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 코덱 설정
    out = cv2.VideoWriter(output_file, fourcc, cap.get(cv2.CAP_PROP_FPS), 
                        (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    frame_count = 0
    detect_interval = 10  # 매 10 프레임마다 얼굴 재탐지


    while True:
        ret, frame = cap.read()
        if not ret:
            break

    # scaleFactor: 얼굴 크기 변화에 따른 스케일 조정 값으로, 이 값을 조정해 얼굴 탐지 정확도를 높입니다.
    # minNeighbors: 얼굴 인식 신뢰도를 설정하며, 값이 높을수록 정확도가 올라가지만 탐지율이 줄어들 수 있습니다.
    # minSize: 탐지할 최소 얼굴 크기를 설정해 작은 불필요한 객체를 무시할 수 있습니다.
        # 얼굴 탐지 최적화
        if frame_count % detect_interval == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # 얼굴에 블러 처리
        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            face = cv2.GaussianBlur(face, (99, 99), 30)
            frame[y:y+h, x:x+w] = face


        # # 프레임의 가로와 세로 크기 가져오기
        # frame_height, frame_width = frame.shape[:2]

        # # 작은 얼굴에만 블러 처리
        # for (x, y, w, h) in faces:
        #     # 얼굴의 크기 비율 계산
        #     face_size_ratio = (w * h) / (frame_width * frame_height)

        #     # 특정 크기 이하(작은 얼굴)에만 블러 적용
        #     if face_size_ratio < min_face_size_ratio:
        #         face = frame[y:y+h, x:x+w]
        #         face = cv2.GaussianBlur(face, (99, 99), 30)
        #         frame[y:y+h, x:x+w] = face




        # 파일에 저장하거나 화면에 출력
        out.write(frame)

        # 블러 결과를 보는 코드
        # cv2.imshow("Blurred Video", frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

        frame_count += 1

    cap.release()
    out.release()  # 파일 저장 종료
    return output_file

# 블러 재생 창을 닫는 코드.
#cv2.destroyAllWindows()

# 커맨드 라인 인수를 위한 설정
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Apply face blur to a video file.")
    parser.add_argument("input_file", type=str, help="Path to the input video file")
    args = parser.parse_args()
    output_file = process_video(args.input_file, min_face_size_ratio=0.1)

    print(f"Processed video saved as {output_file}")
