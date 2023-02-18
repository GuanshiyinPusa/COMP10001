import PIL.Image as pim

filename = input("Enter a filename: ")
threshold = int(input("Enter a threshold: "))
original = pim.open(filename)
image = pim.new("1", original.size)
for x in range(image.width):
    for y in range(image.height):
        colour_value = original.getpixel((x, y))
        if colour_value >= threshold:
            image.putpixel((x, y), 1)
        else:
            image.putpixel((x, y), 0)

image.save('output.png')