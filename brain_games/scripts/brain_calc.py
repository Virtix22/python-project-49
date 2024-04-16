#!/usr/bin/env python3

from brain_games.games.engine.Engine_game import en_game
from brain_games.games import brain_calc_body


def main():
    en_game(brain_calc_body.brain_calc)


if __name__ == '__main__':
    main()
