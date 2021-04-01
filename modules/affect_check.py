def affect_check(x_l, x_r, img_size):
    x_thr_r = 0.6 * img_size[1]
    x_thr_l = 0.4 * img_size[1]
    if x_l >= x_thr_r or x_r <= x_thr_l:
        return True
    else:
        return False
