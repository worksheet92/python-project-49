from brain_games.cli import welcome_user
from brain_games.games.brain_progression import brain_progression


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    brain_progression(username)


if __name__ == '__main__':

    main()