#!/usr/bin/env python
# -*- coding: utf-8 -*-
import GLXCurses
import sys
import curses
from random import randint
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'

if __name__ == '__main__':

    # Create the main Application
    app = GLXCurses.Application()
    app.set_name('Galaxie-Curse Container Demo')

    # Create a Window
    win_main = GLXCurses.Window()
    win_main.set_decorated(1)

    app.add_window(win_main)

    # Main loop
    count = 1
    app.refresh()
    while True:
        message_text = ''
        input_event = app.getch()
        if curses.KEY_RESIZE:
            message_text += 'Screen Size:'
            message_text += str(app.get_parent_size())
            message_text += ' '
            app.refresh()
        if input_event == ord('q'):
            app.refresh()
            break
        count += 1

    # App Close
    app.close()
    # THE END
    sys.exit(0)