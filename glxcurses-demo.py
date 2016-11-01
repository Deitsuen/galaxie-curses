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
    win1.set_title('My super Window 1')


    # Create a Window
    win5 = GLXCurses.Window()
    win5.set_title('My super Window 5')
    win5.set_decorated(1)
    win5.set_spacing(1)

    # Create a Window
    win6 = GLXCurses.Window()
    win6.set_title('My super Window 6')
    win6.set_decorated(1)
    win6.set_spacing(1)

    # Create a Label
    label1 =  GLXCurses.Label()
    label1.set_text('Super thing 1')
    label1.set_justify('RIGHT')
    #label1.set_position_type('CENTER')
    #label1.set_orientation('VERTICAL')

    label2 =  GLXCurses.Label()
    label2.set_text('La vie est belle tout pleins')
    label2.set_justify('RIGHT')
    #label2.set_position_type('CENTER')
    label2.set_orientation('VERTICAL')

    label3 =  GLXCurses.Label()
    label3.set_text('La vie est belle tout pleins')
    label3.set_justify('LEFT')
    #label3.set_position_type('CENTER')
    #label3.set_orientation('VERTICAL')

    progressbar = GLXCurses.ProgressBar()
    progressbar.set_text('Progress 1')
    progressbar.set_spacing(0)
    progressbar.set_show_text(1)
    progressbar.set_position_type('CENTER')
    #progressbar.set_position_type('CENTER')

    # Creat two Vertical Box contener
    vbox1 = GLXCurses.VBox()
    vbox2 = GLXCurses.VBox()

    # Creat a new Horizontal Box contener
    hbox = GLXCurses.HBox()
    hbox.add(vbox1)
    hbox.add(vbox2)

    hbox.subwins_spacing = 0
    vbox1.subwins_spacing = 0
    vbox2.subwins_spacing = 0
    # vbox1.add(label1)
    # vbox1.add(label2)
    # vbox1.add(label3)
    vbox1.add(progressbar)

    vbox2.add(win5)
    vbox2.add(win6)
    #hbox.set_spacing(0)
    hbox.add(win5)
    hbox.add(win6)

    win1.add(hbox)


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

