#!/usr/bin/env python3.8

from brain_games.games.engine.functions import random_number
from brain_games.games.engine.functions import random_operator
from brain_games.games.engine.functions import calc


def brain_calc():
    rules = 'What is the result of the expression?'
    rand_num_1 = random_number()
    rand_num_2 = random_number()
    operator = random_operator()
    ask = [str(rand_num_1), operator, str(rand_num_2)]
    ask = ' '.join(str(_) for _ in ask)
    result = str(calc(operator, rand_num_1, rand_num_2))
    return ask, result, rules
