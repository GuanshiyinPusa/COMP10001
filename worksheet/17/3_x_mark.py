import PIL.Image as pim

image = pim.new('1', (50, 50))
for i in range(50):
    image.putpixel((i, i), 1)
    image.putpixel((i, 49 - i), 1)