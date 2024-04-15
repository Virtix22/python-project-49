#!/usr/bin/env python3.8

from itertools import islice
from random import randint


def brain_progression():
    progression = list(islice(range(randint(0, 5), 101, randint(1, 5)), 10))
    hide_index = randint(0, 9)
    result = str(progression[hide_index])
    progression[hide_index] = '..'
    ask = ' '.join(str(_) for _ in progression)
    return ask, result


def progression_start():
    brain_progression()
