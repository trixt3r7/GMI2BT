from modules import divisible_dict, check_num, random_int


print("===== Find numbers which are divisible with two numbers within 1-1000 ======")
print("Type two numbers to check")
num1 = check_num("First number: ")
num2 = check_num("Second number: ")
divisible = divisible_dict(num1, num2)
print(f"Numbers: {divisible['numbers']}")
print(f"Total: {divisible['total']}")
print(f"Average: {divisible['average']}")

print("\n=================== Guessing game ====================")
max_num = 100
print(f"The computer is thinking of a number between 1 and {max_num}")
secret_number = random_int(max_num)
counter = 0
while True:
    guess = check_num("What number is it thinking of?: ")
    counter += 1
    if guess == secret_number:
        print(f"Congratulations!!! That is correct, It was thinking of {guess}")
        print(f"It took you {counter} tries to guess it right.")
        print(f"Thank you for playing.")
        break
    elif guess > max_num or guess < 0:
        print(f"Try a number between 1 and 100")
    elif guess < secret_number:
        print(f"Thinking of a number HIGHER than {guess}, try again.")
    elif guess > secret_number:
        print(f"Thinking of a number LOWER than {guess}, try again.")
