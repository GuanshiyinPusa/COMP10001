def between_len(words,minlen,maxlen):
    leng = len(words)
    if minlen <= leng <= maxlen:
        return True
    else:
        return False