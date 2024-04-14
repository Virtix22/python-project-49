#!/usr/bin/env python3.8

import prompt
from random import randint, choice
from math import sqrt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def random_number():
    random_number_choice = randint(1, 11)
    return random_number_choice


def random_num():
    rand_num = randint(2, 101)
    return rand_num


def random_operator():
    operators = ['+', '-', '*']
    operator_choice = choice(operators)
    return operator_choice


def user_result():
    user_choice = prompt.string('Your answer? ')
    return user_choice


def wrong_answer(choice, resul, name):
    print(f"{str(choice)} is wrong answer ;(. Correct answer was {str(resul)}.")
    print(f"Let's try again, {name}!")


def cortect_answer():
    print('Correct!')


def congratulation(name):
    print(f'Congratulations, {name}')


def prime(rand_num):
    for delitel in range(2, int(sqrt(rand_num)) + 1):
        if rand_num % delitel == 0:
            result = 'no'
            break
        else:
            result = 'yes'
    return result


def even(rand_num):
    if rand_num % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result


def calc(operator, rand_num_1, rand_num_2):
    if operator == '+':
        result = rand_num_1 + rand_num_2
    elif operator == '*':
        result = rand_num_1 * rand_num_2
    elif operator == '-':
        result = rand_num_1 - rand_num_2
    return result
