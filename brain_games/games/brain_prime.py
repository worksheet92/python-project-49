import random

import prompt


def check_if_prime_number(num):
    j = 2
    if num == 2:
        return True
    if num == 1:
        return False
    while j < num:
        if num % j == 0:
            return False
        else:
            j += 1
    return True


def brain_prime(username):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        rand_num = random.randint(1, 100)
        is_prime_number = check_if_prime_number(rand_num)
        print(f"Question:{rand_num}")
        answer = prompt.string('Your answer:')
        if is_prime_number and answer == 'yes':
            print('Correct!')
        elif not is_prime_number and answer != 'no':
            print(f"'{answer}' is a wrong answer ;(.")
            print("Correct answer was 'no'.")
            print(f"Let's try again {username}!")
            return
        elif not is_prime_number and answer == 'no':
            print('Correct!')
        elif is_prime_number and answer != 'yes':
            print(f"'{answer}' is a wrong answer ;(.")
            print("Correct answer was 'yes'.")
            print(f"Let's try again {username}!")
            return
        i += 1
    print(f'Congratulations {username}!')