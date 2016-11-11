#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from GLXCurses.Widget import Widget

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
        self.set_name('ProgressBar')

        # Make a Style heritage attribute
        if self.get_style().attribute:
            self.attribute = self.get_style().attribute

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
        self.show_text = None
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

    def draw(self):
        parent_height, parent_width = self.get_parent().get_size()
        parent_y, parent_x = self.get_parent().get_origin()

        min_size_width = (self.get_spacing() * 2) + 1
        min_size_height = (self.get_spacing() * 2) + 1
        height_ok = self.get_parent().get_height() >= min_size_height
        width_ok = self.get_parent().get_width() >= min_size_width
        if not height_ok or not width_ok:
            return

        drawing_area = self.get_parent().get_widget().subwin(
            parent_height - (self.get_spacing() * 2),
            parent_width - (self.get_spacing() * 2),
            parent_y + self.get_spacing(),
            parent_x + self.get_spacing()
        )

        self.draw_widget_in_area(drawing_area)

    def get_attr(self, elem, state):
        return self.attribute[elem][state]

    def draw_widget_in_area(self, drawing_area):
        self.set_widget(drawing_area)

        height_ok = self.get_height() > self.get_preferred_height()
        width_ok = self.get_width() > self.get_preferred_width()

        if not height_ok or not width_ok:
            return

        # Many Thing's
        # Check if the text can be display
        text_have_necessary_width = (self.get_preferred_width() + (self.get_spacing() * 2) >= 1)
        text_have_necessary_height = (self.get_preferred_height() + (self.get_spacing() * 2) >= 1)
        if not text_have_necessary_height or not text_have_necessary_width:
            return

        # Orientation: HORIZONTAL, VERTICAL
        if self.get_orientation() == 'HORIZONTAL':
            self.draw_horizontal()

        elif self.get_orientation() == 'VERTICAL':
            self.draw_vertical()

    def draw_vertical(self):
        y_progress = self.get_spacing()

        # Check Justification
        x_progress = self.check_vertical_justification()
        if self.get_show_text():
            # PositionType: CENTER, TOP, BOTTOM
            progress_text = self.check_vertical_position_type()

        # Draw Vertical ProgressBar
        # Draw first interface Character
        self.get_widget().addch(
            y_progress,
            x_progress,
            curses.ACS_HLINE,
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_attr('base', 'STATE_NORMAL'),
                bg=self.get_attr('bg', 'STATE_NORMAL'))
            )
        )
        # Draw the Vertical ProgressBar with Justification and PositionType
        if self.get_inverted():
            # Draw Background
            progress_text = progress_text[::-1]
            increment = 0
            for CHAR in progress_text:
                self.get_widget().addch(
                    self.get_height() - self.get_spacing() - 2 - increment,
                    x_progress,
                    CHAR,
                    curses.color_pair(self.get_style().get_curses_pairs(
                        fg=self.get_attr('base', 'STATE_NORMAL'),
                        bg=self.get_attr('bg', 'STATE_NORMAL'))
                    )
                )
                increment += 1

            count = 0
            for CHAR in progress_text[:int((self.get_height() - self.get_preferred_height()) * self.value / 100)]:
                self.get_widget().addch(
                    self.get_height() - self.get_spacing() - 2 - count,
                    x_progress,
                    CHAR,
                    curses.color_pair(self.get_style().get_curses_pairs(
                        fg=self.get_attr('bg', 'STATE_NORMAL'),
                        bg=self.get_attr('base', 'STATE_NORMAL'))
                    )
                )
                count += 1

            # Draw last interface Character
            self.get_widget().insch(
                self.get_height() - self.get_spacing() - 1,
                x_progress,
                curses.ACS_HLINE,
                curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_attr('base', 'STATE_NORMAL'),
                    bg=self.get_attr('bg', 'STATE_NORMAL'))
                )
            )
        else:
            # Draw the Vertical ProgressBar with Justification and PositionType
            count = 1
            for CHAR in progress_text:
                self.get_widget().addstr(
                    y_progress + count,
                    x_progress,
                    CHAR,
                    curses.color_pair(self.get_style().get_curses_pairs(
                        fg=self.get_attr('base', 'STATE_NORMAL'),
                        bg=self.get_attr('bg', 'STATE_NORMAL'))
                    )
                )
                count += 1

            # Redraw with color inverted but apply percent calculation
            count = 1
            for CHAR in progress_text[:int((self.get_height() - self.get_preferred_height()) * self.value / 100)]:
                self.get_widget().addstr(
                    y_progress + count,
                    x_progress,
                    CHAR,
                    curses.color_pair(self.get_style().get_curses_pairs(
                        fg=self.get_attr('bg', 'STATE_NORMAL'),
                        bg=self.get_attr('base', 'STATE_NORMAL'))
                    )
                )
                count += 1

            # Draw last interface Character
            self.get_widget().insch(
                self.get_height() - self.get_spacing() - 1,
                x_progress,
                curses.ACS_HLINE,
                curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_attr('base', 'STATE_NORMAL'),
                    bg=self.get_attr('bg', 'STATE_NORMAL'))
                )
            )

    def check_vertical_justification(self):
        x_progress = 0
        if self.get_justify() == 'CENTER':
            x_progress = self.get_width() / 2
        elif self.get_justify() == 'LEFT':
            x_progress = self.get_spacing()
        elif self.get_justify() == 'RIGHT':
            x_progress = self.get_width() - self.get_spacing() - (len(self.progressbar_border) / 2)

        return x_progress

    def check_vertical_position_type(self):
        progress_height = self.get_height()
        progress_height -= self.get_spacing() * 2
        progress_height -= len(self.progressbar_border)
        progress_text = str(self.char * progress_height)
        tmp_string = ''
        if self.get_position_type().upper() == 'CENTER':
            if progress_height - (len(self.progressbar_border) / 2) > len(self.text):
                tmp_string += progress_text[:(len(progress_text) / 2) - len(self.text) / 2]
                tmp_string += self.text
                tmp_string += progress_text[-(len(progress_text) - len(tmp_string)):]
            elif progress_height - (len(self.progressbar_border) / 2) >= self.get_preferred_height():
                tmp_string += self.text
            else:
                tmp_string += progress_text[:progress_height]
            progress_text = tmp_string

        elif self.get_position_type().upper() == 'TOP':
            if progress_height - (len(self.progressbar_border) / 2) >= len(self.text):
                tmp_string += self.text
                tmp_string += progress_text[-(len(progress_text) - len(self.text)):]
            elif progress_height - (len(self.progressbar_border) / 2) >= self.get_preferred_height():
                tmp_string += self.text
            else:
                tmp_string += progress_text[:progress_height]
            progress_text = tmp_string

        elif self.get_position_type().upper() == 'BOTTOM':
            if progress_height - (len(self.progressbar_border) / 2) >= len(self.text):
                tmp_string += progress_text[:(len(progress_text) - len(self.text))]
                tmp_string += self.text
            elif progress_height - (len(self.progressbar_border) / 2) >= self.get_preferred_height():
                tmp_string += self.text
            else:
                tmp_string += progress_text[:progress_height]
            progress_text = tmp_string

        return progress_text

    def draw_horizontal(self):

        x_progress = len(self.progressbar_border) / 2 + self.get_spacing()

        progress_text = self.check_horizontal_justification()

        # PositionType: CENTER, TOP, BOTTOM
        y_progress, y_text = self.check_horizontal_position_type()

        # DRAWING
        # Justify the text to center of a string it have small len as the progress bar
        # First Pass when we draw everything in Normal color
        self.get_widget().addstr(
            y_text,
            x_progress - 1,
            self.progressbar_border[:len(self.progressbar_border) / 2],
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_attr('base', 'STATE_NORMAL'),
                bg=self.get_attr('bg', 'STATE_NORMAL'))
            )
        )
        # Draw the progressbar1 background
        # Draw Left to Right Horizontal Progress Bar
        if self.get_inverted():
            progress_text = progress_text[::-1]
            increment = 0
            for CHAR in progress_text:
                self.get_widget().addstr(
                    y_progress,
                    self.get_width() - self.get_spacing() - 2 - increment,
                    CHAR,
                    curses.color_pair(self.get_style().get_curses_pairs(
                        fg=self.get_attr('base', 'STATE_NORMAL'),
                        bg=self.get_attr('bg', 'STATE_NORMAL'))
                    )
                )
                increment += 1
            increment = 0
            for CHAR in progress_text[:int((self.get_width() - self.get_preferred_width()) * self.get_value() / 100)]:
                self.get_widget().addstr(
                    y_progress,
                    self.get_width() - self.get_spacing() - 2 - increment,
                    CHAR,
                    curses.color_pair(self.get_style().get_curses_pairs(
                        fg=self.get_attr('bg', 'STATE_NORMAL'),
                        bg=self.get_attr('base', 'STATE_NORMAL'))
                    )
                )
                increment += 1
        else:
            increment = 0
            for CHAR in progress_text:
                self.get_widget().addstr(
                    y_progress,
                    x_progress + increment,
                    CHAR,
                    curses.color_pair(self.get_style().get_curses_pairs(
                        fg=self.get_attr('base', 'STATE_NORMAL'),
                        bg=self.get_attr('bg', 'STATE_NORMAL'))
                    )
                )
                increment += 1
            increment = 0
            for CHAR in progress_text[:int((self.get_width() - self.get_preferred_width()) * self.get_value() / 100)]:
                self.get_widget().addstr(
                    y_progress,
                    x_progress + increment,
                    CHAR,
                    curses.color_pair(self.get_style().get_curses_pairs(
                        fg=self.get_attr('bg', 'STATE_NORMAL'),
                        bg=self.get_attr('base', 'STATE_NORMAL'))
                    )
                )
                increment += 1
        # Interface management
        self.get_widget().insstr(
            y_progress,
            self.get_width() - self.get_spacing() - 1,
            self.progressbar_border[-len(self.progressbar_border) / 2:],
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_attr('base', 'STATE_NORMAL'),
                bg=self.get_attr('bg', 'STATE_NORMAL'))
            )
        )

    def check_horizontal_justification(self):
        progress_width = self.get_width()
        progress_width -= self.get_spacing() * 2
        progress_width -= len(self.progressbar_border)
        progress_text = str(self.char * progress_width)
        # Justification:
        tmp_string = ''
        if self.get_show_text():
            if self.get_justify() == 'CENTER':
                tmp_string += progress_text[:(len(progress_text) / 2) - len(self.get_text()) / 2]
                tmp_string += self.get_text()
                tmp_string += progress_text[-(len(progress_text) - len(tmp_string)):]
                progress_text = tmp_string

            elif self.get_justify() == 'LEFT':
                tmp_string += self.get_text()
                tmp_string += progress_text[-(len(progress_text) - len(self.get_text())):]
                progress_text = tmp_string

            elif self.get_justify() == 'RIGHT':
                tmp_string += progress_text[:(len(progress_text) - len(self.get_text()))]
                tmp_string += self.get_text()
                progress_text = tmp_string

        return progress_text

    def check_horizontal_position_type(self):
        y_text = 0
        y_progress = 0
        position_type = self.get_position_type()
        if position_type == 'CENTER':
            if (self.get_height() / 2) > self.get_preferred_height():
                y_text = (self.get_height() / 2) - self.get_preferred_height()
                y_progress = (self.get_height() / 2) - self.get_preferred_height()
            else:
                y_text = 0 + self.get_spacing()
                y_progress = 0 + self.get_spacing()

        elif position_type == 'TOP':
            y_text = 0 + self.get_spacing()
            y_progress = 0 + self.get_spacing()

        elif position_type == 'BOTTOM':
            y_text = self.get_height() - self.get_preferred_height() - self.get_spacing()
            y_progress = self.get_height() - self.get_preferred_height() - self.get_spacing()

        return y_progress, y_text



    # Internal widget functions
    def set_text(self, text):
        self.text = text
        self._update_preferred_size()

    def get_text(self):
        return self.text

    def set_value(self, percent=0):
        if 0 <= percent <= 100:
            self.value = percent
        else:
            self.value = 0
        self._update_preferred_size()

    def get_value(self):
        return self.value

    def set_show_text(self, show_text_int):
        self.show_text = show_text_int

    def get_show_text(self):
        return self.show_text

    # Justification: LEFT, RIGHT, CENTER
    def set_justify(self, justification):
        self.justification = str(justification).upper()
        self._update_preferred_size()

    def get_justify(self):
        return self.justification

    # Orientation: HORIZONTAL, VERTICAL
    def set_orientation(self, orientation):
        self.orientation = str(orientation).upper()
        self._update_preferred_size()

    def get_orientation(self):
        return self.orientation

    # PositionType: CENTER, TOP, BOTTOM
    def set_position_type(self, position_type):
        self.position_type = str(position_type).upper()
        self._update_preferred_size()

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

    # Internal
    def _update_preferred_size(self):
        if self.get_orientation() == 'HORIZONTAL':
            # WIDTH
            self.preferred_width = 0
            self.preferred_width += len(self.progressbar_border)
            self.preferred_width += len(self.get_text())
            self.preferred_width += self.get_spacing() * 2
            # HEIGHT
            self.preferred_height = 1
        elif self.get_orientation() == 'VERTICAL':
            # WIDTH
            self.preferred_width = 1
            # HEIGHT
            self.preferred_height = 0
            self.preferred_height += len(self.progressbar_border)
            self.preferred_height += len(self.get_text())
            self.preferred_height += self.get_spacing() * 2
