from collections import deque

def cycle(input_list):
    input_deque = deque(input_list)
    input_deque.rotate(1)
    return list(input_deque)
