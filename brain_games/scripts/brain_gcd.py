from brain_games.cli import welcome_user
from brain_games.games.brain_gcd import brain_gcd


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    brain_gcd(username)

if __name__ == '__main__':
    main()