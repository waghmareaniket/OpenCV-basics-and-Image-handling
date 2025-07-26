import cv2
image=cv2.imread("self.jpeg")
if image is not None:
    h,w,c=image.shape
    print(f"image dimension:\nheight:{h} \nweight:{w} \nColor:{c} ")
else:
    print('error image not see')    