import cv2
image=cv2.imread('self.jpeg')
if image is not None:
    cv2.imshow('self image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("error")