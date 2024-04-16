#!/usr/bin/env python3.8

from brain_games.games.engine.functions import prime, random_num


def brain_prime():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    rand_num = random_num()
    result = prime(rand_num)
    return rand_num, result, rules
