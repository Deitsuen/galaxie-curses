#!/usr/bin/env python
# -*- coding: utf-8 -*-
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Deitsuen
import sys
import uuid
from GLXCurses import Application

class TextBuffer(object):





    def __init__(self, table=None):
        """
        Create the new textBuffer object

        :param line_count - count the number of line and return the result
        :param text - The contents of the buffer. Default value: "".
        """

        self.table = table
        self.tag_table = ""
        self.text = """"""
        self.slice = ""

        # internal
        self.id = uuid.uuid1().int

    def get_line_count(self):
        """
        Obtains the number of lines in the buffer.
        This value is cached, so the function is very fast.
        """
        return len(self.text.split('\n'))

    def get_char_count(self):
        """
        Gets the number of characters in the buffer;
        :Note:
        That characters and bytes are not the same,
        you can’t e.g. expect the contents of the buffer in string form to be this many bytes long.
        The character count is cached, so this function is very fast.
        """
        return len(self.text)

    def get_tag_table(self):
        """
        Get the :class:`TextTagTable <GLXCurses.TextTagTable.TextTagTable>` associated with this buffer.
        """
        if None:
            return None

    def insert(self, text):
        lenght_byte = sys.getsizeof(text)  # <- Len byte
        for line in iter(text):

            if lenght_byte <= -1:
                line = None
                self.text = line
                return self.emit_insert()

    def emit_insert(self):

        instance = {
            'class': self.__class__.__name__,
            'type': 'value-changed',
            'id': self.id
        }

        Application().emit('SIGNALS', instance)


if __name__ == '__main__':
    textbuffer = TextBuffer()
    textbuffer.insert("ttttttt")
    textbuffer.emit_insert()

    # W.I.P (Work In Progress)
