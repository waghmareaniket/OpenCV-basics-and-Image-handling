import cv2
image=cv2.imread('Self.jpeg')
if image is None:
    print("image not show")
else:
    print("image is show")