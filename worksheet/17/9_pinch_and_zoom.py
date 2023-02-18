import PIL.Image as pim

filename = input("Enter a filename: ")
original = pim.open(filename)

zoom_x = int(input("Enter a width multiplier: "))
zoom_y = int(input("Enter a height multiplier: "))
new_size = (original.width * zoom_x, original.height * zoom_y)
image = pim.new(original.mode, new_size)

for x in range(image.width):
    for y in range(image.height):
        source_pixel = (x // zoom_x, y // zoom_y)
        colour_value = original.getpixel(source_pixel)
        image.putpixel((x, y), colour_value)

image.save('output.png')