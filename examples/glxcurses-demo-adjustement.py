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
    app.set_name('GLXCurses Adjustement Demo')

    # Create a Menu
    menu = GLXCurses.MenuBar()
    menu.app_info_label = app.get_name()


    # Create Buttons
    # value, lower, upper, step_increment, page_increment, page_size
    # value, lower, upper, step_increment, page_increment, page_size
    Button1 = GLXCurses.Button()
    Button1.set_text('value +')

    Button2 = GLXCurses.Button()
    Button2.set_text('lower +')

    Button3 = GLXCurses.Button()
    Button3.set_text('upper +')

    Button4 = GLXCurses.Button()
    Button4.set_text('step_increment +')

    Button5 = GLXCurses.Button()
    Button5.set_text('page_increment +')

    Button6 = GLXCurses.Button()
    Button6.set_text('page_size +')

    ######################
    Button7 = GLXCurses.Button()
    Button7.set_text('value -')

    Button8 = GLXCurses.Button()
    Button8.set_text('lower -')

    Button9 = GLXCurses.Button()
    Button9.set_text('upper -')

    Button10 = GLXCurses.Button()
    Button10.set_text('step_increment -')

    Button11 = GLXCurses.Button()
    Button11.set_text('page_increment -')

    Button12 = GLXCurses.Button()
    Button12.set_text('page_size -')



    # Create a new Horizontal Box contener
    hbox_line_1 = GLXCurses.HBox()
    hbox_line_1.set_spacing(1)

    hbox_line_1.pack_end(Button1)
    hbox_line_1.pack_end(Button2)
    hbox_line_1.pack_end(Button3)
    hbox_line_1.pack_end(Button4)
    hbox_line_1.pack_end(Button5)
    hbox_line_1.pack_end(Button6)

    # Create a new Horizontal Box contener
    hbox_line_2 = GLXCurses.HBox()
    hbox_line_2.set_spacing(1)

    hbox_line_2.pack_end(Button7)
    hbox_line_2.pack_end(Button8)
    hbox_line_2.pack_end(Button9)
    hbox_line_2.pack_end(Button10)
    hbox_line_2.pack_end(Button11)
    hbox_line_2.pack_end(Button12)

    # Create a Horizontal Separator and a Label
    hline = GLXCurses.HSeparator()

    label_press_q = GLXCurses.Label()
    label_press_q.set_text('Press "q" key to exit ...')
    label_press_q.set_alignment(0.5, 0.3)
    label_press_q.override_color('yellow')

    label_adjustement = GLXCurses.Label()
    label_adjustement.set_alignment(0.5, 0.7)
    label_adjustement.set_text('coucou')

    # Creat the adjustement
    adjustement = GLXCurses.Adjustment()

    def update_label():
        label_adjustement.set_text(
            'value: {0}, lower: {1}, upper: {2}, step_increment: {3}, page_increment: {4}, page_size: {5}, min_incr: {6}'.format(
                adjustement.get_value(),
                adjustement.get_lower(),
                adjustement.get_upper(),
                adjustement.get_step_increment(),
                adjustement.get_page_increment(),
                adjustement.get_page_size(),
                adjustement.get_minimum_increment()
            ))

    update_label()



    # Create a main Vertical Box
    vbox_main = GLXCurses.VBox()
    vbox_main.pack_end(label_adjustement)
    vbox_main.pack_end(hline)
    vbox_main.pack_end(hbox_line_1)
    vbox_main.pack_end(hbox_line_2)
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
            adjustement.set_value(adjustement.get_value() + adjustement.get_minimum_increment())
            update_label()
        if event_args['id'] == Button2.get_widget_id():
            statusbar.push(context_id, event_args['label'] + ' ' + event_signal)
            adjustement.set_lower(0.3)
            update_label()
        if event_args['id'] == Button3.get_widget_id():
            statusbar.push(context_id, event_args['label'] + ' ' + event_signal)
            adjustement.set_upper(adjustement.get_upper() + adjustement.get_step_increment())
            update_label()
        if event_args['id'] == Button4.get_widget_id():
            statusbar.push(context_id, event_args['label'] + ' ' + event_signal)
            adjustement.set_step_increment(adjustement.get_step_increment() + 0.1)
            update_label()


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
