#!/usr/bin/env python3.8

from math import gcd
from brain_games.games.engine.functions import random_number


def brain_gcd():
    rules = 'Find the greatest common divisor of given numbers.'
    rand_num_1 = random_number()
    rand_num_2 = random_number()
    ask = [rand_num_1, rand_num_2]
    ask = ' '.join(str(_) for _ in ask)
    result = str(gcd(rand_num_1, rand_num_2))
    return ask, result, rules
