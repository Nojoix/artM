import cv2
import numpy as np
import urllib2
import random

#class createImg():
#    def __init__(self, numbers):
#        self.numbers = numbers

def polyline(numbers, url):
    lnum = numbers
    #lnum = self.numbers
    elist = []
    plist = []
    cnt = 0
    c = 0
    try:
        resp = urllib2.urlopen(url)
        imag = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(imag, cv2.IMREAD_COLOR)
        h, w, ch= image.shape
        #image = cv2.imread('imgbq.jpg', -1)
        for n in lnum:
            if int(n) != 0:
                if cnt != 2:
                    nn = random.randint(2,4)
                    xn = random.randint(5, 10)
                    pn = ((int(n * 2)) + (w/nn))
                    if pn > 10:
                        plist.append(pn)
                        cnt += 1
                        c += 1
                else:
                    elist.append(tuple(plist))
                    plist = []
                    cnt = 0
        mask = np.zeros(image.shape, dtype=np.uint8)
        roi_corners = np.array([elist], dtype=np.int32)
        channel_count = image.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
        cv2.fillPoly(mask, roi_corners, ignore_mask_color)
        #self.masked_image = cv2.bitwise_and(image, mask)
        masked_image = cv2.bitwise_and(image, mask)

        # delete black background
        tmp = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)
        _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
        b, g, r = cv2.split(masked_image)
        rgba = [b, g, r, alpha]
        dst = cv2.merge(rgba, 4)

        cv2.imwrite('{0}.png'.format(str(w+h)), dst)
        return masked_image
    except (AttributeError, urllib2.HTTPError):
        return