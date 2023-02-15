from random import randint

def luck_tester(lucky_number, max_rolls, die_size):
    dr = 1
    while dr <= max_rolls:
        if randint(1, die_size) == lucky_number:
            return 'Off to Mordor!'
        dr += 1
    return 'Back to the Shire!'
