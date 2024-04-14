#!/usr/bin/env python3.8

from itertools import islice
from random import randint
from brain_games.games.engine.functions import welcome_user, user_result
from brain_games.games.engine.functions import wrong_answer, cortect_answer
from brain_games.games.engine.functions import congratulation


def brain_progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        progression = list(islice(range(randint(0, 5), 101, randint(1, 5)), 10))
        hide_index = randint(0, 9)
        result = progression[hide_index]
        progression[hide_index] = '..'
        question = ' '.join(str(_) for _ in progression)
        print(f"Question: {(str(question))}")
        user_choice = int(user_result())
        if user_choice == result:
            cortect_answer()
            i += 1
        else:
            wrong_answer(user_choice, result, name)
            break
    if i == 3:
        congratulation(name)


def progression_start():
    brain_progression()
