import random
import prompt


def brain_gcd(username):
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        rand_num1 = random.randint(0, 100)
        rand_num2 = random.randint(0 ,100)
        print(f'{rand_num1} {rand_num2}')
        while rand_num1 != rand_num2:
            if rand_num1 > rand_num2:
                rand_num1 = rand_num1 - rand_num2
            else:
                rand_num2 = rand_num2 - rand_num1    
        answer = prompt.string(f'Your answer:')
        if answer == str(rand_num1):
            print('Correct!')
        else:
            print(f"'{answer}' is a wrong answer ;(. Correct answer was '{rand_num1}'. Let's try again {username}!")               
            return
        i += 1
    print(f'Congratulations {username}!')