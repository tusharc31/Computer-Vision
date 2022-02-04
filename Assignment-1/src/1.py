import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
import numpy as np
import cv2


image_points = []
fig = plt.figure(figsize=(20,30))

img = mpimg.imread('../data/black-dots.JPG')

def onclick(event):
    ix, iy = event.xdata, event.ydata
    image_points.append([ix, iy])

cid = fig.canvas.mpl_connect('button_press_event', onclick)

print(image_points)
imgplot = plt.imshow(img)
plt.show()


