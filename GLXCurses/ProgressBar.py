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
        self.name = 'ProgressBar'

        if self.style.attribute:
            self.color_text = self.style.attribute['text']['STATE_NORMAL']
            self.color_bg = self.style.attribute['bg']['STATE_NORMAL']
            self.color_light = self.style.attribute['base']['STATE_NORMAL']

            self.color_normal = self.style.get_curses_pairs(fg=self.color_text, bg=self.color_bg)
            self.color_progressbar = self.style.get_curses_pairs(fg=self.color_light, bg=self.color_bg)
            self.color_progressbar_inverted = self.style.get_curses_pairs(fg=self.color_bg, bg=self.color_light)
            self.color_red = self.style.get_curses_pairs(fg='RED', bg='RED')
            self.color_yellow = self.style.get_curses_pairs(fg='YELLOW', bg='YELLOW')
        else:
            self.color_normal = 0
            self.color_progressbar = 0
            self.color_progressbar_inverted = 0

        # The Percent value
        self.value = 0
        
        # Internal Widget Setting
        # Justification: LEFT, RIGHT, CENTER
        self.justification = 'CENTER'

        # Orientation: HORIZONTAL, VERTICAL
        self.orientation = 'HORIZONTAL'

        # PositionType: CENTER, TOP, BOTTOM
        self.position_type = 'CENTER'

        # Progress bars normally grow from top to bottom or left to right.
        # Inverted progress bars grow in the opposite direction
        self.inverted = 0

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
        parent_height, parent_width = self.get_parent_size()
        parent_y, parent_x = self.get_parent_origin()
        spacing = self.get_spacing()

        drawing_area = self.parent.widget.subwin(
                parent_height - (spacing * 2),
                parent_width - (spacing * 2),
                parent_y + spacing,
                parent_x + spacing
        )

        self.draw_in_area(drawing_area)

    def draw_in_area(self, drawing_area):
        spacing = self.get_spacing()

        self.widget = drawing_area
        widget_height, widget_width = self.widget.getmaxyx()
        widget_y, widget_x = self.widget.getbegyx()

        min_size_width = (spacing * 2) + spacing
        min_size_height = (spacing * 2)
        if (widget_height >= min_size_height) and (widget_width >= min_size_width):
            # Many Thing's
            # Check if the text can be display
            text_have_necessary_width = (self.preferred_width + (spacing * 2) >= 1)
            text_have_necessary_height = (self.preferred_height + (spacing * 2) >= 1)
            if text_have_necessary_width and text_have_necessary_height:
                y_text = 0
                x_text = 0
                y_progress = 0
                # Orientation: HORIZONTAL, VERTICAL
                if self.get_orientation().upper() == 'HORIZONTAL':
                    self.preferred_width = 0
                    self.preferred_width += len(self.progressbar_border)
                    self.preferred_width += spacing * 2
                    # HEIGHT
                    self.preferred_height = 1

                    progress_width = widget_width
                    progress_width -= spacing * 2
                    progress_width -= len(self.progressbar_border)
                    progress_text = str(self.char * progress_width)

                    # Justification:
                    justify = self.get_justify().upper()
                    text = self.get_text()

                    x_progress = len(self.progressbar_border) / 2 + spacing
                    tmp_string = ''

                    if self.get_show_text():
                        if justify == 'CENTER':
                            tmp_string += progress_text[:(len(progress_text)/2) - len(text)/2]
                            tmp_string += text
                            tmp_string += progress_text[-(len(progress_text) - len(tmp_string)):]
                            progress_text = tmp_string

                        elif justify == 'LEFT':
                            tmp_string += text
                            tmp_string += progress_text[-(len(progress_text) - len(text)):]
                            progress_text = tmp_string

                        elif justify == 'RIGHT':
                            tmp_string += progress_text[:(len(progress_text) - len(text))]
                            tmp_string += text
                            progress_text = tmp_string

                    # PositionType: CENTER, TOP, BOTTOM
                    position_type = self.get_position_type().upper()

                    if position_type == 'CENTER':
                        if (widget_height / 2) > self.preferred_height:
                            y_text = (widget_height / 2) - self.preferred_height
                            y_progress = (widget_height / 2) - self.preferred_height
                        else:
                            y_text = 0 + spacing
                            y_progress = 0 + spacing

                    elif position_type == 'TOP':
                        y_text = 0 + spacing
                        y_progress = 0 + spacing

                    elif position_type == 'BOTTOM':
                        y_text = widget_height - self.preferred_height - spacing
                        y_progress = widget_height - self.preferred_height - spacing

                    # DRAWING
                    # Justify the text to center of a string it have small len as the progress bar
                    # First Pass when we draw everything in Normal color
                    self.widget.addstr(
                        y_text,
                        x_progress - 1,
                        self.progressbar_border[:len(self.progressbar_border)/2],
                        curses.color_pair(self.color_normal)
                    )

                    # Draw the progressbar1 background

                    # Draw Let to Right Horizontal Progress Bar
                    if self.get_inverted():
                        progress_text = progress_text[::-1]
                        count = 0
                        for CHAR in progress_text:
                            self.widget.addstr(
                                y_progress,
                                widget_width - spacing - 2 - count,
                                CHAR,
                                curses.color_pair(self.color_progressbar)
                            )
                            count += 1
                        #self.widget.attron(curses.A_REVERSE)
                        count = 0
                        for CHAR in progress_text[:int((widget_width - self.preferred_width) * self.value / 100)]:
                            self.widget.addstr(
                                y_progress,
                                widget_width - spacing - 2 - count,
                                CHAR,
                                curses.color_pair(self.color_progressbar_inverted)
                            )
                            count += 1
                        #self.widget.attroff(curses.A_REVERSE)
                    else:
                        count = 0
                        for CHAR in progress_text:
                            self.widget.addstr(
                                y_progress,
                                x_progress + count,
                                CHAR,
                                curses.color_pair(self.color_progressbar)
                            )
                            count += 1
                        #self.widget.attron(curses.A_REVERSE)
                        count = 0
                        for CHAR in progress_text[:int((widget_width - self.preferred_width) * self.value / 100)]:
                            self.widget.addstr(
                                y_progress,
                                x_progress + count,
                                CHAR,
                                curses.color_pair(self.color_progressbar_inverted)
                            )
                            count += 1
                        #self.widget.attroff(curses.A_REVERSE)

                    # Interface management
                    self.widget.insstr(
                        y_progress,
                        widget_width - spacing - 1,
                        self.progressbar_border[-len(self.progressbar_border)/2:],
                        curses.color_pair(self.color_normal)
                    )

                elif self.get_orientation().upper() == 'VERTICAL':
                    # WIDTH
                    self.preferred_width = 1
                    # HEIGHT
                    self.preferred_height = 0
                    self.preferred_height += len(self.progressbar_border)
                    self.preferred_height += spacing * 2

                    progress_height = widget_height
                    progress_height -= spacing * 2
                    progress_height -= len(self.progressbar_border)

                    progress_text = str(self.char * progress_height)

                    y_progress = spacing
                    x_progress = 0

                    # Check Justification
                    if self.get_justify().upper() == 'CENTER':
                        x_progress = widget_width / 2
                    elif self.get_justify().upper() == 'LEFT':
                        x_progress = spacing
                    elif self.get_justify().upper() == 'RIGHT':
                        x_progress = widget_width - spacing - (len(self.progressbar_border)/2)

                    # PositionType: CENTER, TOP, BOTTOM
                    if self.get_show_text():
                        tmp_string = ''
                        if self.get_position_type().upper() == 'CENTER':
                            if progress_height - (len(self.progressbar_border)/2) > len(self.text):
                                tmp_string += progress_text[:(len(progress_text) / 2) - len(self.text) / 2]
                                tmp_string += self.text
                                tmp_string += progress_text[-(len(progress_text) - len(tmp_string)):]
                            elif progress_height - (len(self.progressbar_border)/2) >= self.preferred_height:
                                tmp_string += self.text
                            else:
                                tmp_string += progress_text[:progress_height]
                            progress_text = tmp_string

                        elif self.get_position_type().upper() == 'TOP':
                            if progress_height - (len(self.progressbar_border) / 2) >= len(self.text):
                                tmp_string += self.text
                                tmp_string += progress_text[-(len(progress_text) - len(self.text)):]
                            elif progress_height - (len(self.progressbar_border)/2) >= self.preferred_height:
                                tmp_string += self.text
                            else:
                                tmp_string += progress_text[:progress_height]
                            progress_text = tmp_string

                        elif self.get_position_type().upper() == 'BOTTOM':
                            if progress_height - (len(self.progressbar_border) / 2) >= len(self.text):
                                tmp_string += progress_text[:(len(progress_text) - len(self.text))]
                                tmp_string += self.text
                            elif progress_height - (len(self.progressbar_border)/2) >= self.preferred_height:
                                tmp_string += self.text
                            else:
                                tmp_string += progress_text[:progress_height]
                            progress_text = tmp_string

                    # Draw Vertical ProgressBar
                    # Draw first interface Character
                    self.widget.addch(
                        y_progress,
                        x_progress,
                        curses.ACS_HLINE,
                        curses.color_pair(self.color_normal)
                    )
                    # Draw the Vertical ProgressBar with Justification and PositionType
                    if self.get_inverted():
                        # Draw Background
                        progress_text = progress_text[::-1]
                        count = 0
                        for CHAR in progress_text:
                            self.widget.addch(
                                widget_height - spacing - 2 - count,
                                x_progress,
                                CHAR,
                                curses.color_pair(self.color_progressbar)
                            )
                            count += 1

                        #self.widget.attron(curses.A_REVERSE)
                        count = 0
                        for CHAR in progress_text[:int((widget_height - self.preferred_height) * self.value / 100)]:
                            self.widget.addch(
                                widget_height - spacing - 2 - count,
                                x_progress,
                                CHAR,
                                curses.color_pair(self.color_progressbar_inverted)
                            )
                            count += 1
                        #self.widget.attroff(curses.A_REVERSE)

                        # Draw last interface Character
                        self.widget.insch(
                            widget_height - spacing - 1,
                            x_progress,
                            curses.ACS_HLINE,
                            curses.color_pair(self.color_normal)
                        )
                    else:
                        # Draw the Vertical ProgressBar with Justification and PositionType
                        count = 1
                        for CHAR in progress_text:
                            self.widget.addstr(
                                y_progress + count,
                                x_progress,
                                CHAR,
                                curses.color_pair(self.color_progressbar)
                            )
                            count += 1

                        # self.widget.attron(curses.A_REVERSE)
                        count = 1
                        for CHAR in progress_text[:int((widget_height - self.preferred_height) * self.value / 100)]:
                            self.widget.addstr(
                                y_progress + count,
                                x_progress,
                                CHAR,
                                curses.color_pair(self.color_progressbar_inverted)
                            )
                            count += 1
                        # self.widget.attroff(curses.A_REVERSE)

                        # Draw last interface Character
                        self.widget.addch(
                            widget_height - spacing - 1,
                            x_progress,
                            curses.ACS_HLINE,
                            curses.color_pair(self.color_normal)
                        )

    # Internal widget functions
    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def set_value(self, percent=0):
        if percent >= 0:
            self.value = percent
        else:
            self.value = 0
        #self.draw()

    def get_value(self):
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

    # Progress bars normally grow from top to bottom or left to right.
    # Inverted progress bars grow in the opposite direction
    def set_inverted(self, boolean=0):
        if boolean >= 0:
            self.inverted = boolean
        else:
            self.inverted = 0

    def get_inverted(self):
        if self.inverted < 0:
            self.inverted = 0
        return self.inverted
