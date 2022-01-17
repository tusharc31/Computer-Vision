import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,360)
cap.set(10,100) # Brightness id is 10

cnt = 0
while True:
    success, img = cap.read()
    if success == True:
        cnt+=1
        cv2.imshow("output",img)
        cv2.imwrite("Results/Q2/frame"+str(cnt)+".jpg", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

print(f"\nSaved {cnt} videos to Results/Q2")