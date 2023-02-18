def grey_value(image):
    total = sum(len(row) for row in image)
    temp = sum(pixel for row in image for pixel in row)
    return temp / total