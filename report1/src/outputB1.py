import cv2

for i in range(1,10):
    path = f'./../photo/photo{i}.jpeg'
    img = cv2.imread(path)
    cv2.imshow('imshow_photo', img)
    cv2.waitKey(5000) #今回は５秒ごとに画像が切り替わる

cv2.destroyAllWindows() # 全てのウィンドウを一度に破棄