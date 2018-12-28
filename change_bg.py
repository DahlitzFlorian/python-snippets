import cv2
import numpy as np


img = cv2.imread(open(""))

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if all(img[i][j] == np.array([114,89,47])):
            img[i][j] = np.array([200,0,0])

cv2.imwrite("new.jpg", img)
