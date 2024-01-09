import cv2

def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel_value = img[y, x]
        print(f"Location: ({x}, {y}), Pixel Value: {pixel_value}")

path = f'./../photo/photo1.jpg'
img = cv2.imread(path)
cv2.imshow('imshow_photo', img)
cv2.setMouseCallback('imshow_photo', onMouse)
cv2.waitKey(0)

cv2.destroyAllWindows() 