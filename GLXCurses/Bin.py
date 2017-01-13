#!/usr/bin/env python
# -*- coding: utf-8 -*-
from GLXCurses import Container

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Bin(Container):
    def destroy(self):
        raise NotImplementedError

    def __init__(self):
        Container.__init__(self)
        self.child = None

    def get_child(self):
        return self.child
