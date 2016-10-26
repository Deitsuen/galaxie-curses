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
    Application = GLXCurses.Application()
    MenuModel = GLXCurses.MenuModel(Application)
    Application.set_menubar(MenuModel)
    Application.refresh()

    # Main loop
    while True:
        input_event = Application.getch()
        if curses.KEY_RESIZE:
            Application.refresh()
            pass
        if input_event == ord('q'):
            break
        elif input_event == ord('q'):
            break
        else:
            pass
        #Application.refresh()
    Application.close()
    # THE END
    sys.exit(0)

