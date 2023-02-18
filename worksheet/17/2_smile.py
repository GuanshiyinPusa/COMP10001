import PIL.Image as pim

img = pim.new('1',(9,7))
img.putpixel((3,1),1)
img.putpixel((5,1),1)
img.putpixel((3,2),1)
img.putpixel((5,2),1)
img.putpixel((2,4),1)
img.putpixel((3,5),1)
img.putpixel((4,5),1)
img.putpixel((5,5),1)
img.putpixel((6,4),1)
img.save('smile.png')