LIKELY_WORDS = ["Frenchy", "INTENSE", "ComputerScienceFTW", "HelloMrGumby"]
MIDDLE = "Horse20"
CREME_PUFF = 38

def hack_it(start=LIKELY_WORDS, middle=MIDDLE, end=CREME_PUFF):
    from itertools import product, permutations
    ans = []
    for p in permutations(start, 2):
        for n in range(end + 1):
            if n < 10:
                s = f"0{n}"
            else:
                s = str(n)
            ans.append(f"{p[0]}{p[1]}{middle}{s}")
    return ans
