from math import cos, sin, radians

def triangle_legs(hyp, angle):
    angle_rad = radians(angle)
    adjacent = hyp * cos(angle_rad)
    opposite = hyp * sin(angle_rad)
    return (min(adjacent, opposite), max(adjacent, opposite))