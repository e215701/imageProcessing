import cv2
import numpy as np

def detect_hands(image_path):
    # 画像を読み込む
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # エッジ検出
    edges = cv2.Canny(blurred, 50, 150, apertureSize=3)

    # 円の検出（時計の顔）
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # 円の中心点
            center = (i[0], i[1])

            # 針の検出
            lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)
            if lines is not None:
                for line in lines:
                    x1, y1, x2, y2 = line[0]
                    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow('Detected Hands', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 画像のパスを指定して関数を呼び出す
detect_hands('./../images/clock3.jpg')
