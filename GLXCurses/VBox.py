#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


def resize_text(text, max_width, separator='~'):
    if max_width < len(text):
        return text[:(max_width / 2) - 1] + separator + text[-max_width / 2:]
    else:
        return text


class VBox(object):
    def __init__(self, parent):
        self.title = ''
        self.decorated = 0
        self.spacing = 0
        self.subwins_spacing = 0
        self.parent_spacing = 0

        self.widget = ''
        self.widget_to_display = {}
        self.widget_subwins = {}
        self.widget_to_display_id = ''
        self.number_of_widget_to_display = 0
        self.parent = parent

        self.draw()

    # Common Widget mandatory
    def get(self):
        return self.widget

    def get_origin(self):
        return self.widget.getbegyx()

    def get_size(self):
        return self.widget.getmaxyx()

    def get_spacing(self):
        return self.spacing

    def get_parent(self):
        return self.parent

    def get_parent_size(self):
        return self.parent.widget.getmaxyx()

    def get_parent_origin(self):
        return self.parent.widget.getbegyx()

    def set_parent(self, parent):
        self.parent = parent

    def get_parent_spacing(self):
        return self.parent.spacing

    def remove_parent(self):
        self.parent = ''

    # GLXC VBox Functions
    def draw(self):
        parent_height, parent_width = self.parent.get_size()
        parent_y, parent_x = self.parent.get_origin()
        self.widget = self.parent.widget.subwin(
            parent_height - (self.spacing * 2),
            parent_width - (self.spacing * 2),
            parent_y + self.spacing,
            parent_x + self.spacing
        )

        widget_height, widget_width = self.widget.getmaxyx()
        widget_y, widget_x = self.widget.getbegyx()

        # Check widgets to display
        if len(self.widget_to_display.keys()):
            devised_box_size = widget_height / self.number_of_widget_to_display

            for count in range(0, self.number_of_widget_to_display, 1):
                if count == 0:
                    self.widget_subwins[count] = self.widget.subwin(
                        devised_box_size - self.subwins_spacing,
                        widget_width - self.subwins_spacing * 2,
                        widget_y + self.subwins_spacing,
                        widget_x + self.subwins_spacing
                    )
                else:
                    self.widget_subwins[count] = self.widget.subwin(
                        devised_box_size - (self.subwins_spacing/2),
                        widget_width - self.subwins_spacing * 2,
                        widget_y + (devised_box_size * count) + (self.subwins_spacing/2),
                        widget_x + self.subwins_spacing
                    )
                if (widget_height >= self.number_of_widget_to_display +1) and (widget_width >= self.number_of_widget_to_display +1):
                    self.widget_subwins[count].bkgdset(ord(' '), curses.color_pair(10 + count))
                    self.widget_subwins[count].bkgd(ord(' '), curses.color_pair(10 + count))
                    #self.widget_to_display[0].set_parent(self.widget_subwins[count])
                #self.widget_to_display[count].draw()



    def set_title(self, title):
        self.title = title

    def set_decorated(self, boolean):
        self.decorated = int(boolean)

    def add(self, widget):
        id_max = len(self.widget_to_display.keys())
        if bool(self.widget_to_display):
            self.widget_to_display[id_max] = widget
        else:
            self.widget_to_display[id_max + 1] = widget
        self.number_of_widget_to_display += 1

    def refresh(self):
        self.draw()



