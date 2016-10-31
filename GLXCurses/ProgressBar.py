#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from Widget import Widget

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class ProgressBar(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.type = 'ProgressBar'

        self.text = ''
        self.text_to_delete = "[]100.0%"
        self.text_to_delete += str(self.text)
        self.percent = float(0)
        self.char = '|'
        self.bold = 1


    def draw(self):
        parent_height, parent_width = self.parent.get_size()
        parent_y, parent_x = self.parent.get_origin()

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



        widget_y = widget_y
        widget_x = widget_x
        self.size = size
        self.size -= len(self.text_to_delete)
        if self.size + len(str(self.text)) >= len(str(self.text)) - 2:
            if self.bold:
                self.widget.addstr(
                    widget_y,
                    widget_x,
                    str(self.text),
                    curses.color_pair(self.get_style_by_type(self.type)) | curses.A_BOLD
                )
            else:
                self.widget.addstr(
                    widget_y,
                    widget_x,
                    str(self.text),
                    curses.color_pair(self.get_style_by_type(self.type))
                )
            if not len(str(self.text_to_delete)) - len(self.text) >= self.size + 9:
                if self.bold:
                    self.widget.addstr(
                        widget_y,
                        widget_x + len(str(self.text)),
                        "[",
                        curses.color_pair(self.get_style_by_type(self.type)) | curses.A_BOLD
                    )
                    self.widget.addstr(
                        widget_y,
                        widget_x + len(str(self.text)) + 1,
                        str(self.char * int(self.size * self.percent / 100)),
                        self.fg_color | curses.A_BOLD
                    )
                    self.widget.addstr(
                        widget_y,
                        widget_x + len(str(self.text)) + self.size + 1,
                        "]",
                        self.bg_color | curses.A_BOLD
                    )
                else:
                    self.widget.addstr(
                        widget_y,
                        widget_x + len(str(self.text)),
                        "[",
                        self.bg_color
                    )
                    self.widget.addstr(
                        widget_y,
                        widget_x + len(str(self.text)) + 1,
                        str(self.char * int(self.size * self.percent / 100)),
                        self.fg_color
                    )
                    self.widget.addstr(
                        widget_y,
                        widget_x + len(str(self.text)) + self.size + 1,
                        "]",
                        self.bg_color
                    )
            dist_x =widget_x + self.size + 4 + 4
            cpu_num_color = self.bg_color
            if int(round(self.percent)) >= 0:
                dist_x =widget_x + len(str(self.text)) + self.size + 1 + 3
                cpu_num_color = self.bg_color
            if int(round(self.percent)) >= 10:
                dist_x =widget_x + len(str(self.text)) + self.size + 1 + 2
                cpu_num_color = self.bg_color
            if int(round(self.percent)) >= 70:
                dist_x =widget_x + len(str(self.text)) + self.size + 1 + 2
                cpu_num_color = curses.color_pair(7)
            if int(round(self.percent)) >= 95:
                dist_x =widget_x + len(str(self.text)) + self.size + 1 + 2
                cpu_num_color = curses.color_pair(9)
            if int(round(self.percent)) == 100:
                dist_x =widget_x + len(str(self.text)) + self.size + 1 + 1
                cpu_num_color = curses.color_pair(9)
            if self.bold:
                self.parent.addstr(
                    widget_y,
                    dist_x,
                    str(str(self.percent) + "%"),
                    cpu_num_color | curses.A_BOLD
                )
            else:
                self.parent.addstr(
                    widget_y,
                    dist_x,
                    str(str(self.percent) + "%"),
                    cpu_num_color
                )

                # rows, columns = os.popen('stty size', 'r').read().split()
                # self.cli_progress_bar(
                #    "Scaning for " + file_pattern.upper()[2:] + ": ",
                #    int(round(100 * count / len(extension_list))),
                #    100,
                #    int(parent_x)
                # )