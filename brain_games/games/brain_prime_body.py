#!/usr/bin/env python3.8

from brain_games.games.engine.functions import welcome_user, prime, random_num
from brain_games.games.engine.functions import user_result, cortect_answer
from brain_games.games.engine.functions import wrong_answer, congratulation


def brain_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    i = 0
    while i < 3:
        rand_num = random_num()
        result = prime(rand_num)
        print(f"Question: {rand_num}")
        user_choice = user_result()
        if user_choice == result:
            cortect_answer()
            i += 1
        else:
            wrong_answer(user_choice, result, name)
            break
    if i == 3:
        congratulation(name)


def prime_start():
    brain_prime()
