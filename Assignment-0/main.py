import cv2


###### Reading image
# img = cv2.imread("sample.jpeg", 0)
# print(img.shape)
# cv2.imshow("Output", img)
# cv2.waitKey(1000)


###### Reading video and saving frames
# vid = cv2.VideoCapture("sample_vid.mp4")
# count = 0

# while True:

#     success, img = vid.read()
#     if success == True:
#         count = count+1
#         cv2.imwrite("frames/frame"+str(count)+".jpg", img)

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

#     for i in range(len(files)):
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

# pathIn= './frames/'
# pathOut = 'video.avi'
# fps = 30.0
# convert_frames_to_video(pathIn, pathOut, fps)
