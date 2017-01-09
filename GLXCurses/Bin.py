#!/usr/bin/env python
# -*- coding: utf-8 -*-
import GLXCurses

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Bin(GLXCurses.Container):
    def __init__(self):
        GLXCurses.Container.__init__(self)
        self.child = None

    def get_child(self):
        return self.child
