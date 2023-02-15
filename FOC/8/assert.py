def withdraw(amount, balance):
    assert type(balance) == int
    if balance < -100:
        print("Insufficient balance")
        return(balance)
    else:
        print("withdrawn")
        return(balance - amount)
withdraw(100,'a')