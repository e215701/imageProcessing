import numpy as np
import cv2

def gammaCurve(frame, gamma = 1):
    look_up_table = np.zeros((256,1), dtype = 'uint8')
    for i in range(256):
        look_up_table[i][0] = pow(i / 255, 1 / gamma) * 255
    return cv2.LUT(frame, look_up_table)

# 画像を読み込む
image = cv2.imread('./../photo/gs.jpeg')

# ガンマ値を設定
gamma = 3.0

# ガンマ補正を適用
corrected_image = gammaCurve(image, gamma)

# 結果を保存
cv2.imwrite('./../output_images/gamma_corrected_gs.jpg', corrected_image)