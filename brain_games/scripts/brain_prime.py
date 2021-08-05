#!/usr/bin/env python


from brain_games.games.cli import welcome_user
from brain_games.games.purpose_game import purpose_brain_prime
from brain_games.games.prime import check_prime
from brain_games.games.check_answer import check_answer


def main():
    name = welcome_user()
    purpose_brain_prime()
    check_prime()
    check_answer(check_prime, name)


if __name__ == '__main__':
    main()
