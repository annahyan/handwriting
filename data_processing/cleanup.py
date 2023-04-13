#!/usr/bin/env python3

import argparse
import os
import cv2
import numpy as np

parser = argparse.ArgumentParser(description='Crop a region from a PNG image.')
parser.add_argument('filename', metavar='filename', type=str,
                    help='the name of the input PNG file')

parser.add_argument('outdir', metavar='outdir', type=str,
                    help='the name of the output directory')

# Parse the arguments
args = parser.parse_args()

img_name = os.path.splitext(os.path.basename(args.filename))[0]
output_dir = args.outdir

# Processing

img = cv2.imread(args.filename)

_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

gray = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# getting the line ends
xleft = 1e5
ytop = 1e5
xright = 0
ybottom = 0

relevant_contours = []
discarded = []

for contour in contours:
    x,y,w,h = cv2.boundingRect(contour)
    aspect_ratio = float(w)/h
    
    ### This part gets the main words
    if aspect_ratio > 0.2 and aspect_ratio < 5 and w > 10 and h > 10:
        cv2.rectangle(thresh, (x, y), (x+w, y+h), (0, 255, 0), 2)
        relevant_contours.append(contour)
        if x < xleft:
            xleft = x
        if y < ytop:
            ytop = y
        if x + w > xright:
            xright = x + w
        if y + h > ybottom:
            ybottom = y + h
    
    else:
        discarded.append(contour)

for contour in discarded:
    x,y,w,h = cv2.boundingRect(contour)

    if y > ytop  and y + h < ybottom:
        cv2.rectangle(thresh, (x, y), (x+w, y+h), (255, 0, 0), 2)
        relevant_contours.append(contour)

# cv2.imshow('image window', thresh)
# # add wait key. window waits until user presses a key
# cv2.waitKey(0)
# # and finally destroy/close all open windows
# cv2.destroyAllWindows()

# Draw relevant contours on a new image
output = np.zeros_like(thresh)
cv2.drawContours(output, relevant_contours, -1, (255, 255, 255), -1)

cv2.imwrite(os.path.join(output_dir, img_name + "_cleaned.png"), output)