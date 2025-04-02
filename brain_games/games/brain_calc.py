import random
import prompt
import operator


def brain_calc(username):
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        rand_num1 = random.randint(0, 1000)
        rand_num2 = random.randint(0, 1000)
        operators = ['+', '-', '*']
        operator = random.choice(operators)
        print(f'{rand_num1} {operator} {rand_num2}')
        if operator == '+':
            result = rand_num1 + rand_num2
        elif operator == '-':
            result = rand_num1 - rand_num2
        elif operator == '*':
            result = rand_num1 * rand_num2
        answer = prompt.string(f"Your answer:")
        if answer == str(result):
            print('Correct!')
        else:
            print(f"'{answer}' is a wrong answer ;(. Correct answer was '{result}'. Let's try again {username}!")
            return
        i += 1
    print(f'Congratulations {username}!')