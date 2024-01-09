import numpy as np
import cv2

# 画像を読み込む
img_origin = cv2.imread('./../photo/p1.jpeg')

# 色の反転
img = cv2.bitwise_not(img_origin)

# 画像のグレースケール化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 画像の白黒2値化
ret, img_binary = cv2.threshold(gray, 150, 255,cv2.THRESH_BINARY)

# 輪郭を抽出する
contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
img_contour = cv2.drawContours(img_origin, contours, -1, (0, 255, 0), 5)

# 画像を保存
cv2.imwrite('./../output_images/contour.jpeg', img_contour)