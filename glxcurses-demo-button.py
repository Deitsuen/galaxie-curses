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
    Button1.set_application(app)
    Button1.set_text('Button')

    RadioButton1 = GLXCurses.RadioButton()
    RadioButton1.set_application(app)
    RadioButton1.set_text('RadioButton')

    CheckButton1 = GLXCurses.CheckButton()
    CheckButton1.set_application(app)
    CheckButton1.set_text('CheckButton')

    # Create a new Horizontal Box contener
    hbox = GLXCurses.HBox()
    hbox.set_spacing(1)

    hbox.pack_end(Button1)
    hbox.pack_end(RadioButton1)
    hbox.pack_end(CheckButton1)

    # Create a Horizontal Separator and a Label
    hline = GLXCurses.HSeparator()

    label_press_q = GLXCurses.Label()
    label_press_q.set_text('Press q key to exit ...')

    # Create a main Vertical Box
    vbox_main = GLXCurses.VBox()
    vbox_main.pack_end(hline)
    vbox_main.pack_end(hbox)
    vbox_main.pack_end(hline)
    vbox_main.pack_end(label_press_q)

    # Create the main Window
    win_main = GLXCurses.Window()
    win_main.set_title('GLXCurses Buttons Demo.')
    win_main.add(vbox_main)

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
        if input_event == -1:
            continue

        if curses.KEY_RESIZE:
            message_text += 'Screen Size:'
            message_text += str(app.get_parent_size())
            message_text += ' '
            statusbar.push(message_text)
            app.refresh()

        if input_event == curses.KEY_MOUSE:
            event = curses.getmouse()
            for Button in [Button1,
                           CheckButton1,
                           RadioButton1]:
                if Button.mouse_event(event):
                    message_text += Button.get_text()
                    message_text += ':('
                    message_text += Button.get_states()
                    message_text += ')'
                    statusbar.push(message_text)
                    app.refresh()

        if input_event == ord('q'):
            break

    # App Close
    app.close()
    # THE END
    sys.exit(0)
