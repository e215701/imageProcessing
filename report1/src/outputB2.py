import cv2

for i in range(1,10):
    path = f'./../photo/photo{i}.jpeg'
    img = cv2.imread(path)

    window_name = f'imshow_photo{i}'
    cv2.imshow(window_name, img)
    # ウィンドウの位置を変更
    if i <= 4:
        cv2.moveWindow(window_name, 325*(i-1), 0)  
    elif i <= 8:
        cv2.moveWindow(window_name, 325*(i-5), 200)
    else:
        cv2.moveWindow(window_name, 325*(i-9), 400)

cv2.waitKey(0) #０にすることで各画像が消えないようにしている。
cv2.destroyAllWindows() # 全てのウィンドウを一度に破棄