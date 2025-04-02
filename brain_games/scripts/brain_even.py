from brain_games.cli import welcome_user
from brain_games.game_even import game_even

def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()
    game_even(username)

if __name__ == '__main__':
    main()

