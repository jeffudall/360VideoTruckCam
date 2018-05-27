from imutils.video import VideoStream
from rotate import rotate_bound
import cv2
import time
import numpy as np
import imutils

height = 1000
width = 600

#truck = cv2.imread('truck3.tif', cv2.IMREAD_UNCHANGED)

x_offsett=80
y_offsett=50
y_offsetr1=140
x_offsetr1=250
x_offsetl1=120
y_offsetl1=140
x_offsetl2=120
y_offsetl2=345
y_offsetr2=345
x_offsetr2=250
x_offsetl3=120
y_offsetl3=550
y_offsetr3=550
x_offsetr3=250
x_offsetb=130
y_offsetb=755

anglef = 0
anglel1 = 270
anglel2 = 270
angler1 = 90
angler2 = 90
angleb = 180

leftStream1 = VideoStream(3).start()
rightStream1 = VideoStream(7).start()
backStream = VideoStream(0).start()
leftStream2 = VideoStream(4).start()
rightStream2 = VideoStream(2).start()
leftStream3 = VideoStream(1).start()
rightStream3 = VideoStream(5).start()
time.sleep(2.0)

ls = [0]*180

while True:
    
    imageCanvastruck = np.zeros((height, width, 4), np.uint8)
    imageCanvasl1 = np.zeros((height, width, 4), np.uint8)
    imageCanvasl2 = np.zeros((height, width, 4), np.uint8)
    imageCanvasr1 = np.zeros((height, width, 4), np.uint8)
    imageCanvasr2 = np.zeros((height, width, 4), np.uint8)
    imageCanvasl3 = np.zeros((height, width, 4), np.uint8)
    imageCanvasr3 = np.zeros((height, width, 4), np.uint8)
    imageCanvasb = np.zeros((height, width, 4), np.uint8)

    right1 = rightStream1.read()
    left1 = leftStream1.read()
    back = backStream.read()
    left2 = leftStream2.read()
    right2 = rightStream2.read()
    left3 = leftStream3.read()
    right3 = rightStream3.read()
    
    left1 = imutils.resize(left1, width=200)
    right1 = imutils.resize(right1, width=200)
    back = imutils.resize(back, width=200)
    left2 = imutils.resize(left2, width=200)
    right2 = imutils.resize(right2, width=200)
    left3 = imutils.resize(left3, width=200)
    right3 = imutils.resize(right3, width=200)
    
    left1 = rotate_bound(left1, anglel1)
    left2 = rotate_bound(left2, anglel2)
    right1 = rotate_bound(right1, angler1)
    right2 = rotate_bound(right2, angler2)
    right3 = rotate_bound(right3, angler2)
    left3 = rotate_bound(left3, anglel2)
    back = rotate_bound(back, angleb)
    
    #truck = cv2.cvtColor(truck, cv2.COLOR_BGR2BGRA)
    left1 = cv2.cvtColor(left1, cv2.COLOR_BGR2BGRA)
    left2 = cv2.cvtColor(left2, cv2.COLOR_BGR2BGRA)
    right1 = cv2.cvtColor(right1, cv2.COLOR_BGR2BGRA)
    right2 = cv2.cvtColor(right2, cv2.COLOR_BGR2BGRA)
    left3 = cv2.cvtColor(left3, cv2.COLOR_BGR2BGRA)
    right3 = cv2.cvtColor(right3, cv2.COLOR_BGR2BGRA)
    back = cv2.cvtColor(back, cv2.COLOR_BGR2BGRA)
    
    #imageCanvastruck[y_offsett:y_offsett+truck.shape[0], x_offsett:x_offsett+truck.shape[1]] = truck
    imageCanvasl1[y_offsetl1:y_offsetl1+left1.shape[0], x_offsetl1:x_offsetl1+left1.shape[1]] = left1
    imageCanvasl2[y_offsetl2:y_offsetl2+left2.shape[0], x_offsetl2:x_offsetl2+left2.shape[1]] = left2
    imageCanvasl3[y_offsetl3:y_offsetl3+left3.shape[0], x_offsetl3:x_offsetl3+left3.shape[1]] = left3
    imageCanvasr1[y_offsetr1:y_offsetr1+right1.shape[0], x_offsetr1:x_offsetr1+right1.shape[1]] = right1
    imageCanvasr2[y_offsetr2:y_offsetr2+right2.shape[0], x_offsetr2:x_offsetr2+right2.shape[1]] = right2
    imageCanvasr3[y_offsetr3:y_offsetr3+right3.shape[0], x_offsetr3:x_offsetr3+right3.shape[1]] = right3
    imageCanvasb[y_offsetb:y_offsetb+back.shape[0], x_offsetb:x_offsetb+back.shape[1]] = back        
    
    #res = imageCanvasf[:]
    #cnd = imageCanvasl1[:,:,] > 0
    res = imageCanvasl1[:]
    cnd = imageCanvasl2[:,:,] > 0
    res[cnd] = imageCanvasl2[cnd]
    cnd = imageCanvasl3[:,:,] > 0
    res[cnd] = imageCanvasl3[cnd]
    cnd = imageCanvasr1[:,:,] > 0
    res[cnd] = imageCanvasr1[cnd]
    cnd = imageCanvasr2[:,:,] > 0
    res[cnd] = imageCanvasr2[cnd]
    cnd = imageCanvasr3[:,:,] > 0
    res[cnd] = imageCanvasr3[cnd]
    cnd = imageCanvasb[:,:,] > 0
    res[cnd] = imageCanvasb[cnd]
   # cnd = imageCanvastruck[:,:,] > 0
   # res[cnd] = imageCanvastruck[cnd]
    
    cv2.imshow("Birds Eye", res)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        y_offsett = y_offsett - 1
        print("y_offsett = ", y_offsett)
    
    elif key == ord("w"):
        x_offsett = x_offsett - 1
        print("x_offsett = ", x_offsett)
        
    elif key == ord("e"):
        y_offsett = y_offsett + 1
        print("y_offsett = ", y_offsett)
        
    elif key == ord("r"):
        x_offsett = x_offsett + 1
        print("x_offsett = ", x_offsett)
    
    
    if key == ord("a"):
        y_offsetl1 = y_offsetl1 - 1
        print("y_offsetl1 = ", y_offsetl1)
    
    elif key == ord("s"):
        x_offsetl1 = x_offsetl1 - 1
        print("x_offsetl1 = ", x_offsetl1)
        
    elif key == ord("d"):
        y_offsetl1 = y_offsetl1 + 1
        print("y_offsetl1 = ", y_offsetl1)
        
    elif key == ord("f"):
        x_offsetl1 = x_offsetl1 + 1
        print("x_offsetl1 = ", x_offsetl1)
        
        
    if key == ord("z"):
        y_offsetr1 = y_offsetr1 - 1
        print("y_offsetr1 = ", y_offsetr1)
    
    elif key == ord("x"):
        x_offsetr1 = x_offsetr1 - 1
        print("x_offsetr1 = ", x_offsetr1)
        
    elif key == ord("c"):
        y_offsetr1 = y_offsetr1 + 1
        print("y_offsetr1 = ", y_offsetr1)
        
    elif key == ord("v"):
        x_offsetr1 = x_offsetr1 + 1
        print("x_offsetr1 = ", x_offsetr1)
        
        
    if key == ord("t"):
        y_offsetl2 = y_offsetl2 - 1
        print("y_offsetl2 = ", y_offsetl2)
    
    elif key == ord("y"):
        x_offsetl2 = x_offsetl2 - 1
        print("x_offsetl2 = ", x_offsetl2)
        
    elif key == ord("u"):
        y_offsetl2 = y_offsetl2 + 1
        print("y_offsetl2 = ", y_offsetl2)
        
    elif key == ord("i"):
        x_offsetl2 = x_offsetl2 + 1
        print("x_offsetl2 = ", x_offsetl2)
        
        
    if key == ord("g"):
        y_offsetr2 = y_offsetr2 - 1
        print("y_offsetr2 = ", y_offsetr2)
    
    elif key == ord("h"):
        x_offsetr2 = x_offsetr2 - 1
        print("x_offsetr2 = ", x_offsetr2)
        
    elif key == ord("j"):
        y_offsetr2 = y_offsetr2 + 1
        print("y_offsetr2 = ", y_offsetr2)
        
    elif key == ord("k"):
        x_offsetr2 = x_offsetr2 + 1
        print("x_offsetr2 = ", x_offsetr2)
        
        
    if key == ord("1"):
        y_offsetr3 = y_offsetr3 - 1
        print("y_offsetr3 = ", y_offsetr3)
    
    elif key == ord("2"):
        x_offsetr3 = x_offsetr3 - 1
        print("x_offsetr3 = ", x_offsetr3)
        
    elif key == ord("3"):
        y_offsetr3 = y_offsetr3 + 1
        print("y_offsetr3 = ", y_offsetr3)
        
    elif key == ord("4"):
        x_offsetr3 = x_offsetr3 + 1
        print("x_offsetr3 = ", x_offsetr3)
        
        
    if key == ord("5"):
        y_offsetl3 = y_offsetl3 - 1
        print("y_offsetl3 = ", y_offsetl3)
    
    elif key == ord("6"):
        x_offsetl3 = x_offsetl3 - 1
        print("x_offsetl3 = ", x_offsetl3)
        
    elif key == ord("7"):
        y_offsetl3 = y_offsetl3 + 1
        print("y_offsetl3 = ", y_offsetl3)
        
    elif key == ord("8"):
        x_offsetl3 = x_offsetl3 + 1
        print("x_offsetl3 = ", x_offsetl3)
        
        
    if key == ord("b"):
        y_offsetb = y_offsetb - 1
        print("y_offsetb = ", y_offsetb)
    
    elif key == ord("n"):
        x_offsetb = x_offsetb - 1
        print("x_offsetb = ", x_offsetb)
        
    elif key == ord("m"):
        y_offsetb = y_offsetb + 1
        print("y_offsetb = ", y_offsetb)
        
    elif key == ord(","):
        x_offsetb = x_offsetb + 1
        print("x_offsetb = ", x_offsetb)
        
        
    elif key == ord("-"):
        anglel2 = anglel2 + 1
        angler2 = angler2 + 1
        angleb = angleb + 1
        print("angle = ", (anglel2-180))
        
    elif key == ord("="):
        anglel2 = anglel2 - 1
        angler2 = angler2 - 1
        angleb = angleb - 1
        print("angle = ", (anglel2-180))
        
    if key == ord("|"):
        i = anglel2-180
        a = [x_offsetl1,y_offsetl1,x_offsetl2,y_offsetl2,x_offsetl3,y_offsetl3,
                x_offsetr1,y_offsetr1,x_offsetr2,y_offsetr2,x_offsetr3,y_offsetr3,
                x_offsetb,y_offsetb]
        ls[i] = a
        #f = open("listbin", "wb") #Creates a serial file listbin with write-back permission
        #f.write(pickle.dumps(ls))
        #f.close() 
        print("coord = ", (ls[i]))
        
    if key == ord("/"):
        break

cv2.waitkey(0)
   
cv2.destroyAllWindows()
cv2.waitKey(1)