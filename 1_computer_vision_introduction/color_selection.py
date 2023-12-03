from matplotlib import pyplot as plt
from pathlib import Path
import numpy as np

if __name__ == "__main__":
    img_path = Path("../medias/test.jpg")
    img = plt.imread(img_path)
    color_select = np.copy(img)
    red_threshold = 220
    green_threshold = 220
    blue_threshold = 220
    rgb_threshold = [red_threshold, green_threshold, blue_threshold]
    thresholds = (img[:, :, 0] < rgb_threshold[0]) \
                | (img[:, :, 1] < rgb_threshold[1]) \
                | (img[:, :, 2] < rgb_threshold[2])
    color_select[thresholds] = [0, 0, 0]
    fig, ax = plt.subplots(1, 2, figsize = (10, 3))
    ax[0].imshow(img)
    ax[1].imshow(color_select)
    plt.show()