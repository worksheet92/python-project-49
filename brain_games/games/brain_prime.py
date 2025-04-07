import random
import prompt

def brain_prime(username):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        rand_num = random.randint(1, 100)
        j = 2
        is_prime_number = True
        while j < rand_num / 2:
            if rand_num % j == 0:
                is_prime_number = False
                break 
            else:
                j += 1
        print(f"Question:{rand_num}")
        answer = prompt.string(f'Your answer:')
        if is_prime_number == True and answer == 'yes':
            print('Correct!')
        elif is_prime_number == False and answer != 'no':
            print(f"'{answer}' is a wrong answer ;(. Correct answer was 'no'. Let's try again {username}!")
            return
        elif is_prime_number == False and answer == 'no':
            print('Correct!')
        elif is_prime_number == True and answer != 'yes':
            print(f"'{answer}' is a wrong answer ;(. Correct answer was 'yes'. Let's try again {username}!")
            return
        i += 1
    print(f'Congratulations {username}!')