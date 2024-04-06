#!/usr/bin/env python3

from brain_games.cli import welcome_user


def greetings():
    print('Welcome to the Brain Games!')


def main():
    greetings()
    welcome_user()


if __name__ == '__main__':
    main()
    