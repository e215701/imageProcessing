import cv2
import matplotlib.pyplot as plt

# 画像を読み込み
path = f'./../photo/photo1.jpg'
img = cv2.imread(path)

# ヒストグラムの作成（引数の'img'を[ ]で囲うことを忘れないで下さい）
b_histogram = cv2.calcHist([img], [0], None, [256], [0, 256])
g_histogram = cv2.calcHist([img], [1], None, [256], [0, 256])
r_histogram = cv2.calcHist([img], [2], None, [256], [0, 256])

# Matplotlibで表示するためにRGBの並びに変更する
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# ヒストグラムの可視化
plt.rcParams["figure.figsize"] = [12,3.8]                        
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.15, top=0.9) 
plt.subplot(121)                                                 
plt.imshow(rgb_img)                                            
plt.axis("off")                                                  
plt.subplot(122)                                                 
plt.plot(b_histogram, color='blue', label='blue')                
plt.plot(g_histogram, color='green', label='green')              
plt.plot(r_histogram, color='red', label='red')                  
plt.legend(loc=0)                                                
plt.xlabel('Brightness')                                         
plt.ylabel('Count')                                              
plt.show()                                                       