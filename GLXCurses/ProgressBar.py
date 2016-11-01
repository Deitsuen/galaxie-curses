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
        text_to_return = text[:(max_width / 2) - 1] + separator + text[-max_width / 2:]
        if len(text_to_return) == 1:
            text_to_return = text[:1]
        elif len(text_to_return) == 2:
            text_to_return = str(text[:1] + text[-1:])
        elif len(text_to_return) == 3:
            text_to_return = str(text[:1] + separator + text[-1:])
        return text_to_return
    else:
        return text


class ProgressBar(Widget):
    def __init__(self):
        Widget.__init__(self)

        # Internal Widget Setting
        self.text = 'coucou'
        self.percent = 100
        self.text_value = '{0: >3}{1:}'.format(self.percent, '%')
        self.preferred_height = 1
        self.preferred_width = len(self.text) + len("[]100.0%")

        self.char = ' '
        # Justification: LEFT, RIGHT, CENTER
        self.justification = 'CENTER'

        # Orientation: HORIZONTAL, VERTICAL
        self.orientation = 'HORIZONTAL'

        # PositionType: CENTER, TOP, BOTTOM
        self.position_type = 'CENTER'

        # Default color
        self.fg_color = curses.COLOR_YELLOW
        self.bg_color = curses.COLOR_BLACK

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

            # Impose the Background color to the Widget
            if curses.has_colors():
                drawing_area.bkgdset(ord(' '), curses.color_pair(self.style.colors.index('ProgressBar')))
                drawing_area.bkgd(ord(' '), curses.color_pair(self.style.colors.index('ProgressBar')))
                for I in range(widget_y, widget_height):
                    drawing_area.insstr(
                        I,
                        0,
                        str(' ' * int(widget_width - 1)),
                        curses.color_pair(self.style.colors.index('ProgressBar'))
                    )
                    drawing_area.insstr(
                        I,
                        int(widget_width - 1),
                        str(' '),
                        curses.color_pair(self.style.colors.index('ProgressBar'))
                    )

            # Many Thing's
            if not self.text == '':
                # Check if the text can be display
                text_have_necessary_width = (self.preferred_width + self.get_spacing() >= 1)
                text_have_necessary_height = (self.preferred_height + self.get_spacing() >= 1)
                if text_have_necessary_width and text_have_necessary_height:
                    y_text = 0
                    x_text = 0
                    y_progress = 0
                    x_progress = 0
                    y_value = 0
                    x_value = 0
                    # Orientation: HORIZONTAL, VERTICAL
                    if self.orientation == 'HORIZONTAL':
                        # Check Justification
                        if self.justification == 'CENTER':
                            x_text = 0 + self.get_spacing()
                            x_progress = len(self.text) + 1
                            x_value = widget_width - len(self.text_value)
                        elif self.justification == 'LEFT':
                            x_text = 0 + self.get_spacing()
                        elif self.justification == 'RIGHT':
                            x_text = widget_width - self.preferred_width

                        # PositionType: CENTER, TOP, BOTTOM
                        if self.position_type == 'CENTER':
                            if (widget_height / 2) > self.preferred_height:
                                y_text = (widget_height / 2) - self.preferred_height
                                y_progress = (widget_height / 2) - self.preferred_height
                                y_value = (widget_height / 2) - self.preferred_height
                            else:
                                y_text = 0
                                y_progress = 0
                                y_value = 0
                        elif self.position_type == 'TOP':
                            y_text = 0
                            y_progress = 0
                            y_value = 0
                        elif self.position_type == 'BOTTOM':
                            y_text = widget_height - self.preferred_height
                            y_progress = widget_height - self.preferred_height
                            y_value = widget_height - self.preferred_height

                        # DRAWING
                        # Draw the Horizontal Label with Justification and PositionType
                        message_to_display = resize_text(self.text, widget_width - 1, '~')
                        drawing_area.insstr(
                            y_text,
                            x_text,
                            message_to_display,
                            curses.color_pair(self.style.colors.index('ProgressBar'))
                        )
                        drawing_area.insstr(
                            y_text,
                            x_progress - 1,
                            str('['),
                            curses.color_pair(self.style.colors.index('ProgressBar'))
                        )
                        # Draw the progressbar background
                        drawing_area.insstr(
                            y_progress,
                            x_progress,
                            str(self.char * int(widget_width - self.preferred_width)),
                            curses.color_pair(self.style.colors.index('ProgressBarBG')) | curses.A_BOLD
                        )
                        # Draw the progressbar value
                        drawing_area.insstr(
                            y_progress,
                            x_progress,
                            str(self.char * int(1 + (widget_width - self.preferred_width) * self.percent / 100)),
                            curses.color_pair(self.style.colors.index('ProgressBarFG')) | curses.A_BOLD
                        )
                        drawing_area.insstr(
                            y_value,
                            x_value - 1,
                            str(']'),
                            curses.color_pair(self.style.colors.index('ProgressBar'))
                        )
                        drawing_area.insstr(
                            y_value,
                            x_value,
                            self.text_value,
                            curses.color_pair(self.style.colors.index('ProgressBar'))
                        )
                    elif self.orientation == 'VERTICAL':

                        # Check Justification
                        if self.justification == 'CENTER':
                            x_text = (widget_width - self.get_spacing() / 2) - (self.preferred_width - self.get_spacing() / 2)
                        elif self.justification == 'LEFT':
                            x_text = 0 + self.get_spacing()
                        elif self.justification == 'RIGHT':
                            x_text = widget_width - self.preferred_width - self.get_spacing()

                        # PositionType: CENTER, TOP, BOTTOM
                        if self.position_type == 'CENTER':
                            #y_text = (widget_height / 2) - (self.preferred_height / 2)
                            if (widget_height / 2) > (self.preferred_height / 2):
                                y_text = (widget_height / 2) - (self.preferred_height / 2)
                            else:
                                y_text = 0
                        elif self.position_type == 'TOP':
                            y_text = 0
                        elif self.position_type == 'BOTTOM':
                            y_text = widget_height - self.preferred_height
                        # Draw the Vertical Label with Justification and PositionType

                        message_to_display = resize_text(self.text, widget_height - 1, '~')
                        if len(message_to_display) > 2:
                            count = 0
                            for CHAR in message_to_display:
                                drawing_area.insstr(
                                    y_text + count,
                                    x_text,
                                    CHAR,
                                    curses.color_pair(self.style.colors.index('Label'))
                                )
                                count += 1

    # Internal widget functions
    def set_text(self, text):
        self.text = text
        if self.orientation == 'HORIZONTAL':
            self.preferred_width = len(self.text)
            self.preferred_height = 1
        elif self.orientation == 'VERTICAL':
            self.preferred_width = 1
            self.preferred_height = len(self.text)

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
        if self.orientation == 'HORIZONTAL':
            self.preferred_width = len(self.text)
            self.preferred_height = 1
        elif self.orientation == 'VERTICAL':
            self.preferred_width = 1
            self.preferred_height = len(self.text)

    def get_orientation(self):
        return self.orientation

    # PositionType: CENTER, TOP, BOTTOM
    def set_position_type(self, position_type):
        self.position_type = position_type

    def get_position_type(self):
        return self.position_type

