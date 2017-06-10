#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import uuid
from GLXCurses import Application
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Adam Bouadil alias "Deitsuen" <adamb27750@orange.fr> all rights reserved


class TextBuffer(object):
    def __init__(self, table=None):

        """
        Create the new textBuffer object
        ***Properties***
        line_count - the number of


        text - The contents of the buffer. Default value: "".
        """

        self.table = table
        self.tag_table = ""
        self.text = 'lalalala'
        self.buffer = ['lala', 'yoyo', 'toto']
        self.slice = ""

        # internal
        # Unique ID it permit to individually identify a widget by example for get_focus get_default
        self.id = uuid.uuid1().int

    def get_line_count(self):
        """
        Obtains the number of lines in the buffer.
        This value is cached, so the function is very fast.

        :param line
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
        return len(self.buffer)

    def text_buffer_get_tag_table(self):
        """
        Get the :class:`TextTagTable <GLXCurses.TextTagTable.TextTagTable>` associated with this buffer.
        """
        pass

    def insert(self, text, iter):
        lenght_of_byte = sys.getsizeof(text)
        if lenght_of_byte == -1:
            text = None
            self.buffer.insert(iter, text)
            self.emit_insert_text()

        else:
            self.buffer.insert(iter, text)
            self.emit_insert_text()

        return str(self.buffer)

    def insert_at_cursor(self, position):

        print self.insert('ceci est une suite de texte', position)

    def emit_insert_text(self):
        # Create a Dict with everything
        instance = {
            'class': self.__class__.__name__,
            'type': 'insert-text',
            'id': self.id
        }
        # EVENT EMIT
        Application().emit('SIGNALS', instance)
        return instance

    def get_buffer(self):
        return str(self.buffer)

    def insert_interactive(self, text, position):

        tag_no_edit = 0
        self.insert(text, position)
        if position == tag_no_edit:
            self.buffer.remove(text)
            print 'this position is not editable {}'.format(position)
        else:
            "this insert on position {} is a success".format(position)

        for c, value in enumerate(self.buffer):
            if c == tag_no_edit:
                print c, "no editable"
            else:
                print c, "editable"


if __name__ == '__main__':
    textbuffer = TextBuffer()
    iter = 1
    print ("Text:      :" + str(textbuffer.get_char_count()))
    print ("Text:      :" + str(textbuffer.get_line_count()))
    print textbuffer.insert('Ceci est un texte', 0)
    print textbuffer.insert_at_cursor(iter)
    print textbuffer.insert_interactive("CROIT Y ", 0)
