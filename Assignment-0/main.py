import cv2


###### Reading image
# img = cv2.imread("./FINAL/Data/Q3/Set-2/background.jpg")
# print(img.shape)
# cv2.imshow("Output", img)
# cv2.waitKey(1000)

# for i in range(1, 79):
#     cv2.imwrite("gg/frame"+str(i)+".jpg", img)


###### Reading video and saving frames
# vid = cv2.VideoCapture("FINAL/Data/Q3/Set-1/vid1-2.mp4")
# count = 0

# while True:

#     success, img = vid.read()
#     if success == True:
#         count = count+1
#         cv2.imshow("Output",img)
#         if cv2.waitKey(40) & 0xFF == ord('q'):
#             break
#         # cv2.imwrite("gg/frame"+str(count)+".jpg", img)

#     else:
#         break

# print(f"Total frames: {count}")


######## Using webcam
# cap = cv2.VideoCapture(0) # using default camera, if more than 1, add ID
# cap.set(3,640) # width is id no 3
# cap.set(4,480) # height is id no 4
# cap.set(10,100) # Brightness id is 10
# while True:
#     success, img = cap.read()
#     cv2.imshow("Output",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


######## FRAMES TO VIDEO
# import numpy as np
# import os
# from os.path import isfile, join

# def convert_frames_to_video(pathIn,pathOut,fps):

#     frame_array = []
#     files = os.listdir(pathIn)
#     files.sort(key = lambda x: int(x[5:-4]))

#     for i in range(0, len(files), 5):
#         filename = pathIn + files[i]
#         img = cv2.imread(filename)
#         height, width, layers = img.shape
#         print(filename, height, width, layers)
#         size = (width,height)
#         frame_array.append(img)

#     out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

#     for i in range(len(frame_array)):
#         out.write(frame_array[i])

#     out.release()

# pathIn= './gg/'
# pathOut = 'bt.avi'
# fps = 24.0
# convert_frames_to_video(pathIn, pathOut, fps)



######## CHROMA KEYING
# import cv2
# import numpy as np
 
# video1 = cv2.VideoCapture("FINAL/Data/Q3/Set-1/vid1-2.mp4")
# video2 = cv2.VideoCapture("FINAL/Data/Q3/Set-1/vid2.mp4")

# cnt = 0

# while True:

#     cnt += 1
 
#     ret1, frame1 = video1.read()
#     ret2, frame2 = video2.read()

#     ret = ret1 and ret2

#     if ret == True:
    
#         frame1 = cv2.resize(frame1, (640, 360))
#         frame2 = cv2.resize(frame2, (640, 360))
    
#         l_bound = np.array([160, 160, 160])
#         u_bound = np.array([255, 255, 255])
    
#         mask1 = cv2.inRange(frame1, l_bound, u_bound)
#         res = cv2.bitwise_and(frame1, frame1, mask = mask1)
    
#         f = frame1 - res
#         f = np.where(f == 0, frame2, f)
    
#         # cv2.imshow("video", frame)
#         cv2.imshow("mask", f)
#         # cv2.imwrite("gg/"+str(cnt)+".jpg", f)
    
#         if cv2.waitKey(25) == 27:
#             break

#     else:
#         break
 
# video1.release()
# video2.release()
# cv2.destroyAllWindows()


import cv2
import numpy as np
 
video1 = cv2.VideoCapture("FINAL/Data/Q3/vid1-2.mp4")
video2 = cv2.VideoCapture("FINAL/Data/Q3/vid2.mp4")

cnt = 0

while True:

    cnt += 1
 
    ret1, frame1 = video1.read()
    ret2, frame2 = video2.read()

    ret = ret1 and ret2

    if ret == True:
    
        frame1 = cv2.resize(frame1, (640, 360))
        frame2 = cv2.resize(frame2, (640, 360))
        frame1_copy = np.copy(frame1)
        l_bound = np.array([160, 160, 160])
        u_bound = np.array([255, 255, 255])
        mask = cv2.inRange(frame1_copy, l_bound, u_bound)
        masked_image = np.copy(frame1_copy)
        masked_image[mask != 0] = [0, 0, 0]
        background = frame2[0:360, 0:640]
        background[mask == 0] = [0, 0, 0]
        final_image = background + masked_image
        cv2.imshow("output", final_image)

        if cv2.waitKey(25) == 27:
            break

    else:
        break
 
video1.release()
video2.release()
cv2.destroyAllWindows()
