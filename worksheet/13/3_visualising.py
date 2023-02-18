limit = int(input("Maximum number to factorise: "))
for i in range(1, limit + 1):
    line = ''
    for j in range(1, limit + 1):
        if i % j == 0:
            line += "* "
        else:
            line += "- "
    print(line)
