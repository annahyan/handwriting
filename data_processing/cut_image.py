#!/usr/bin/env python3

import argparse
import os
from PIL import Image

parser = argparse.ArgumentParser(description='Crop a region from a PNG image.')
parser.add_argument('filename', metavar='filename', type=str,
                    help='the name of the input PNG file')

# Parse the arguments
args = parser.parse_args()

# Create a directory with the same name as the input PNG file's basename
output_dir = os.path.splitext(os.path.basename(args.filename))[0]
os.makedirs(output_dir, exist_ok=True)

# Open the PNG file
image = Image.open(args.filename)

## 40 lines 
nlines = 40
left = 30
top = 30
right = 870

linewidth = 30

# Open the PNG file

for i in range(15):

    box = (left, top + i * linewidth - 5, right, top + (i + 1) * linewidth + 5 )

    cropped_image = image.crop(box)

    # Save the cropped image in the output directory with the same basename as the input PNG file
    output_filename = os.path.join(output_dir, "side1_line" + str(i) + ".png")

    cropped_image.save(output_filename)



for i in range(15):

    box = (left + right - 15, top + i * linewidth - 5, right + right, top + (i + 1) * linewidth + 5 )

    cropped_image = image.crop(box)

    # Save the cropped image in the output directory with the same basename as the input PNG file
    output_filename = os.path.join(output_dir, "side2_line" + str(i) + ".png")

    cropped_image.save(output_filename)
