from brain_games.cli import welcome_user
from brain_games.games.brain_calc import brain_calc


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    brain_calc(username)


if __name__ == '__main__':

    main()