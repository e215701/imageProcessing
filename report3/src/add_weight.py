import cv2

# １つ目の画像の重みの値
alpha = 0.8

# 画像を読み込む
src1 = cv2.imread('./../photo/p1.jpeg') # 1つ目の画像
src2 = cv2.imread('./../photo/p2.jpeg') # 2つ目の画像

# "SRC"２を"SRC"１と同じサイズにリサイズ
src2_resized = cv2.resize(src2, (src1.shape[1], src1.shape[0]))

# 画像を合成する
# 単純平均で画像間演算
img1 = cv2.addWeighted(src1, 0.5, src2_resized, 0.5, 0.0)

# 画像を合成する
beta = 1.0 - alpha # "２つ目の画像の重みの値, 
img2 = cv2.addWeighted(src1, alpha, src2_resized, beta, 0.0)

# 合成した画像を保存する
cv2.imwrite('./../output_images/add_average.jpeg', img1)
cv2.imwrite('./../output_images/add_a.jpeg', img2)