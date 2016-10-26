#!/usr/bin/env python
# -*- coding: utf-8 -*-
import GLXCurses
import sys
import curses
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'

if __name__ == '__main__':
    # Create the main Application
    app = GLXCurses.Application()

    # Create a Menu
    menu = GLXCurses.MenuModel(app)

    # Create a Window
    win = GLXCurses.Window(app)

    # Add Everything inside the Application
    app.set_menubar(menu)
    app.add_window(win)

    # Main loop
    while True:
        input_event = app.getch()
        if curses.KEY_RESIZE:
            app.refresh()
            pass
        elif input_event == ord('q'):
            break
        else:
            pass

    # App Close
    app.close()
    # THE END
    sys.exit(0)

