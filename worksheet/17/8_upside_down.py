import PIL.Image as pim

filename = input("Enter a filename: ")
original = pim.open(filename)
image = pim.new(original.mode, original.size)
for x in range(image.width):
    for y in range(image.height):
        colour_value = original.getpixel((image.width - 1 - x,
                                          image.height - 1 - y))
        image.putpixel((x, y), colour_value)
image.save('output.png')