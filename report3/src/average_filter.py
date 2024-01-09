import cv2
import numpy as np

# 画像の読み込み
image = cv2.imread('./../photo/p4.jpeg')  # 画像のファイル名を指定

# 加重平均化フィルタ（3x3）のカーネル
weighted_kernel_3x3 = np.array([[1, 4, 1],
                                [4, 12, 4],
                                [1, 4, 1]]) / 32.0

# 加重平均化フィルタ（5x5）のカーネル
weighted_kernel_5x5 = np.array([[1, 4, 6, 4, 1],
                                [4, 16, 24, 16, 4],
                                [6, 24, 36, 24, 6],
                                [4, 16, 24, 16, 4],
                                [1, 4, 6, 4, 1]]) / 256.0

# 通常の平均化フィルタ（3x3）
average_kernel_3x3 = np.ones((3, 3), dtype=np.float32) / 9.0

# 通常の平均化フィルタ（5x5）
average_kernel_5x5 = np.ones((5, 5), dtype=np.float32) / 25.0

# フィルタを画像に適用
weighted_3x3_result = cv2.filter2D(image, -1, weighted_kernel_3x3)
weighted_5x5_result = cv2.filter2D(image, -1, weighted_kernel_5x5)
average_3x3_result = cv2.filter2D(image, -1, average_kernel_3x3)
average_5x5_result = cv2.filter2D(image, -1, average_kernel_5x5)

# 画像を保存
cv2.imwrite('./../output_images/exec5/Weighted_3x3.jpeg', weighted_3x3_result)
cv2.imwrite('./../output_images/exec5/Weighted_5x5.jpeg', weighted_5x5_result)
cv2.imwrite('./../output_images/exec5/Average_3x3.jpeg', average_3x3_result)
cv2.imwrite('./../output_images/exec5/Average_5x5.jpeg', average_5x5_result)