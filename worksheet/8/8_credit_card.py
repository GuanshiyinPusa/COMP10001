def validate_card(cardnum):
    leng = len(cardnum)
    total = 0
    for i in cardnum:
        total += int(i)
    return leng == 16 and total % 10 == 0
