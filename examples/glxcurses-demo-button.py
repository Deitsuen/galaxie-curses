#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
# Require when you haven't GLXCurses as default Package
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))
import GLXCurses
import curses
import logging

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'

if __name__ == '__main__':
    logging.basicConfig(filename='/tmp/galaxie-curses.log',
                        level=logging.DEBUG,
                        format='%(asctime)s, %(levelname)s, %(message)s')
    logging.info('Started glxcurses-demo')

    # Create the main Application
    app = GLXCurses.Application()
    app.set_name('GLXCurses Buttons Demo')

    # Create a Menu
    menu = GLXCurses.MenuBar()
    menu.app_info_label = app.get_name()

    # Create Buttons
    Button1 = GLXCurses.Button()
    Button1.set_text('Button')

    RadioButton1 = GLXCurses.RadioButton()
    RadioButton1.set_text('RadioButton')

    CheckButton1 = GLXCurses.CheckButton()
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
    label_press_q.set_text('Press "q" key to exit ...')
    label_press_q.set_alignment(0.5, 0.3)
    label_press_q.override_color('yellow')

    # Create a main Vertical Box
    vbox_main = GLXCurses.VBox()
    vbox_main.pack_end(hline)
    vbox_main.pack_end(hbox)
    vbox_main.pack_end(hline)
    vbox_main.pack_end(label_press_q)

    # Create the main Window
    win_main = GLXCurses.Window()
    win_main.add(vbox_main)

    # Create a Status Bar
    statusbar = GLXCurses.Statusbar()
    context_id = statusbar.get_context_id("example")

    def handle_keys(self, event_signal, *event_args):
        logging.debug('HANDLE KEY: '+str(event_args[0]))

        if event_args[0] == curses.KEY_F5:
            app.set_is_focus(Button1)

        if event_args[0] == curses.KEY_F6:
            Button1.set_sensitive(not Button1.get_sensitive())

        # Keyboard temporary thing
        if event_args[0] == ord('q'):
            # Everything have a end, the main loop too ...
            GLXCurses.mainloop.quit()

    def on_click(self, event_signal, event_args=None):
        if event_args is None:
            event_args = dict()
        statusbar.push(context_id, '')
        if event_args['id'] == Button1.get_widget_id():
            statusbar.push(context_id, event_args['label'] + ' ' + event_signal)
        if event_args['id'] == RadioButton1.get_widget_id():
            if RadioButton1.get_active():
                statusbar.push(context_id, RadioButton1.get_text() + ' ' + 'is active')
            else:
                statusbar.push(context_id, RadioButton1.get_text() + ' ' + 'is not active')

        if event_args['id'] == CheckButton1.get_widget_id():
            if CheckButton1.get_active():
                statusbar.push(context_id, CheckButton1.get_text() + ' ' + 'is active')
            else:
                statusbar.push(context_id, CheckButton1.get_text() + ' ' + 'is not active')

    # Add Everything inside the Application
    app.add_menubar(menu)
    app.add_window(win_main)
    app.add_statusbar(statusbar)
    # Signal
    app.connect('BUTTON1_CLICKED', on_click)
    app.connect('BUTTON1_RELEASED', on_click)
    app.connect('CURSES', handle_keys)

    # Main loop
    GLXCurses.mainloop.run()

    # THE END
    sys.exit(0)
