import cv2

path = f'./../photo/photo1.jpg'
img = cv2.imread(path)

cv2.imshow('imshow_photo', img)  #画像を描画
cv2.waitKey(0) #待機時間、ミリ秒指定、０の場合はボタンが押されるまで待機

cv2.destroyAllWindows()  # 全てのウィンドウを一度に破棄