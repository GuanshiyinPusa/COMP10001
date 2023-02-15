def check_move(column, row):
    col = column.upper()
    if "A" <= col <= "H" and 1 <= row <= 8:
        return f'The piece is moved to {col}{row}.'
    return 'The position is not valid.'
