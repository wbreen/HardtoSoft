import numpy as np
import cv2



def makeSmaller(image):
	w, h, s = image.shape
	new_w = w/3
	new_h = h/3
	return int(new_w), int(new_h)

def showImage(windowName, image):
	image = cv2.imread(image)
	new_w, new_h = makeSmaller(image)
	image = cv2.resize(image, (new_h, new_w))
	cv2.imshow(windowName, image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()



def makeGreySmaller(image):
	w, h = image.shape
	new_w = w/3
	new_h = h/3
	return int(new_w), int(new_h)
def showGreyImage(windowName, image):
	new_w, new_h = makeGreySmaller(image)
	image = cv2.resize(image, (new_h, new_w))
	cv2.imshow(windowName, image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()