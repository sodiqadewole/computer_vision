import cv2
import numpy as np
import os

# load image as grayscale
img = cv2.imread(os.path.join(os.getcwd(), 'scientific_python/cv_tutorials/' 'lion.jpg'), 0)
img = img/255
img
cv2.imshow('image', img) 
cv2.waitKey(0)
cv2.destroyWindow('image')
#cv2.destroyAllWindows()
