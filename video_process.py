import numpy
import cv2,time

video=cv2.VideoCapture(0)
first_frame=None
a=0
while True:
    a=a+1

    check,frame=video.read()


    print(check)
    print(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    if first_frame is None:
        first_frame=gray
        continue
    delta_frame=cv2.absdiff(first_frame,gray)
    thrersh=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    #thrersh=cv2.dilate(thrersh,None,iterations=2)

    (cnts,_)=cv2.findContours(thrersh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour)<1000:
            continue

        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("thresh",thrersh)
    cv2.imshow("blurres",gray)
    cv2.imshow("delta frame",delta_frame)
    cv2.imshow("color frame",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()
