def check_move(position):
    if len(position) != 2:
        return 'The position is not valid.'
    col = position[0].upper()
    if "A" <= col <= "H":
        row = int(position[1])
        if 1 <= row <= 8:
            return f'The piece is moved to {col}{row}.'
        return 'The row value is not in the range 1 to 8!'
    return 'The column value is not in the range a-h or A-H!'
