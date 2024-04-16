#!/usr/bin/env python3

from brain_games.games.engine.functions import welcome_user
from brain_games.games.engine.functions import user_result
from brain_games.games.engine.functions import wrong_answer, correct_answer
from brain_games.games.engine.functions import congratulation


def en_game(game):
    name = welcome_user()
    i = 0
    while i < 3:
        ask, result, rules = game()
        print(rules)
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
