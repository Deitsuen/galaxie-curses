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
from GLXCurses import glxc

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
    app.set_name('GLXCurses Dev Demo')

    # Create a main Vertical Box
    vbox_main = GLXCurses.VBox()

    # Create the main Window
    win_main = GLXCurses.Window()
    win_main.add(vbox_main)

    def handle_keys(self, event_signal, *event_args):
        logging.debug('HANDLE KEY: '+str(event_args[0]))

        # Keyboard temporary thing
        if event_args[0] == ord('q'):
            # Everything have a end, the main loop too ...
            GLXCurses.mainloop.quit()

    # Add Everything inside the Application
    app.add_window(win_main)

    # Signal

    app.connect('CURSES', handle_keys)

    # Main loop
    GLXCurses.mainloop.run()

    # THE END
    sys.exit(0)
