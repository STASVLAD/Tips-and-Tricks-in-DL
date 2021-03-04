import os
import cv2 


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


def video_packer(path, delete_after=False):
    img_array = []
    for root, dir, files in os.walk(path):
        for filename in files:
            img = cv2.imread(os.path.join(root, filename))
            height, width, layers = img.shape
            size = (width,height)
            img_array.append(img) 
    out = cv2.VideoWriter(path + 'project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()