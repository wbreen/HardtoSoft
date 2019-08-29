#@Author William Breen 8/27/2019

import cv2
import numpy
import Helper_methods as hm
import matplotlib.pyplot as plt

fold = "Test_Photos/"
thrImg = "Three_images_"
sixImg = "Six_images_"
save_loc = "Cutout_Photos/"

#Import images here:
testImg = fold+thrImg+'1.jpg'

#hm.showImage('test', testImg)


#start thresholding, make rectangles where the photos are supposed to be and then cut out there to make each of those into its own photo

#opening is removing small white noise
#closing is removing small black noise


def get_Picture_Loc(image):
	#Start by converting to grayscale
	img = cv2.imread(image)
	grayImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	#hm.showGreyImage('grayImg', grayImg)
	
	thr = 180
	ret, thresh = cv2.threshold(grayImg, thr, 255, cv2.THRESH_BINARY)
	hm.showGreyImage("Image with Threshold", thresh)
	strucEle = cv2.getStructuringElement(cv2.MORPH_RECT, (20,20))
	close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, strucEle)
	hm.showGreyImage("Image after close 1", close)

	openStrucEle = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
	open = cv2.morphologyEx(close, cv2.MORPH_OPEN, strucEle)
	hm.showGreyImage("Image after open 1", open)

	