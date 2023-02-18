def basenum(num, base):
    st = str(num)
    for i in range(len(st)):
        if int(st[i]) >= base:
            return False
    return True
