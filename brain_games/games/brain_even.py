import random

import prompt


def brain_even(username):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0 
    while i < 3:
        random_number = random.randint(0, 1000)
        print(f"Question: {random_number}")
        answer = prompt.string("Your answer:")
        if random_number % 2 == 0 and answer == 'yes':
            print('Your answer: yes\nCorrect!')
        elif random_number % 2 == 0 and answer != 'yes':
            print(f"'{answer}' is a wrong answer ;(.")
            print("Correct answer was 'no'.")
            print(f"Let's try again {username}!")
            return
        elif random_number % 2 != 0 and answer == 'no':
            print('Your answer: no\nCorrect!')
        elif random_number % 2 != 0 and answer != 'no':
            print(f"'{answer}' is a wrong answer ;(.")
            print("Correct answer was 'yes'.")
            print(f"Let's try again {username}!")
            return
        i += 1
    print(f'Congratulations, {username}')