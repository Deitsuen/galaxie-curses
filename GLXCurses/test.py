#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses
import itertools


def init_curses_pairs():
    # Prepare a list with the palette
    curses_colors = list()
    curses_colors.append(curses.COLOR_BLACK)
    curses_colors.append(curses.COLOR_WHITE)
    curses_colors.append(curses.A_BOLD | curses.COLOR_WHITE)
    curses_colors.append(curses.COLOR_BLUE)
    curses_colors.append(curses.COLOR_RED)
    curses_colors.append(curses.COLOR_MAGENTA)
    curses_colors.append(curses.COLOR_CYAN)
    curses_colors.append(curses.COLOR_GREEN)
    curses_colors.append(curses.COLOR_YELLOW)
    curses_colors.append(curses.A_BOLD | curses.COLOR_YELLOW)
    curses_colors.append(curses.A_BOLD | curses.COLOR_RED)

    # Prepare a Combination List for each Color
    curses_colors_pairs = list(itertools.product(curses_colors, curses_colors))
    # curses_colors_pairs = list()
    curses_colors_pairs.insert(0, [curses.COLOR_BLACK, curses.COLOR_WHITE])
    #curses_colors_pairs = list()

    # Add Default setting and mer
    #curses_colors_pairs.append([black, white])
    #curses_colors_pairs += fb

    index = 1
    for I in curses_colors_pairs:
        #curses.init_pair(index, I[0], I[1])
        index += 1
    index = 0
    for I in curses_colors_pairs:
        print("curses.init_pair(" + str(index) + ", " + str(I[0]) + ", " + str(I[1]) + ")")
        index += 1

    def get_int_to_color(integer):
        if integer == 0:
            return 'BLACK'
        elif integer == 7:
            return 'GRAY'
        elif integer == 2097159:
            return 'WHITE'
        elif integer == 4:
            return 'BLUE'
        elif integer == 1:
            return 'RED'
        elif integer == 5:
            return 'MAGENTA'
        elif integer == 6:
            return 'CYAN'
        elif integer == 2:
            return 'GREEN'
        elif integer == 3:
            return 'ORANGE'
        elif integer == 2097155:
            return 'YELLOW'
        elif integer == 2097153:
            return 'PINK'

    def get_color_to_int(color):
        if color == 'BLACK':
            return curses.COLOR_BLACK
        if color == 'GRAY':
            return curses.COLOR_WHITE
        if color == 'WHITE':
            return curses.A_BOLD | curses.COLOR_WHITE
        if color == 'BLUE':
            return curses.COLOR_BLUE
        if color == 'RED':
            return curses.COLOR_RED
        if color == 'MAGENTA':
            return curses.COLOR_MAGENTA
        if color == 'CYAN':
            return curses.COLOR_CYAN
        if color == 'GREEN':
            return curses.COLOR_GREEN
        if color == 'ORANGE':
            return curses.COLOR_YELLOW
        if color == 'YELLOW':
            return curses.A_BOLD | curses.COLOR_YELLOW
        if color == 'PINK':
            return curses.A_BOLD | curses.COLOR_RED

    index = 0
    for I in curses_colors_pairs:
        print("Index=" + str(index) + " FG=" + str(get_int_to_color(I[0])) + " BG=" + str(get_int_to_color(I[1])))
        index += 1



if __name__ == '__main__':
    init_curses_pairs()
