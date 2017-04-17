
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import uuid
from GLXCurses import Application

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Deitsuen


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
        self.buffer = ['Bonjour']
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

    def insert(self):
        text = 'Ceci est un texte'
        lenght_of_byte = sys.getsizeof(text)
        if lenght_of_byte == -1:
            text = None
            self.buffer.insert(1, text)
            self.emit_insert_text()
        else:
            self.buffer.insert(1,text)

        return self.buffer

    def emit_insert_text(self):
        instance = {
            'class': self.__class__.__name__,
            'type': 'insert-text',
            'id': self.id
        }
        # EVENT EMIT
        Application().emit('SIGNALS', instance)


if __name__ == '__main__':
    textbuffer = TextBuffer()
    print ("Text:      :" + str(textbuffer.get_char_count()))
    print ("Text:      :" + str(textbuffer.get_line_count()))
    print textbuffer.insert()
