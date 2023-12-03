from matplotlib import pyplot as plt
from pathlib import Path
import numpy as np

if __name__ == "__main__":
    img_path = Path("../medias/test.jpg")
    img = plt.imread(img_path)
    region_select = np.copy(img)
    left_bottom = [0, 539]
    right_bottom = [900, 539]
    apex = [400, 0]
    fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
    fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
    fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)
    XX, YY = np.meshgrid(np.arange(0, img.shape[1]), np.arange(0, img.shape[0]))
    region_thresholds = (YY > (XX * fit_left[0] + fit_left[1])) \
                      & (YY > (XX * fit_right[0] + fit_right[1])) \
                      & (YY < (XX * fit_bottom[0] + fit_bottom[1]))
    region_select[region_thresholds] = [255, 0, 0]
    fig, ax = plt.subplots(1, 2, figsize = (10, 3))
    ax[0].imshow(img)
    ax[1].imshow(region_select)
    plt.show()