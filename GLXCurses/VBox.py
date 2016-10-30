#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from Widget import Widget
from Box import Box

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class VBox(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.type = 'VBox'
        self.title = ''

        self.subwins_spacing = 0

        self.widget_to_display = {}
        self.widget_subwins = {}
        self.h_widget_list = {}
        self.widget_to_display_id = ''
        self.number_of_widget_to_display = 0


    # GLXC VBox Functions
    def draw(self):
        parent_height, parent_width = self.parent.get_size()
        parent_y, parent_x = self.parent.get_origin()
        self.widget = self.parent.widget.subwin(
            parent_height - (self.widget_spacing * 2),
            parent_width - (self.widget_spacing * 2),
            parent_y + self.widget_spacing,
            parent_x + self.widget_spacing
        )

        widget_height, widget_width = self.widget.getmaxyx()
        widget_y, widget_x = self.widget.getbegyx()

        # Check widgets to display
        if (widget_height >= self.number_of_widget_to_display + 1) and (
                    widget_width >= self.number_of_widget_to_display + 1):
            if len(self.widget_to_display.keys()):
                devised_box_size = widget_height / self.number_of_widget_to_display

                for ID in range(0, self.number_of_widget_to_display, 1):
                    if ID == 0:
                        self.widget_subwins[ID] = self.widget.subwin(
                            devised_box_size - self.subwins_spacing,
                            widget_width - self.subwins_spacing * 2,
                            widget_y + self.subwins_spacing,
                            widget_x + self.subwins_spacing
                        )
                    else:
                        self.widget_subwins[ID] = self.widget.subwin(
                            devised_box_size - (self.subwins_spacing / 2),
                            widget_width - self.subwins_spacing * 2,
                            widget_y + (devised_box_size * ID) + (self.subwins_spacing / 2),
                            widget_x + self.subwins_spacing
                        )

                    self.widget_subwins[ID].bkgdset(ord(' '), curses.color_pair(self.get_style_by_type('Debug') + ID))
                    self.widget_subwins[ID].bkgd(ord(' '), curses.color_pair(self.get_style_by_type('Debug') + ID))

                    # Check widgets to display
                    #self.h_widget_list[ID] = Box(self)
                    #self.h_widget_list[ID].add(self.h_widget_list[ID].draw())
                    #self.h_widget_list[ID].refresh()
                    # self.widget_to_display[ID].set_parent(self.h_widget_list[ID])
                    # self.h_widget_list[ID].widget = self.widget_subwins[ID]
                    # self.widget_to_display[ID].add_parent(self.h_widget_list[ID])
                    # self.h_widget_list[ID].set_parent(self.widget_subwins[ID])
                    # self.h_widget_list[ID].add(self.h_widget_list[ID])
                    # self.h_widget_list[ID].draw()
                    # self.widget_to_display[0].add
                    # self.widget_to_display[0].set_parent(self.widget_subwins[ID])
                    # self.widget_to_display[ID].draw()

    def set_title(self, title):
        self.title = title

    def add(self, widget):
        widget.set_parent(self)
        id_max = len(self.widget_to_display.keys())
        if bool(self.widget_to_display):
            self.widget_to_display[id_max] = widget
        else:
            self.widget_to_display[id_max + 1] = widget
        self.number_of_widget_to_display += 1
