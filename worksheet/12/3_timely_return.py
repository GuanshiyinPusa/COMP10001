def issorted(numlist):
    return all(numlist[i] <= numlist[i+1] for i in range(len(numlist)-1))