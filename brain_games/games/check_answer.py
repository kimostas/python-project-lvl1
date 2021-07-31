#!/usr/bin/env python


def check_answer(game, name):
    questions = 3
    for _ in range(questions):
        answer, expression = game()
        print(f"Question: {expression}")
        user_input = input("Your answer: ")
        if user_input == answer:
            print("Correct!")
            continue
        if user_input != answer:
            print(f"'{user_input}' is wrong answer ;(. Correct answer was "
                  f"'{answer}'. \nLet's try again, {name}! ")
            return
    print(f"Congratulations, {name}!")