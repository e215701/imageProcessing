import numpy as np
import cv2
from matplotlib import pyplot as plt
 
# 画像から輪郭を検出する関数
def contours(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                  # グレースケール化
    ret, img_binary = cv2.threshold(img_gray,                         # 二値化
                                    60, 255,                          # 二値化のための閾値60(調整要)
                                    cv2.THRESH_BINARY)
    contour_list, hierarchy = cv2.findContours(img_binary,            # 輪郭検出
                                           cv2.RETR_LIST,             # 外側の輪郭のみ抽出
                                           cv2.CHAIN_APPROX_SIMPLE)
    contours_array = [np.array(contour) for contour in contour_list]  # 輪郭情報をndarrayに変換
    x = np.mean(contours_array[0].T[0, 0])                            # 輪郭のx方向平均値を算出
    y = np.mean(contours_array[0].T[1, 0])                            # 輪郭のy方向平均値を算出
    return x, y

movie = cv2.VideoCapture('./../movies/testmovie1.avi')                # 動画ファイルの読み込み

# 動画ファイル保存用の設定
fps = int(movie.get(cv2.CAP_PROP_FPS))                                # 動画のFPSを取得
w = int(movie.get(cv2.CAP_PROP_FRAME_WIDTH))                          # 動画の横幅を取得
h = int(movie.get(cv2.CAP_PROP_FRAME_HEIGHT))                         # 動画の縦幅を取得
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')                   # 動画保存時のfourcc設定（mp4用）
video = cv2.VideoWriter('./../output_movies/tracking_video.mp4', fourcc, fps, (w, h), True)   # 動画の仕様（ファイル名、fourcc, FPS, サイズ, カラー）
 
# ファイルからフレームを1枚ずつ取得して動画処理後に保存する
x_list = []
y_list = []
while True:
    ret, frame = movie.read()                                         # フレームを取得
 
    # フレームが取得できない場合はループを抜ける
    if not ret:
        break
 
    x, y = contours(frame)                                            # 輪郭検出から物体中心を算出
 
    # 検出された位置に矢印を描画
    start_point = (int(x)+30, int(y)+30)  # 矢印の始点
    end_point = (int(x) + 0, int(y) + 0)  # 矢印の終点 (例：始点から右下に50ピクセル)
    arrow_color = (0, 255, 0)  # 矢印の色 (緑)
    thickness = 3  # 矢印の太さ

    # 検出された位置にテキストを描画
    font = cv2.FONT_HERSHEY_SIMPLEX  # フォントの種類
    text_position = (int(x)+40, int(y)+45) # テキストを表示する位置
    font_scale = 1                   # フォントサイズ
    font_color = (0, 255, 0)         # フォントの色 (緑)
    line_type = 2                    # 線の太さ


    frame = cv2.arrowedLine(frame, start_point, end_point, arrow_color, thickness)
    frame = cv2.putText(frame, 'Object', text_position, font, font_scale, font_color, line_type)


 
    video.write(frame)  # 動画を保存する
    x_list.append(x)
    y_list.append(y)
 
# 動画オブジェクト解放
movie.release()