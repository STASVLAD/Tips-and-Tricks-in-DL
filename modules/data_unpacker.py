import os
import cv2 as cv

def video_unpacker(path, delete_after=False): 
    ''' path - путь к видосу, 
    эту функцию можно будет потом циклом проделать над несколькими видео
    delete_after допишу, если нужно будет удалять ориг видео'''
    folder = os.path.splitext(path)[0]
    try:
        os.mkdir(folder)
    except FileExistsError:
        pass

    video = cv2.VideoCapture(path)
    lenght = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    
    for image in range(lenght):
        _, frame = video.read()
        name = f'frame_{image}.jpg'
        cv2.imwrite(os.path.join(folder, name), frame)
