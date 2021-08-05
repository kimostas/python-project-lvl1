#!/usr/bin/env python


from brain_games.games.cli import welcome_user
from brain_games.games.purpose_game import purpose_brain_gcd
from brain_games.games.gcd import check_gcd
from brain_games.games.check_answer import check_answer


def main():
    name = welcome_user()
    purpose_brain_gcd()
    check_gcd()
    check_answer(check_gcd, name)


if __name__ == '__main__':
    main()
