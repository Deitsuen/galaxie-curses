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

    # Create Buttons
    Button1 = GLXCurses.Button()
    Button1.set_text('Button')

    RadioButton1 = GLXCurses.RadioButton()
    RadioButton1.set_text('RadioButton')

    CheckButton1 = GLXCurses.CheckButton()
    CheckButton1.set_text('CheckButton')

    # Creat a new Horizontal Box contener
    hbox = GLXCurses.HBox()
    hbox.set_spacing(1)

    hbox.add(Button1)
    hbox.add(RadioButton1)
    hbox.add(CheckButton1)

    # Create the main Window
    win_main = GLXCurses.Window()
    win_main.set_title('Press q key for exit.')
    win_main.add(hbox)

    # Create a Status Bar
    statusbar = GLXCurses.Statusbar()
    # Add Everything inside the Application
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
            if RadioButton1.mouse_event(event):
                message_text += RadioButton1.get_states()
                message_text += ' '
                statusbar.push(message_text)
                app.refresh()
            elif Button1.mouse_event(event):
                message_text += Button1.get_states()
                message_text += ' '
                statusbar.push(message_text)
                app.refresh()
            elif CheckButton1.mouse_event(event):
                message_text += CheckButton1.get_states()
                message_text += ' '
                statusbar.push(message_text)
                app.refresh()

        if input_event == ord('q'):
            break

    # App Close
    app.close()
    # THE END
    sys.exit(0)
