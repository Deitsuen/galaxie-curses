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
    app.set_name('GLXCurses Entry Demo')

    # Create a Menu
    menu = GLXCurses.MenuBar()
    menu.app_info_label = app.get_name()

    # Create Buttons
    Entry = GLXCurses.Entry()
    Entry.set_text('TEST')

    # Create a new Horizontal Box contener
    hbox = GLXCurses.HBox()
    hbox.set_spacing(1)
    hbox.pack_end(Entry)

    # Create a Horizontal Separator and a Label
    hline = GLXCurses.HSeparator()

    label = GLXCurses.Label()
    label.set_text('Press "q" key to exit ... What about you arrows\'s key\'s')
    label.set_single_line_mode(True)
    label.set_justify('center')
    label.set_alignment(0.5, 0.3)
    label.override_color('yellow')

    # Create a main Vertical Box
    vbox_main = GLXCurses.VBox()
    vbox_main.pack_end(hline)
    vbox_main.pack_end(hbox)
    vbox_main.pack_end(hline)
    vbox_main.pack_end(label)

    # Create the main Window
    win_main = GLXCurses.Window()
    win_main.add(vbox_main)

    # Create a Status Bar
    statusbar = GLXCurses.StatusBar()
    context_id = statusbar.get_context_id("example")
    signal_context_id = statusbar.get_context_id("SIGNAL")
    entry_context_id = statusbar.get_context_id("ENTRY")
    arrow_pressed_context_id = statusbar.get_context_id("ARROW_PRESSED")


    def handle_keys(self, event_signal, *event_args):
        statusbar.remove_all(arrow_pressed_context_id)
        statusbar.push(arrow_pressed_context_id, 'HANDLE KEY: ' + str(event_args[0]))
        position = 0
        if event_args[0] == curses.KEY_F5:
            if app.get_is_focus() == Entry.id:
                app.set_is_focus(None)

            else:
                app.set_is_focus(Entry)

        if event_args[0] == curses.KEY_F6:
            Entry.set_sensitive(not Entry.get_sensitive())

        if event_args[0] == curses.KEY_UP:
            x, y = label.get_alignment()
            y -= 0.033
            label.set_alignment(x, y)

        if event_args[0] == curses.KEY_DOWN:
            x, y = label.get_alignment()
            y += 0.033
            label.set_alignment(x, y)
        # if event_args[0] == curses.KEY_RIGHT:
        #     x, y = label.get_alignment()
        #     x += 0.033
        #     label.set_alignment(x, y)
        # if event_args[0] == curses.KEY_LEFT:
        #     x, y = label.get_alignment()
        #     x -= 0.033
        #     label.set_alignment(x, y)

        for alphabet in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:

            if event_args[0] == ord('q'):
                # Everything have a end, the main loop too ...
                GLXCurses.mainloop.quit()

            if event_args[0] == ord(alphabet):
                if app.get_is_focus():
                    Entry.add_text(alphabet)

        if event_args[0] == curses.KEY_BACKSPACE:
            Entry.remove_text()

        if event_args[0] == ord(' '):
            Entry.add_text(' ')
        if event_args[0] == curses.KEY_RIGHT:
            Entry.move_cursor('forward')

        if event_args[0] == curses.KEY_LEFT:
            Entry.move_cursor('backward')


    def on_click(self, event_signal, event_args=None):
        if event_args is None:
            event_args = dict()
        if event_args['id'] == app.get_is_focus():
            statusbar.remove_all(entry_context_id)
            statusbar.push(entry_context_id, event_args['label'] + ' ' + event_signal)


    def signal_event(self, event_signal, event_args=None):
        if event_args is None:
            event_args = dict()

            # Crash AUTO
            # statusbar.push(
            #    signal_context_id, "{0}: {1}".format(event_signal, event_args)
            # )


    # Add Everything inside the Application
    app.add_menubar(menu)
    app.add_window(win_main)
    # app.remove_window(win_main)
    app.add_statusbar(statusbar)

    # Event's and Signals
    app.connect('BUTTON1_CLICKED', on_click)  # Mouse Button
    app.connect('BUTTON1_RELEASED', on_click)  # Mouse Button
    app.connect('CURSES', handle_keys)  # Keyboard
    app.connect('SIGNALS', signal_event)  # Something it emit a signal

    # Main loop
    GLXCurses.mainloop.run()

    # THE END
    sys.exit(0)
