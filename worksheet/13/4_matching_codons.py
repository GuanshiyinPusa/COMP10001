def matching_codons(complements, pool1, pool2):
    answ = []
    for cha in pool1:
        ans = ''.join([complements.get(temp) for temp in cha])
        if ans in pool2:
            answ.append((cha, ans))
    return answ