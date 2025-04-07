import random
import prompt

def brain_progression(username):
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        rand_num = random.randint(0, 50)
        rand_num_diffrence = random.randint(1, 10)
        rand_num_times = random.randint(5, 10)
        j = 0
        list_of_num = []
        while j != rand_num_times:
            list_of_num.append(rand_num)
            rand_num = rand_num + rand_num_diffrence
            j += 1
        index = random.randint(0, len(list_of_num) - 1)
        rand_element = list_of_num[index]
        list_of_num[index] = '..'
        print(f"Question:{list_of_num}")
        answer = prompt.string(f'Your answer:')
        if answer == str(rand_element):
            print('Correct!')
        else:
            print(f"'{answer}' is a wrong answer ;(. Correct answer was '{rand_element}'. Let's try again {username}!")               
            return
        i += 1
    print(f'Congratulations {username}!')