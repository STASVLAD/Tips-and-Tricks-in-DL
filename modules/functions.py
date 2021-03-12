import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


def img_show(img):
    plt.figure(dpi=150)
    plt.axis('off')
    plt.imshow(img)
    plt.show()
