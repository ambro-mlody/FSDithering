import pygame as py
import sys
import math


py.init()
image = py.image.load("teleport2.jpg")
image_size = image.get_size()
size = (image_size[0] * 2, image_size[1])
window = py.display.set_mode(size)
py.display.set_caption("FSDithering")


#def set_pixel(x, y, m):

bits = 1
new_image = image
for y in range(image_size[1] - 1):
    for x in range(1, image_size[0] - 1, 1):
        color = image.get_at((x, y))
        oldR = color.r
        oldG = color.g
        oldB = color.b

        newR = round(bits * oldR/255) * math.floor(255/bits)
        newG = round(bits * oldG/255) * math.floor(255/bits)
        newB = round(bits * oldB/255) * math.floor(255/bits)

        errR = oldR - newR
        errG = oldG - newG
        errB = oldB - newB

        c = (newR + newG + newB) / 3



        new_image.set_at((x, y), (newB, newG, newR))

        r = new_image.get_at((x + 1, y)).r
        g = new_image.get_at((x + 1, y)).g
        b = new_image.get_at((x + 1, y)).b
        a = new_image.get_at((x + 1, y)).a

        r = r + errR * 7 / 16
        g = g + errG * 7 / 16
        b = b + errB * 7 / 16

        c = (r + g + b) / 3
        if r > 255:
            r = 255
        if g > 255:
            g = 255
        if b > 255:
            b = 255

        if r < 0:
            r = 0
        if g < 0:
            g = 0
        if b < 0:
            b = 0

        if c > 255:
            c = 255

        if c < 0:
            c = 0

        #print(r, g, b)
        new_image.set_at((x + 1, y), (b, g, r))

        r = new_image.get_at((x - 1, y + 1)).r
        g = new_image.get_at((x - 1, y + 1)).g
        b = new_image.get_at((x - 1, y + 1)).b
        a = new_image.get_at((x - 1, y + 1)).a

        r = r + errR * 3 / 16
        g = g + errG * 3 / 16
        b = b + errB * 3 / 16

        c = (r + g + b) / 3
        if r > 255:
            r = 255
        if g > 255:
            g = 255
        if b > 255:
            b = 255

        if r < 0:
            r = 0
        if g < 0:
            g = 0
        if b < 0:
            b = 0

        if c > 255:
            c = 255

        if c < 0:
            c = 0
        new_image.set_at((x - 1, y + 1), (b, g, r))
        #print(r, g, b)

        r = new_image.get_at((x, y + 1)).r
        g = new_image.get_at((x, y + 1)).g
        b = new_image.get_at((x, y + 1)).b
        a = new_image.get_at((x, y + 1)).a

        r = r + errR * 5 / 16
        g = g + errG * 5 / 16
        b = b + errB * 5 / 16
        c = (r + g + b) / 3
        if r > 255:
            r = 255
        if g > 255:
            g = 255
        if b > 255:
            b = 255

        if r < 0:
            r = 0
        if g < 0:
            g = 0
        if b < 0:
            b = 0

        if c > 255:
            c = 255

        if c < 0:
            c = 0
        new_image.set_at((x, y + 1), (b, g, r))
        #print(r, g, b)

        r = new_image.get_at((x + 1, y + 1)).r
        g = new_image.get_at((x + 1, y + 1)).g
        b = new_image.get_at((x + 1, y + 1)).b
        a = new_image.get_at((x + 1, y + 1)).a

        r = r + errR * 1 / 16
        g = g + errG * 1 / 16
        b = b + errB * 1 / 16
        c = (r + g + b) / 3
        if r > 255:
            r = 255
        if g > 255:
            g = 255
        if b > 255:
            b = 255

        if r < 0:
            r = 0
        if g < 0:
            g = 0
        if b < 0:
            b = 0

        if c > 255:
            c = 255

        if c < 0:
            c = 0
        new_image.set_at((x + 1, y + 1), (b, g, r))
        #print(r, g, b)


old_image = py.image.load("teleport2.jpg")
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    window.fill((0, 0, 0))
    window.blit(old_image, (0, 0))
    window.blit(new_image, (image_size[0], 0))
    py.display.update()
