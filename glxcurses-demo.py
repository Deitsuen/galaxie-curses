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
    menu = GLXCurses.MenuModel()
    menu.app_info_label = app.get_name()

    # Create a Window
    win1 = GLXCurses.Window()
    win1.title = 'My super Window 1'

    # Create a Window
    win2 = GLXCurses.Window()
    win2.title = 'My super Window 2'
    win2.set_decorated(1)
    win2.set_spacing(1)

    # Create a Window
    win3 = GLXCurses.Window()
    win3.title = 'My super Window 3'
    win3.set_decorated(0)
    win3.set_spacing(1)

    vbox = GLXCurses.VBox()

    # Create a Window
    win4 = GLXCurses.Window()
    win4.title = 'My super Window 4'
    win4.set_decorated(1)
    win4.set_spacing(1)

    # Create a Window
    win5 = GLXCurses.Window()
    win5.title = 'My super Window 5'
    win5.set_decorated(1)
    win5.set_spacing(1)

    # Create a Window
    win6 = GLXCurses.Window()
    win6.title = 'My super Window 6'
    win6.set_decorated(1)
    win6.set_spacing(1)

    win1.add(win2)
    win2.add(win3)

    win3.add(vbox)

    vbox.subwins_spacing = 1
    vbox.add(win4)
    vbox.add(win5)
    vbox.add(win6)

    # Creat a Status Bar
    toolbar = GLXCurses.Toolbar()
    toolbar.button_list = [
        'Help',
        'Options',
        '',
        '',
        '',
        '',
        '',
        '',
        'Menu',
        'Quit'
    ]

    # Add Everything inside the Application
    app.add_menubar(menu)
    app.add_window(win1)
    app.add_statusbar(GLXCurses.Statusbar())
    app.add_toolbar(toolbar)

    # Main loop
    count = 1
    app.refresh()
    while True:
        input_event = app.getch()
        if curses.KEY_RESIZE:
            screen_height, screen_width = app.screen.getmaxyx()
            message_text = ''
            message_text += 'Screen Size:'
            message_text += str(app.get_parent_size())
            message_text += ' '
            message_text += 'Win:1'
            message_text += ' '
            message_text += str(win1.get_size())
            message_text += ' '
            message_text += 'Win2:'
            message_text += ' '
            message_text += str(win2.get_size())
            message_text += ' '
            message_text += 'Win3:'
            message_text += ' '
            message_text += str(win3.get_size())
            message_text += ' '
            message_text += 'Win4:'
            message_text += ' '
            message_text += str(win4.get_size())
            message_text += ' '
            message_text += 'Win5:'
            message_text += ' '
            message_text += str(win5.get_size())
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

