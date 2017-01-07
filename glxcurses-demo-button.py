#!/usr/bin/env python
# -*- coding: utf-8 -*-
import GLXCurses
import sys
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

    def on_resize():
        app.get_screen().refresh()

    def handle_keys(self, event_signal, *event_args):
        logging.debug('HANDLE KEY: '+str(event_args[0]))

        if event_args[0] == curses.KEY_F5:
            app.set_is_focus(Button1)

        if event_args[0] == curses.KEY_F6:
            Button1.set_sensitive(not Button1.get_sensitive())

        # Keyboard temporary thing
        if event_args[0] == curses.KEY_F10 or event_args[0] == ord('q'):
            app.stop()

    def on_click(self, event_signal, event_args=dict()):
        #logging.debug(str(event_signal) + ' ' + str(event_args))
        if event_args['id'] == Button1.get_widget_id():
            statusbar.push('Stopping every operation\'s')
            app.stop()

    app.connect('RESIZE', on_resize)
    app.connect('BUTTON1_CLICKED', on_click)
    app.connect('BUTTON1_RELEASED', on_click)
    app.connect('CURSES', handle_keys)

    # Main loop
    app.start()
    # THE END
    sys.exit(0)
