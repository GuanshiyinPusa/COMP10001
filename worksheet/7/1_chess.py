def check_move(column, row):
    if "A" <= column <= "H" and 1 <= row <= 8:
        return f'The piece is moved to {column}{row}.'
    return 'The position is not valid.'

