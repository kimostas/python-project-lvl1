#!/usr/bin/env python


from brain_games.games.cli import welcome_user
from brain_games.games.purpose_game import purpose_brain_culc
from brain_games.games.calc import check_calc
from brain_games.games.check_answer import check_answer


def main():
    name = welcome_user()
    purpose_brain_culc()
    check_answer(check_calc, name)


if __name__ == '__main__':
    main()
