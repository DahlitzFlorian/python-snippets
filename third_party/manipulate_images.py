import imageio
import numpy as np
import scipy.ndimage


start_img = imageio.imread(
    "http://static.cricinfo.com/db/PICTURES/CMS/263600/263697.20.jpg"
)
gray_inv_img = 255 - np.dot(start_img[..., :3], [0.299, 0.587, 0.114])
blur_img = scipy.ndimage.filters.gaussian_filter(inverted_img, sigma=5)


def dodge(front, back):
    result = front * 255 / (255 - back)
    result[np.logical_or(result > 255, back == 255)] = 255
    return result.astype("uint8")


final_img = dodge(blur_img, gray_img)
