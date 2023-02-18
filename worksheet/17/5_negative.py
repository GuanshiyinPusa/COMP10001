import PIL.Image as pim

filename = input("Enter a filename: ")
original = pim.open(filename)
image = pim.new("L", original.size)
for x in range(image.width):
    for y in range(image.height):
        colour_value = original.getpixel((x, y))
        negative = 255 - colour_value
        image.putpixel((x, y), negative)
image.save('output.png')