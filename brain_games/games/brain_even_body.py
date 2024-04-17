#!/usr/bin/env python3.8

from random import randint
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def random_number():
    rand_num = randint(1, 11)
    return rand_num


def is_even(ask):
    if ask % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result


def game_body():
    ask = random_number()
    result = is_even(ask)
    return ask, result
