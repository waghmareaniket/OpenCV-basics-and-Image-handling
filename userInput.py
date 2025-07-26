import cv2
image_path=input('enter the path of image')
image=cv2.imread(image_path)
if image is None:
    print("image is not ")
else:
    print("image is here")
    cv2.imshow("your_image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    save_path=input("enter new path to save file")
    cv2.imwrite(save_path,image)
    print(f'image saved{save_path}')