from matplotlib import pyplot as plt
from pathlib import Path
import numpy as np

if __name__ == "__main__":
    img_path = Path("../medias/test.jpg")
    img = plt.imread(img_path)
    image_selection = np.copy(img)

    # Color thresholding
    red_threshold = 220
    green_threshold = 220
    blue_threshold = 220
    rgb_threshold = [red_threshold, green_threshold, blue_threshold]
    color_thresholds = (img[:, :, 0] < rgb_threshold[0]) \
                     | (img[:, :, 1] < rgb_threshold[1]) \
                     | (img[:, :, 2] < rgb_threshold[2])
    
    # Region thresholding
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
    image_selection[~color_thresholds & region_thresholds] = [255, 0, 0]

    # Plot
    fig, ax = plt.subplots(1, 2, figsize = (10, 3))
    ax[0].imshow(img)
    ax[1].imshow(image_selection)
    plt.show()