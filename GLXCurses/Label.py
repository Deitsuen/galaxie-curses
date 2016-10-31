#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from Widget import Widget
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


def resize_text(text, max_width, separator='~'):
    if max_width < len(text):
        return text[:(max_width / 2) - 1] + separator + text[-max_width / 2:]
    else:
        return text


class Label(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.type = 'Label'

        # Internal Widget Setting
        self.text = ''

        # Justification: LEFT, RIGHT, CENTER
        self.justification = 'CENTER'

        # Orientation: HORIZONTAL, VERTICAL
        self.orientation = 'HORIZONTAL'

        # PositionType: CENTER, TOP, BOTTOM
        self.position_type = 'CENTER'

    def draw(self):
        parent_height, parent_width = self.parent.get_size()
        parent_y, parent_x = self.parent.get_origin()
        self.parent_spacing = self.parent.get_spacing()

        drawing_area = self.parent.widget.subwin(
                parent_height - (self.widget_spacing * 2),
                parent_width - (self.widget_spacing * 2),
                parent_y + self.widget_spacing,
                parent_x + self.widget_spacing
        )

        self.draw_in_area(drawing_area)

    def draw_in_area(self, drawing_area):

        self.widget = drawing_area

        widget_height, widget_width = drawing_area.getmaxyx()
        widget_y, widget_x = drawing_area.getbegyx()
        min_size_width = (self.widget_spacing * 2) + self.widget_spacing
        min_size_height = (self.widget_spacing * 2)
        if (widget_height >= min_size_height) and (widget_width >= min_size_width):
            if curses.has_colors():
                drawing_area.bkgdset(ord(' '), curses.color_pair(self.get_style_by_type(self.type)))
                drawing_area.bkgd(ord(' '), curses.color_pair(self.get_style_by_type(self.type)))
                for I in range(widget_y, widget_height):
                    drawing_area.addstr(
                        I,
                        0,
                        str(' ' * int(widget_width - 1)),
                        curses.color_pair(self.get_style_by_type(self.type))
                    )
                    drawing_area.insstr(
                        I,
                        int(widget_width - 1),
                        str(' '),
                        curses.color_pair(self.get_style_by_type(self.type))
                    )
            # Compute text position

            if not self.text == '':
                text_len = len(self.text)
                text_half_len = text_len / 2
                text_have_width = (text_len + self.get_spacing() <= widget_width)
                text_have_height = (1 + self.get_spacing() * 2 <= widget_height-1)
                if text_have_width and text_have_height:
                    # Check Justification
                    if self.justification == 'CENTER':
                        x_text = (widget_width / 2) - text_half_len
                    elif self.justification == 'LEFT':
                        x_text = 0
                    elif self.justification == 'RIGHT':
                        x_text = widget_width - text_len
                    # PositionType: CENTER, TOP, BOTTOM
                    if self.position_type == 'CENTER':
                        if (widget_height / 2) > 1:
                            y_text = (widget_height / 2) - 1
                        else:
                            y_text = 0
                    elif self.justification == 'TOP':
                        y_text = 0
                    elif self.justification == 'BOTTOM':
                        y_text = 0

                    # Draw the Label
                    drawing_area.addstr(
                        y_text,
                        x_text,
                        resize_text(self.text, widget_width - 1, '~'),
                        curses.color_pair(self.get_style_by_type(self.type))
                    )



    # Internal widget functions
    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    # Justification: LEFT, RIGHT, CENTER
    def set_justify(self, justification):
        self.justification = justification

    def get_justify(self):
        return self.justification

    # Orientation: HORIZONTAL, VERTICAL
    def set_orientation(self, orientation):
        self.orientation = orientation

    def get_orientation(self):
        return self.orientation

    # PositionType: CENTER, TOP, BOTTOM
    def set_position_type(self, position_type):
        self.position_type = position_type

    def get_position_type(self):
        return self.position_type

