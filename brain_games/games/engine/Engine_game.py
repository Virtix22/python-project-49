#!/usr/bin/env python3

from brain_games.games.engine.functions import welcome_user
from brain_games.games.engine.functions import user_result
from brain_games.games.engine.functions import wrong_answer, correct_answer
from brain_games.games.engine.functions import congratulation
from brain_games.games.brain_even_body import brain_even
from brain_games.games.brain_calc_body import brain_calc
from brain_games.games.brain_gcd_body import brain_gcd
from brain_games.games.brain_progression_body import brain_progression
from brain_games.games.brain_prime_body import brain_prime


def en_game(game):
    i = 0
    while i < 3:
        ask, result = game()
        print(f'Question: {ask}')
        user_choice = user_result()
        if user_choice == result:
            correct_answer()
            i += 1
        else:
            wrong_answer(user_choice, result, name)
            break
    if i == 3:
        congratulation(name)


def even_start():
    global name
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    en_game(brain_even)


def calc_start():
    global name
    name = welcome_user()
    print('What is the result of the expression?')
    en_game(brain_calc)


def gcd_start():
    global name
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    en_game(brain_gcd)


def progression_start():
    global name
    name = welcome_user()
    print('What number is missing in the progression?')
    en_game(brain_progression)


def prime_start():
    global name
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    en_game(brain_prime)
