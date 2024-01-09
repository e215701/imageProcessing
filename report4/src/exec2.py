import cv2
from matplotlib import pyplot as plt

path = './../images/building.jpg'                                               # 画像のパス
i = cv2.imread(path,0)
th = 127                                                        # 閾値
i_max = 255                                                     # 最大輝度値
ret, i_binary = cv2.threshold(i, th, i_max, cv2.THRESH_BINARY)   # 二値化処理

cv2.imwrite('./../output_images/binary_image2.jpg', i_binary)

cv2.imshow('binary_image', i_binary)
# cv2.imshow('Original', image_copy1)
cv2.waitKey(0)
cv2.destroyAllWindows()