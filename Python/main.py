import cv2
import numpy as np 
import Image_splitter as img_spl

#folder locations
fold = "Test_Photos/"
thrImg = "Three_images_"
sixImg = "Six_images_"
save_loc = "Cutout_Photos/"


img_spl.get_Picture_Loc(fold+thrImg+'1.jpg')