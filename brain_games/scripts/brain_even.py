from brain_games.cli import welcome_user
from brain_games.games.brain_even import brain_even


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    brain_even(username)

if __name__ == '__main__':
    main()