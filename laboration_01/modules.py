from random import randint


def divisible_list(n1, n2):
    numbers_list = []
    for i in range(1, 1001):
        if i % n1 == 0 and i % n2 == 0:
            numbers_list.append(i)
    return numbers_list


def divisible_dict(n1, n2):
    numbers_list = []
    divisible = {}
    for i in range(1, 1001):
        if i % n1 == 0 and i % n2 == 0:
            numbers_list.append(i)
    divisible["numbers"] = numbers_list
    divisible["total"] = sum(numbers_list)
    divisible["average"] = sum(numbers_list) / len(numbers_list)
    return divisible


def check_num(question):
    while True:
        try:
            num = int(input(question))
            check_for_division_error = 2 / num
            break
        except ValueError:
            print("Invalid input, enter only whole numbers")
        except ZeroDivisionError:
            print("Number 0 is not allowed.")
    return num


# En metod som slumpar ett tal som användaren ska gissa på
def random_int(max_num):
    return randint(1, max_num)
