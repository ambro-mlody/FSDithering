import pygame as py
import sys
import math


py.init()
image = py.image.load("obrazek.jpg")
image_size = image.get_size()
size = (image_size[0] * 2, image_size[1])
window = py.display.set_mode(size)
py.display.set_caption("FSDithering")


#def set_pixel(x, y, m):

bits = 2
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


        new_image.set_at((x, y), (newR, newG, newB))

        #r = new_image.get_at((x + 1, y)).r
        #g = new_image.get_at((x + 1, y)).g
        #b = new_image.get_at((x + 1, y)).b
        #a = new_image.get_at((x + 1, y)).a

        #r = r + errR * 7 / 16
        #g = g + errG * 7 / 16
        #b = b + errB * 7 / 16

        #new_image.set_at((x + 1, y), (r, g, b, a))
        # print(r, g, b)

        #r = new_image.get_at((x - 1, y + 1)).r
        #g = new_image.get_at((x - 1, y + 1)).g
        #b = new_image.get_at((x - 1, y + 1)).b
        #a = new_image.get_at((x - 1, y + 1)).a

        #r = r + errR * 3 / 16
        #g = g + errG * 3 / 16
        #b = b + errB * 3 / 16

        #new_image.set_at((x - 1, y + 1), (r, g, b, a))
        #print(r, g, b)

        #r = new_image.get_at((x, y + 1)).r
        #g = new_image.get_at((x, y + 1)).g
        #b = new_image.get_at((x, y + 1)).b
        #a = new_image.get_at((x, y + 1)).a

        #r = r + errR * 5 / 16
        #g = g + errG * 5 / 16
        #b = b + errB * 5 / 16

        #new_image.set_at((x, y + 1), (r, g, b, a))
        #print(r, g, b)

        #r = new_image.get_at((x + 1, y + 1)).r
        #g = new_image.get_at((x + 1, y + 1)).g
        #b = new_image.get_at((x + 1, y + 1)).b
        #a = new_image.get_at((x + 1, y + 1)).a

        #r = r + errR * 1 / 16
        #g = g + errG * 1 / 16
        #b = b + errB * 1 / 16

        #new_image.set_at((x + 1, y + 1), (r, g, b, a))
        #print(r, g, b)


old_image = py.image.load("obrazek.jpg")
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    window.fill((0, 0, 0))
    window.blit(old_image, (0, 0))
    window.blit(new_image, (image_size[0], 0))
    py.display.update()
