#!/usr/bin/env python3.8

from brain_games.games.engine.functions import welcome_user, random_number
from brain_games.games.engine.functions import random_operator, user_result
from brain_games.games.engine.functions import wrong_answer, cortect_answer
from brain_games.games.engine.functions import congratulation, calc


def brain_calc():
    name = welcome_user()
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        rand_num_1 = random_number()
        rand_num_2 = random_number()
        operator = random_operator()
        print(f'Question: {str(rand_num_1)} {operator} {str(rand_num_2)}')
        user_choice = int(user_result())
        result = calc(operator, rand_num_1, rand_num_2)
        if user_choice == result:
            cortect_answer()
            i += 1
        else:
            wrong_answer(user_choice, result, name)
            break
    if i == 3:
        congratulation(name)


def calc_start():
    brain_calc()
