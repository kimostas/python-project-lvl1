#!/usr/bin/env python


from brain_games.games.cli import welcome_user
from brain_games.games.purpose_game import purpose_brain_progression
from brain_games.games.progression import check_progression
from brain_games.games.check_answer import check_answer


def main():
    name = welcome_user()
    purpose_brain_progression()
    check_progression()
    check_answer(check_progression, name)


if __name__ == '__main__':
    main()
