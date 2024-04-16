#!/usr/bin/env python3.8

from brain_games.games.engine.functions import even, random_number


def brain_even():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    rand_num = random_number()
    result = even(rand_num)
    return rand_num, result, rules
