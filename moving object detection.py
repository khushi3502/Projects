import cv2#import the open cv
import time#time library
import imutils#resizing library
cam = cv2.VideoCapture(0)#initialize he camera
time.sleep(1)# 1 second delay
firstFrame=None # initializing there  are no object
area = 500# threshold area
while True:#infinite loop
    _,img = cam.read()#read the frame of the camera
    text = "Normal"#initialize the text as normal
    img = imutils.resize(img,width=500)#resize the image
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#convert color to gray scale
    gaussianImg = cv2.GaussianBlur(grayImg,(21,21),0)#smoothening
    if firstFrame is None:
        firstFrame=gaussianImg
        continue
    imgDiff = cv2.absdiff(firstFrame,gaussianImg) #subracting current frame from gaussian frame
    threshImg = cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1]#threshold
    treshImg = cv2.dilate(threshImg,None,iterations=2)#remove the holes
    cnts = cv2.findContours(threshImg.copy(),cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE) #covering upthe hole moving object
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c)< area:
            continue
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),2)
        text="MMOVING OBJECT DETECTED"
    print(text)
    cv2.putText(img,text,(10,20),
           cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.imshow("camerafeed",img)
    key=cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
    
    
