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

    # Creat a new Vertical Box contener
    vbox = GLXCurses.VBox()

    # Create a Window
    label1 =  GLXCurses.Label()
    label1.set_text('La vie est belle tout pleins')
    label1.set_justify('LEFT')
    #label1.set_position_type('CENTER')
    label1.set_orientation('VERTICAL')

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

    win1.add(vbox)

    vbox.subwins_spacing = 1
    vbox.add(label1)
    vbox.set_spacing(0)
    #vbox.add(win5)
    #vbox.add(win6)

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
    statusbar = GLXCurses.Statusbar()
    # Add Everything inside the Application
    app.add_menubar(menu)
    app.add_window(win1)
    app.add_statusbar(statusbar)
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

