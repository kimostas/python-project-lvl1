#!/usr/bin/env python


from brain_games.cli import welcome_user
from brain_games.is_even import is_even
from brain_games.get_answer import check_answer


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    is_even()
    check_answer(is_even, name)


if __name__ == '__main__':
    main()
