import cv2
import numpy as np

# 画像の読み込み
image = cv2.imread('./../photo/p5.jpeg')  # 画像のファイル名を指定

# ガウシアンぼかしフィルタの適用
blurred = cv2.GaussianBlur(image, (0, 0), sigmaX=1.5)

# 鮮鋭化フィルタの強度を変更しながら適用
sharpened = cv2.addWeighted(image, 3.5, blurred, -1.5, 0)

# 画像を保存
cv2.imwrite('./../output_images/clear_filter.jpeg', sharpened)