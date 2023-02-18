import PIL.Image as pim
filename = input("Enter a filename: ")
print()
print(f"Summary of {filename}")
image = pim.open(filename)
print(f"Mode: {image.mode}")
print(f"Width: {image.width}px")
print(f"Height: {image.height}px")