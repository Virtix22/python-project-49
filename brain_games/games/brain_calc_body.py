#!/usr/bin/env python3.8

from random import randint, choice
RULES = 'What is the result of the expression?'


def random_number():
    rand_num = randint(1, 11)
    return rand_num


def random_operator():
    operators = ['+', '-', '*']
    operator_choice = choice(operators)
    return operator_choice


def calc(operator, rand_num_1, rand_num_2):
    if operator == '+':
        result = rand_num_1 + rand_num_2
    elif operator == '*':
        result = rand_num_1 * rand_num_2
    elif operator == '-':
        result = rand_num_1 - rand_num_2
    return result


def game_body():
    rand_num_1 = random_number()
    rand_num_2 = random_number()
    operator = random_operator()
    ask = [str(rand_num_1), operator, str(rand_num_2)]
    ask = ' '.join(str(_) for _ in ask)
    result = str(calc(operator, rand_num_1, rand_num_2))
    return ask, result
