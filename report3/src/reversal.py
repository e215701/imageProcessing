import cv2

img = cv2.imread('./../photo/p2.jpeg')

img_flip_lr = cv2.flip(img, 1)
cv2.imwrite('./../output_images/reversal.jpeg', img_flip_lr)