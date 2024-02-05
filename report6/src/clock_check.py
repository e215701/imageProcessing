import cv2
import numpy as np
import math

def detect_and_save_largest_clock(image_path, output_path):
    # 画像を読み込む
    image = cv2.imread(image_path)

    # グレースケールに変換
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # ぼかしを適用してノイズを軽減
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # エッジ検出
    edges = cv2.Canny(blurred, 50, 150)

    # 輪郭を検出
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 面積が大きい1つの長方形（矩形）を取得
    rectangles = [cv2.boundingRect(contour) for contour in contours]
    rectangles = sorted(rectangles, key=lambda x: x[2] * x[3], reverse=True)[:1]

    # 長方形（矩形）の検出と時刻推定
    for rect in rectangles:
        # 長方形（矩形）を描画
        x, y, w, h = rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 長方形（矩形）の中心を利用して時刻を推定
        rect_center = (x + w // 2, y + h // 2)
        time_estimation = estimate_time_within_rectangle(rect_center, image.shape[:2], rect)
        print("推定時刻 (長方形):", time_estimation)

        # 推定時刻を画像に描画
        font = cv2.FONT_HERSHEY_SIMPLEX
        if w > h:
            font_scale = int(w//140)
        else:
            font_scale = int(h//290)
        font_thickness = 2
        text_position = (20, 50)
        text_color = (0, 0, 0)
        text = f"Estimated Time: {time_estimation}"
        cv2.putText(image, text, text_position, font, font_scale, text_color, font_thickness)

    # 結果を保存
    cv2.imwrite(output_path, image)

    # 結果を表示
    cv2.imshow('Detected Clock', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def estimate_time_within_rectangle(center, image_shape, rectangle):
    # 長方形の中心座標を取得
    rectangle_center = ((rectangle[0] + rectangle[2]) // 2, (rectangle[1] + rectangle[3]) // 2)

    # 中心からの角度を計算
    angle_rad = math.atan2(center[1] - rectangle_center[1], center[0] - rectangle_center[0])

    # ラジアンを度に変換
    angle_deg = math.degrees(angle_rad)
    # 時刻の推定
    if 50 > int(angle_deg) >= 40:
        hours = (int(angle_deg % 30) % 12) + 3
        minutes = (int((angle_deg // 30) * 5)) + 34
    elif 40 > int(angle_deg) >= 30 or int(angle_deg) >= 50:
        hours = (int(angle_deg % 30) % 12) + 1
        minutes = (int((angle_deg // 30) * 5)) + 3
    else:
        hours = (int(angle_deg % 30) % 12) - 1
        minutes = (int((angle_deg // 30) * 5))
    
    return f"{hours:02d}:{minutes:02d}"

# 画像のパスと保存先のパスを指定して処理を実行
image_number = input("画像のパスを入力してください: ")
if image_number == "1":
    image_path = './../images/clocks/clock1.jpg'
    output_path = './../output/detected_clock1.jpg'
elif image_number == "2":
    image_path = './../images/clocks/clock2.jpg'
    output_path = './../output/detected_clock2.jpg'
elif image_number == "3":
    image_path = './../images/clocks/clock3.jpg'
    output_path = './../output/detected_clock3.jpg'
elif image_number == "4":
    image_path = './../images/clocks/clock4.jpg'
    output_path = './../output/detected_clock4.jpg'

detect_and_save_largest_clock(image_path, output_path)