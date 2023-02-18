import PIL.Image as pim

image = pim.new('1', (32, 24), 1)
for i in range(16):
    for j in range(12):
        image.putpixel((i, j), 0)
        image.putpixel((16 + i, 12 + j), 0)

image.save('output.png')