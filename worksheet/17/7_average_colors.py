import PIL.Image as pim

filename = input("Enter a filename: ")
original = pim.open(filename)
image = pim.new("L", original.size)
for x in range(image.width):
    for y in range(image.height):
        r, g, b = original.getpixel((x, y))
        average = (r + g + b) // 3
        image.putpixel((x, y), average)
image.save('output.png')