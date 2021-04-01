import cv2


def get_fps():
    video = cv2.VideoCapture('/content/video.mp4')
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()
    with open('/content/fps.txt', 'w') as fp:
        fp.write(str(fps))
