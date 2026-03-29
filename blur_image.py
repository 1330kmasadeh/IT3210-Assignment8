from image_lib import *

def blur(image):

    width = image.getWidth()
    height = image.getHeight()

    new_image = EmptyImage(width, height)

    for x in range(1, width-1):
        for y in range(1, height-1):

            r_total = 0
            g_total = 0
            b_total = 0

            for dx in [-1,0,1]:
                for dy in [-1,0,1]:

                    p = image.getPixel(x+dx, y+dy)

                    r_total += p.getRed()
                    g_total += p.getGreen()
                    b_total += p.getBlue()

            r = int(r_total / 9)
            g = int(g_total / 9)
            b = int(b_total / 9)

            new_pixel = Pixel(r,g,b)

            new_image.setPixel(x,y,new_pixel)

    return new_image
