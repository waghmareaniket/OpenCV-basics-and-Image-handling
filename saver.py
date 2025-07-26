import cv2
image=cv2.imread('Self.jpeg')
if image is not None:
    savers=cv2.imwrite('selfImg.jpg',image)
    if savers:
        print("image is saved as selfImg name")
    else:
        print("image not saved")
else:
    print("error img not see")    