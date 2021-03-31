import cv2
import numpy as np


def detect_color(img, Threshold=0.01):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # lower mask (0-10)
    lower_red = np.array([0, 70, 50])
    upper_red = np.array([10, 255, 255])
    mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

    # upper mask (170-180)
    lower_red1 = np.array([170, 70, 50])
    upper_red1 = np.array([180, 255, 255])
    mask1 = cv2.inRange(img_hsv, lower_red1, upper_red1)

    # defining the Range of yellow color
    lower_yellow = np.array([21, 39, 64])
    upper_yellow = np.array([40, 255, 255])
    mask2 = cv2.inRange(img_hsv, lower_yellow, upper_yellow)

    # defining the Range of green color
    lowew_green = np.array([41, 52, 72])
    upper_green = np.array([102, 255, 255])
    mask3 = cv2.inRange(img_hsv, lowew_green, upper_green)

    # red pixels' mask
    mask_red = mask0 + mask1
    mask_yellow = mask2
    mask_green = mask3

    # Compare the percentage
    rate_red = np.count_nonzero(mask_red) / (img.shape[0] * img.shape[1])
    rate_yellow = np.count_nonzero(mask_yellow) / (img.shape[0] * img.shape[1])
    rate_green = np.count_nonzero(mask_green) / (img.shape[0] * img.shape[1])
    rates = [rate_red, rate_yellow, rate_green]
    colors = ['red', 'yellow', 'green']
    rate_max = max(rates)

    if rate_max > Threshold:
        return colors[rates.index(rate_max)]
    else:
        return 'unknown'
