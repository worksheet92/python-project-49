import random

import prompt


def find_divisor(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1   


def brain_gcd(username):
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        rand_num1 = random.randint(0, 100)
        rand_num2 = random.randint(0, 100)
        print(f'{rand_num1} {rand_num2}')
        result = find_divisor(rand_num1, rand_num2)   
        answer = prompt.string('Your answer:')
        if answer == str(result):
            print('Correct!')
        else:
            print(f"'{answer}' is a wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            print(f"Let's try again {username}!")          
            return
        i += 1
    print(f'Congratulations {username}!')