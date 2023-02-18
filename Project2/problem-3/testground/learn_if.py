def is_valid_input(input_str):
    if len(input_str) > 0:
        return input_str
    else:
        return False

input_value = "Hello World!"

if input_str := is_valid_input(input_value):
    print("Valid input:", input_str)
else:
    print("Invalid input")
