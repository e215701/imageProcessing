import cv2

path = f'./../photo/photo1.jpg'
img = cv2.imread(path)

print(img.shape)