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

        # The Percent value
        self.value = 0
        
        # Internal Widget Setting
        # Justification: LEFT, RIGHT, CENTER
        self.justification = 'CENTER'

        # Orientation: HORIZONTAL, VERTICAL
        self.orientation = 'HORIZONTAL'

        # PositionType: CENTER, TOP, BOTTOM
        self.position_type = 'CENTER'

        # Label
        self.text = ''
        self.show_text = 0
        # Interface
        self.progressbar_border = '[]'
        self.progressbar_vertical_border = '__'

        if self.orientation == 'HORIZONTAL':
            # WIDTH
            self.preferred_width = 0
            self.preferred_width += len(self.progressbar_border)
            self.preferred_width += self.get_spacing() * 2
            # HEIGHT
            self.preferred_height = 1
        elif self.orientation == 'VERTICAL':
            # WIDTH
            self.preferred_width = 1
            # HEIGHT
            self.preferred_height = 0
            self.preferred_height += len(self.progressbar_border)
            self.preferred_height += self.get_spacing() * 2

        self.char = ' '

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
            # Many Thing's
            # Check if the text can be display
            text_have_necessary_width = (self.preferred_width + (self.get_spacing() * 2) >= 1)
            text_have_necessary_height = (self.preferred_height + (self.get_spacing() * 2) >= 1)
            if text_have_necessary_width and text_have_necessary_height:
                y_text = 0
                x_text = 0
                y_progress = 0
                # Orientation: HORIZONTAL, VERTICAL
                if self.orientation == 'HORIZONTAL':
                    self.preferred_width = 0
                    self.preferred_width += len(self.progressbar_border)
                    self.preferred_width += self.get_spacing() * 2
                    # HEIGHT
                    self.preferred_height = 1

                    progress_width = widget_width
                    progress_width -= self.get_spacing() * 2
                    progress_width -= len(self.progressbar_border)
                    progress_text = str(self.char * progress_width)

                    # Justification:
                    x_progress = len(self.progressbar_border) / 2 + self.get_spacing()

                    tmp_string = ''
                    if self.show_text:
                        if self.justification == 'CENTER':
                            tmp_string += progress_text[:(len(progress_text)/2) - len(self.text)/2]
                            tmp_string += self.text
                            tmp_string += progress_text[-(len(progress_text) - len(tmp_string)):]
                            progress_text = tmp_string

                        elif self.justification == 'LEFT':
                            tmp_string += self.text
                            tmp_string += progress_text[-(len(progress_text) - len(self.text)):]
                            progress_text = tmp_string

                        elif self.justification == 'RIGHT':
                            tmp_string += progress_text[:(len(progress_text) - len(self.text))]
                            tmp_string += self.text
                            progress_text = tmp_string

                    # PositionType: CENTER, TOP, BOTTOM
                    if self.position_type == 'CENTER':
                        if (widget_height / 2) > self.preferred_height:
                            y_text = (widget_height / 2) - self.preferred_height
                            y_progress = (widget_height / 2) - self.preferred_height
                        else:
                            y_text = 0 + self.get_spacing()
                            y_progress = 0 + self.get_spacing()

                    elif self.position_type == 'TOP':
                        y_text = 0 + self.get_spacing()
                        y_progress = 0 + self.get_spacing()

                    elif self.position_type == 'BOTTOM':
                        y_text = widget_height - self.preferred_height - self.get_spacing()
                        y_progress = widget_height - self.preferred_height - self.get_spacing()

                    # DRAWING
                    # Justify the text to center of a string it have small len as the progress bar
                    # Frist Pass when we draw everything in Normal color
                    drawing_area.addstr(
                        y_text,
                        x_progress - 1,
                        self.progressbar_border[:len(self.progressbar_border)/2]
                    )

                    # Draw the progressbar background
                    drawing_area.addstr(
                        y_progress,
                        x_progress,
                        progress_text
                    )

                    # Draw the progressbar value and apply percent formula
                    drawing_area.attron(curses.A_REVERSE)
                    drawing_area.addstr(
                        y_progress,
                        x_progress,
                        progress_text[:int((widget_width - self.preferred_width) * self.value / 100)]
                    )
                    drawing_area.attroff(curses.A_REVERSE)

                    # Interface management
                    drawing_area.insstr(
                        widget_y + self.get_spacing(),
                        widget_width - self.get_spacing() - 1,
                        self.progressbar_border[-len(self.progressbar_border)/2:]
                    )

                elif self.orientation == 'VERTICAL':
                    # WIDTH
                    self.preferred_width = 1
                    # HEIGHT
                    self.preferred_height = 0
                    self.preferred_height += len(self.progressbar_border)
                    self.preferred_height += self.get_spacing() * 2

                    progress_height = widget_height
                    progress_height -= self.get_spacing() * 2
                    progress_height -= len(self.progressbar_border)

                    progress_text = str(self.char * progress_height)

                    y_progress = self.get_spacing()
                    x_progress = 0


                    # Check Justification
                    if self.justification == 'CENTER':
                        x_progress = widget_width / 2
                    elif self.justification == 'LEFT':
                        x_progress = self.get_spacing()
                    elif self.justification == 'RIGHT':
                        x_progress = widget_width - self.get_spacing() - 1

                    # PositionType: CENTER, TOP, BOTTOM
                    if self.show_text:
                        tmp_string = ''
                        if self.position_type == 'CENTER':
                            tmp_string += progress_text[:(len(progress_text) / 2) - len(self.text) / 2]
                            tmp_string += self.text
                            tmp_string += progress_text[-(len(progress_text) - len(tmp_string)):]
                            progress_text = tmp_string

                        elif self.position_type == 'TOP':
                            tmp_string += self.text
                            tmp_string += progress_text[-(len(progress_text) - len(self.text)):]
                            progress_text = tmp_string

                        elif self.position_type == 'BOTTOM':
                            tmp_string += progress_text[:(len(progress_text) - len(self.text))]
                            tmp_string += self.text
                            progress_text = tmp_string

                    # Draw Vertical ProgressBar
                    # Draw first interface Character
                    drawing_area.insch(
                        y_progress,
                        x_progress,
                        curses.ACS_HLINE
                    )
                    # Draw the Vertical ProgressBar with Justification and PositionType
                    count = 1
                    for CHAR in progress_text:
                        drawing_area.addstr(
                            y_progress + count,
                            x_progress,
                            CHAR
                        )
                        count += 1
                    drawing_area.attron(curses.A_REVERSE)
                    count = 1
                    for CHAR in progress_text[:int((widget_height - self.preferred_height) * self.value / 100)]:
                        drawing_area.addstr(
                            y_progress + count,
                            x_progress,
                            CHAR
                        )
                        count += 1
                    drawing_area.attroff(curses.A_REVERSE)

                    # Draw last interface Character
                    drawing_area.insch(
                        widget_height - self.get_spacing() - 1,
                        x_progress,
                        curses.ACS_HLINE
                    )

    # Internal widget functions
    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def set_value(self, percent=0):
        if self.value >= 0:
            self.value = percent
        else:
            self.value = 0
        self.text = '{0: >3}{1:}'.format(self.value, '%')

    def get_value(self):
        if self.value >= 0:
            return self.value
        else:
            self.value = 0
            return self.value

    def set_show_text(self, show_text_int):
        self.show_text = show_text_int

    def get_show_text(self):
        return self.show_text

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

