#!/usr/bin/env python3.8

from math import gcd
from random import randint
RULES = 'Find the greatest common divisor of given numbers.'


def random_number():
    random_number_choice = randint(1, 11)
    return random_number_choice


def game_body():
    rand_num_1 = random_number()
    rand_num_2 = random_number()
    ask = [rand_num_1, rand_num_2]
    ask = ' '.join(str(_) for _ in ask)
    result = str(gcd(rand_num_1, rand_num_2))
    return ask, result
