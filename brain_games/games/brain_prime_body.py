#!/usr/bin/env python3.8

from brain_games.games.engine.functions import prime, random_num


def brain_prime():
    rand_num = random_num()
    result = prime(rand_num)
    return rand_num, result
