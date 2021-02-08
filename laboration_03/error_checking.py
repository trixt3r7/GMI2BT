def check_num(input_string):
    try:
        input_string = int(input_string)
        return input_string
    except ValueError:
        print("Invalid input. Please try again.")


def num_in_range(input_string, list):
    while True:
        number = input(input_string)
        if check_num(number) and int(number) <= len(list):
            number = int(number)
            number -= 1
            return number
