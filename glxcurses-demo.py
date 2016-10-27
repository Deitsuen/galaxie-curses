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
    app.set_name('Galaxie-Curse Demo')

    # Create a Menu
    menu = GLXCurses.MenuModel(app)

    # Create a Window
    win = GLXCurses.Window(app)
    win.title = 'My super Window'
    win.set_decorated(1)

    # Creat a Status Bar
    statusbar = GLXCurses.Statusbar(app)
    statusbar.push('Bonjour je suis un message')

    # Add Everything inside the Application
    app.add_menubar(menu)
    app.add_window(win)
    app.add_statusbar(statusbar)

    # Main loop
    while True:
        input_event = app.getch()
        if curses.KEY_RESIZE:
            app.refresh()
            pass
        if input_event == ord('q'):
            break

    # App Close
    app.close()
    # THE END
    sys.exit(0)

