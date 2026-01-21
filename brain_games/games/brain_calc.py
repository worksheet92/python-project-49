import random

import prompt


def calc(num1, num2, operator):
    if operator == '+':
        num1 + num2
    elif operator == '-':
        num1 - num2
    elif operator == '*':
        num1 * num2     


def brain_calc(username):
    
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        rand_num1 = random.randint(0, 1000)
        rand_num2 = random.randint(0, 1000)
        operators = ['+', '-', '*']
        operator = random.choice(operators)
        print(f'Question: {rand_num1} {operator} {rand_num2}')
        result = calc(rand_num1, rand_num2, operator)
        answer = prompt.string("Your answer:")
        if answer == str(result):
            print('Correct!')
        else:
            print(f"'{answer}' is a wrong answer ;(.")
            print(f"Correct answer was '{result}'.")
            print(f"Let's try again {username}!")  
            return
        i += 1
    print(f'Congratulations, {username}!')