#!/usr/bin/env python3

import prompt
MAX_TRIES = 3


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def user_result():
    user_choice = prompt.string('Your answer? ')
    return user_choice


def wrong_answer(user_choice, result, name):
    wrong_message = 'is wrong answer ;(. Correct answer was'
    print(f"{str(user_choice)} {wrong_message} {str(result)}.")
    print(f"Let's try again, {name}!")


def correct_answer():
    print('Correct!')


def congratulation(name):
    print(f'Congratulations, {name}!')


def engine(game):
    name = welcome_user()
    print(game.RULES)
    count_tries = 0
    while count_tries < MAX_TRIES:
        ask, result = game.game_body()
        print(f'Question: {ask}')
        user_choice = user_result()
        if user_choice == result:
            correct_answer()
            count_tries += 1
        else:
            wrong_answer(user_choice, result, name)
            break
    if count_tries == MAX_TRIES:
        congratulation(name)
