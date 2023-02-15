def check_csc(code):
    return len(code) == 3 and code.isdigit() and 0 <= int(code) < 1000
