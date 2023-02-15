def check_move(column, row):
    col = column.upper()
    if "A" <= col <= "H" and 1 <= row <= 8:
        return f'The piece is moved to {col}{row}.'
    elif col not in "ABCDEFGH":
        return 'The column value is not in the range a-h or A-H!'
    return 'The row value is not in the range 1 to 8!'
