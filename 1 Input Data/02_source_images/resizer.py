#!/usr/bin/python
from PIL import Image
import os
import math

path = "data/source_images/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item) and "jpeg" in item:
            im = Image.open(path+item)
            imResize = im.resize((math.floor(im.size[0]/5),math.floor(im.size[1]/5)))
            imResize.save(path+item, 'JPEG', quality=90)
            print(item)
resize()