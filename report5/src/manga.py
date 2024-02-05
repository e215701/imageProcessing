# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 漫画化フィルタ
def manga_filter(src, screen, th1=60, th2=150):
    
    # グレースケール変換
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    # スクリーントーン画像を入力画像と同じ大きさにリサイズ
    screen = cv2.resize(screen,(gray.shape[1],gray.shape[0]))

    # Cannyアルゴリズムで輪郭検出し、色反転
    edge = 255 - cv2.Canny(gray, 80, 120)

    # 三値化
    gray[gray <= th1] = 0
    gray[gray >= th2] = 255
    gray[ np.where((gray > th1) & (gray < th2)) ] = screen[ np.where((gray > th1)&(gray < th2)) ]

    # 三値画像と輪郭画像を合成
    return cv2.bitwise_and(gray, edge)


# 入力画像とスクリーントーン画像を取得
img = cv2.imread("./../images/fig1.jpeg")
screen = cv2.imread("./../images/screen.png")
    
# 画像の漫画化
manga = manga_filter(img, screen, 70, 140)

# 結果を出力
cv2.imwrite("./../output/manga.jpeg", manga)

# テキストを追加
font = cv2.FONT_HERSHEY_SIMPLEX
text = "Blue Devils"
org = (50, manga.shape[0] - 30) # 画像の左下に配置
font_scale = 4
color = (255, 0, 0) # 青色
thickness = 8
line_type = cv2.LINE_AA

cv2.putText(manga, text, org, font, font_scale, color, thickness, line_type)

# 結果を出力
cv2.imwrite("./../output/manga2.jpeg", manga)