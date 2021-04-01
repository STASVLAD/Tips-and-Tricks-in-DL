def area_check(box, img_size=(1920, 1080), x_bound=0.15, y_bound=0.65):
    assert len(box) == 4
    

    x_thr = x_bound * img_size[0]
    y_thr = y_bound * img_size[1]
    
    if (box[0] < x_thr or box[2] > (img_size[0] - x_thr)) or box[3] > y_thr:
        return False       
    else:
        return True
