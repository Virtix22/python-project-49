#!/usr/bin/env python3.8

from math import gcd
from brain_games.games.engine.functions import welcome_user, random_number
from brain_games.games.engine.functions import user_result, cortect_answer
from brain_games.games.engine.functions import wrong_answer, congratulation


def brain_gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        rand_num_1 = random_number()
        rand_num_2 = random_number()
        print(f"Question: {str(rand_num_1)} {str(rand_num_2)}")
        user_choice = int(user_result())
        if user_choice == gcd(rand_num_1, rand_num_2):
            cortect_answer()
            i += 1
        else:
            wrong_answer(user_choice, gcd(rand_num_1, rand_num_2), name)
            break
    if i == 3:
        congratulation(name)


def gcd_start():
    brain_gcd()
