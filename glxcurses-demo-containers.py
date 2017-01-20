#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import GLXCurses

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'

if __name__ == '__main__':

    # Create the main Application
    app = GLXCurses.Application()
    app.set_name('Galaxie-Curse Container Demo')

    # Create a Window
    win_main = GLXCurses.Window()
    #win_main.set_decorated(1)

    # Create a Frame
    frame1 = GLXCurses.Frame()
    frame1.set_label('Galaxie-Curse Container Frame Demo')
    frame1.set_spacing(1)
    frame1.set_label_align(0.5, 0.0)

    win_main.add(frame1)

    def handle_keys(self, event_signal, *event_args):
        if event_args[0] == ord('q'):
            # Everything have a end, the main loop too ...
            GLXCurses.mainloop.quit()

    # Add Everything inside the Application
    app.add_window(win_main)

    # Signal
    app.connect('CURSES', handle_keys)

    # Main loop start
    GLXCurses.mainloop.run()

    # THE END
    sys.exit(0)
