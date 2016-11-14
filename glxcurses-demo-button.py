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
    app.set_name('Galaxie-Curse Demo')

    # # Create a Menu
    # menu = GLXCurses.MenuModel()
    # menu.app_info_label = app.get_name()

    # Create the main Window
    win_main = GLXCurses.Window()
    win_main.set_title('Button Demo')

    # Create a Window
    # win6 = GLXCurses.Window()
    # win6.set_title('Label Widget')
    # win6.set_decorated(1)
    # win6.set_spacing(1)

    # Creat Button
    Button1 = GLXCurses.Button()
    Button1.set_text('Button1')

    RadioButton1 = GLXCurses.RadioButton()
    RadioButton1.set_text('RadioButton1')

    # Creat a new Horizontal Box contener
    hbox = GLXCurses.HBox()
    hbox.subwins_spacing = 0

    hbox.add(Button1)
    hbox.add(RadioButton1)
    # HSepartor = GLXCurses.HSeparator()
    # HSepartor.set_spacing(0)
    #VSepartor.set_position_type('center')
    # Creat two Vertical Box contener
    # vbox1 = GLXCurses.VBox()
    # vbox1.subwins_spacing = 0
    # vbox1.add(hbox)
    # vbox1.add(HSepartor)
    # vbox1.add(RadioButton1)

    # vbox1.add(win6)




    win_main.add(hbox)
    #win_main.add(RadioButton1)

    # Creat a Status Bar
    statusbar = GLXCurses.Statusbar()
    # Add Everything inside the Application
    # app.add_menubar(menu)
    app.add_window(win_main)
    app.add_statusbar(statusbar)

    # Main loop
    app.refresh()
    while True:
        message_text = ''
        input_event = app.getch()
        if curses.KEY_RESIZE:
            message_text += 'Screen Size:'
            message_text += str(app.get_parent_size())
            message_text += ' '
            statusbar.push(message_text)
            app.refresh()

        if input_event == curses.KEY_MOUSE:
            event = curses.getmouse()
            for Button in [RadioButton1, Button1]:
                if Button.mouse_event(event):
                    message_text += Button.get_states_list()
                    message_text += ' '
                    statusbar.push(message_text)
                    app.refresh()

            # if Button1.key_pressed(input_event):
            #     pass

        if input_event == ord('q'):
            break

    # App Close
    app.close()
    # THE END
    sys.exit(0)
