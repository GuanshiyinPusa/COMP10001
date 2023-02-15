iterator = iter([1,2,3])
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break