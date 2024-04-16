#!/usr/bin/env python3

from brain_games.games.engine.Engine_game import en_game
from brain_games.games import brain_even_body


def main():
    en_game(brain_even_body.brain_even)


if __name__ == '__main__':
    main()
