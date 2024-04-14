#!/usr/bin/env python3.8

from brain_games.games.engine.functions import welcome_user, random_number
from brain_games.games.engine.functions import user_result, even
from brain_games.games.engine.functions import wrong_answer, cortect_answer
from brain_games.games.engine.functions import congratulation


def brain_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        rand_num = random_number()
        result = even(rand_num)
        print(f'Question: {rand_num}')
        user_choice = user_result()
        if user_choice == result:
            cortect_answer()
            i += 1
        else:
            wrong_answer(user_choice, result, name)
            break
    if i == 3:
        congratulation(name)


def even_start():
    brain_even()
