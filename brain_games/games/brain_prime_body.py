#!/usr/bin/env python3.8

from random import randint
from math import sqrt
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def random_num():
    rand_num = randint(2, 101)
    return rand_num


def is_prime(ask):
    for delitel in range(2, int(sqrt(ask)) + 1):
        if ask % delitel == 0:
            result = 'no'
            break
        else:
            result = 'yes'
    return result


def game_body():
    ask = random_num()
    rigt_result = is_prime(ask)
    return ask, rigt_result
