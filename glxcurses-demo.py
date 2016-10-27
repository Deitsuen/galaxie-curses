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

    # Creat a Status Bar
    toolbar = GLXCurses.Toolbar(app)

    # Add Everything inside the Application
    app.add_menubar(menu)
    app.add_window(win)
    app.add_statusbar(statusbar)
    app.add_toolbar(toolbar)

    # Main loop
    count = 1
    while True:
        input_event = app.getch()
        if curses.KEY_RESIZE:
            screen_height, screen_width = app.screen.getmaxyx()
            message_text = ''
            message_text += 'Screen Size:'
            message_text += ' '
            message_text += str(screen_width)
            message_text += 'x'
            message_text += str(screen_height)
            statusbar.push(message_text)
            app.refresh()
            pass
        if input_event == ord('q'):
            break
        count += 1

    # App Close
    app.close()
    # THE END
    sys.exit(0)

