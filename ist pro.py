import cv2
img = cv2.imread("C:/Users/Lenovo/Downloads/img.png")
#cv2.imwrite("C:/Users/Lenovo/Downloads/imgcopy1.jpg",img)
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("C:/Users/Lenovo/Downloads/imgcopy2.jpg",grayImg)
cv2.imshow("grayimg",grayImg)
#cv2.imshow("orig",img)
cv2.waitKey(0)
cv2.destroyAllWindow()
