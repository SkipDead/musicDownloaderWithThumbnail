import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import math
import re
import io
import urllib.request


def getThumbnail(url):
    exp = "^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*"
    s = re.findall(exp,url)[0][-1]
    print("youtube video code : " + s)
    thumbnail = f"https://i.ytimg.com/vi/{s}/maxresdefault.jpg"
    print(thumbnail)
    f = open(f'{s}.jpg','wb')
    f.write(urllib.request.urlopen(thumbnail).read())
    f.close()
    return s+'.jpg'

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

def center_crop(img, dim):
	"""Returns center cropped image
	Args:
	img: image to be center cropped
	dim: dimensions (width, height) to be cropped
	"""
	width, height = img.shape[1], img.shape[0]

	# process crop width and height for max available dimension
	crop_width = dim[0] if dim[0]<img.shape[1] else img.shape[1]
	crop_height = dim[1] if dim[1]<img.shape[0] else img.shape[0] 
	mid_x, mid_y = int(width/2), int(height/2)
	cw2, ch2 = int(crop_width/2), int(crop_height/2) 
	crop_img = img[mid_y-ch2:mid_y+ch2, mid_x-cw2:mid_x+cw2]
	return crop_img


def getYtThumbnail(yturl): #https://youtu.be/RMQC7POVYWM
    imgfilename = getThumbnail(yturl)
    img=cv2.imread(imgfilename)
    resizedimg = image_resize(img, height=300)
    cropimg = center_crop(resizedimg, (300,300))
    cv2.imwrite(imgfilename, cropimg)
    return imgfilename
    #plt.imshow(cropimg[...,::-1])
    #plt.show()