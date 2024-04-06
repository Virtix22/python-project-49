#!/usr/bin/env python3

import random
import prompt
from brain_games.module.welcome import welcome_user

#def welcome_user():
 #   print('Welcome to the Brain Games!')
  #  name = prompt.string('May I have your name? ')
   # print(f'Hello, {name}!')
    #return name


def even(name):
    print('Answer "yes" if the number is even, otherwise answer "no"')
    i = 0
    while i < 3:
        random_number = random.randint(0, 10001)
        print(f'Question: {random_number}')
        choice = prompt.string('Your answer? ')
        if random_number % 2 == 0 and choice == 'yes' or random_number % 2 != 0 and choice == 'no':
            print('Correct!')
            i+=1
        elif random_number % 2 == 0 and choice == 'no':
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            break
        elif random_number % 2 != 0 and choice == 'yes':
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}')


def main():
    name = welcome_user()
    even(name)


if __name__ == '__main__':
    main()