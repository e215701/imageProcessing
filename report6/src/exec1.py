import cv2
import numpy as np


def detect_clock_hands(image_path):
    # 画像を読み込む
    img = cv2.imread(image_path)
    output = img.copy()

    # グレースケールに変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ブラーを適用してノイズを減らす
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 二値化
    _, thresh = cv2.threshold(blurred, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    # エッジ検出
    edges = cv2.Canny(thresh, 50, 150, apertureSize=3)

    # 円の検出
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=400, param1=50, param2=30, minRadius=0, maxRadius=0)

    # 円が検出されたか確認
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # 円の中心を描画
            center = (i[0], i[1])
            cv2.circle(output, center, 1, (255, 0, 0), 3)
            # 円の外周を描画
            radius = i[2]
            cv2.circle(output, center, radius, (255, 0, 255), 3)

    # マスクを作成して円の中だけを残す
    mask = np.zeros_like(gray)
    cv2.circle(mask, center, radius, (255, 255, 255), -1)

    # マスクを適用したエッジ
    masked_edges = cv2.bitwise_and(edges, edges, mask=mask)

    # 針の検出（直線検出）
    lines = cv2.HoughLinesP(masked_edges, 1, np.pi / 180, threshold=50, minLineLength=radius * 0.5, maxLineGap=20)

    # 針を識別し、描画する
    if lines is not None:
        lines = sorted(lines, key=lambda x: np.hypot((x[0][2] - x[0][0]), (x[0][3] - x[0][1])), reverse=True)
        # 最も長い直線を長針とする
        longest_line = lines[0][0]
        cv2.line(output, (longest_line[0], longest_line[1]), (longest_line[2], longest_line[3]), (0, 255, 0), 2)
        # 次に長い直線を短針とする
        if len(lines) > 1:
            second_longest_line = lines[1][0]
            cv2.line(output, (second_longest_line[0], second_longest_line[1]), (second_longest_line[2], second_longest_line[3]), (0, 0, 255), 2)

    # 画像を保存
    cv2.imwrite('detected_clock_hands.jpg', output)
    cv2.imshow('detected_clock_hands.jpg', output)
    cv2.waitKey(0) #待機時間、ミリ秒指定、０の場合はボタンが押されるまで待機

    cv2.destroyAllWindows()  # 全てのウィンドウを一度に破棄
    # 結果を返す
    return 'detected_clock_hands.jpg'

# 画像のパスを指定して関数を呼び出す
detect_clock_hands('./../images/clock1.jpg')