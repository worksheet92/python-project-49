from brain_games.cli import welcome_user
from brain_games.games.brain_prime import brain_prime


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    brain_prime(username)


if __name__ == '__main__':

    main()