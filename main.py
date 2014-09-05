#! /usr/bin/env python

import sys
import math
from PIL import Image

if __name__ == '__main__':
    source = Image.open(sys.argv[1])
    source.convert('RGB')
    dest = source.copy()

    (width, height) = source.size
    print width
    print height

    for y in range(height):
        for x in range(width):
            (old_r, old_g, old_b) = source.getpixel((x,y))
            dest.putpixel((x,y), (old_r, old_g, old_b))
            
            (new_r, new_g, new_b) = (old_r, old_g, old_b)

            dr = abs(old_r - new_r)
            dg = abs(old_g - new_g)
            db = abs(old_b - new_b)

            r = 0
            g = 0
            b = 0

            if x < width-1:
                (r,g,b) = source.getpixel((x+1,y))
                r += dr * 7 / 16
                g += dg * 7 / 16
                b += db * 7 / 16
                dest.putpixel((x+1,y), (r,g,b))

            if x > 0 and y < height-1:
                (r,g,b) = source.getpixel((x-1,y+1))
                r += dr * 3 / 16
                g += dg * 3 / 16
                b += db * 3 / 16
                dest.putpixel((x-1,y+1), (r,g,b))

            if y < height-1:
                (r,g,b) = source.getpixel((x,y+1))
                r += dr * 5 / 16
                g += dg * 5 / 16
                b += db * 5 / 16
                dest.putpixel((x,y+1), (r,g,b))

            if x < width-1 and y < height-1:
                (r,g,b) = source.getpixel((x+1,y+1))
                r += dr * 1 / 16
                g += dg * 1 / 16
                b += db * 1 / 16
                dest.putpixel((x+1,y+1), (r,g,b))

    dest.save(sys.argv[2])
