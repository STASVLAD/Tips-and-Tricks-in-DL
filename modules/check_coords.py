import numpy as np


def check_coords(past, future, box_delta=20):
    '''
    Проверяет боксы на разницу в координатах
    Разница задается параметром box_delta 
    '''
    if future is None or past is None:
        return None
    for i in range(len(past)):
        if np.abs(past[i] - future[i]) > box_delta:
            return False
    return True
