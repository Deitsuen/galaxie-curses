#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import uuid


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
        self.text = 'abc def ghi jkl'
        self.buffer = ['NoEdit', 'Edit1', 'Edit2', 'Edit3', 'Edit4', "Edit5"]
        self.slice = ""
        self.tag_no_edit = [0, 1, 2, 3]
        # internal
        # Unique ID it permit to individually identify a widget by example for get_focus get_default
        self.id = uuid.uuid1().int
        self.noposition = 0

    def get_line_count(self, buffer):
        """
        Obtains the number of lines in the buffer.
        This value is cached, so the function is very fast.

        :param line
        """

        return len(str(buffer).split(' '))

    def get_char_count(self):

        """
        Gets the number of characters in the buffer;
        :Note:
        That characters and bytes are not the same,
        you can’t e.g. expect the contents of the buffer in string form to be this many bytes long.
        The character count is cached, so this function is very fast.
        """
        return len(str(self.buffer))

    def text_buffer_get_tag_table(self):
        """
        Get the :class:`TextTagTable <GLXCurses.TextTagTable.TextTagTable>` associated with this buffer.
        """
        pass

    def insert(self, text, iter):
        self.iter = iter

        lenght_of_byte = len(text)
        if lenght_of_byte == -1:
            text = None
            self.buffer.insert(iter, text)
            self.emit_insert_text()

        else:
            self.buffer.insert(iter, text)
            self.emit_insert_text()

        return str(self.buffer)

    def insert_at_cursor(self, text):

        print self.insert(text, self.iter)

    def emit_insert_text(self):
        # Create a Dict with everything
        instance = {
            'class': self.__class__.__name__,
            'type': 'insert-text',
            'id': self.id
        }
        # EVENT EMIT

        return instance

    def get_buffer(self):
        return str(self.buffer)

    def view_edit(self):

        for c, value in enumerate(self.buffer):
            try:
                if c == self.tag_no_edit[self.noposition]:
                    self.noposition += 1
                    print c, "no editable"
            except IndexError:
                print c, "editable"

    def insert_interactive(self, text):
        print self.view_edit()
        choice_position = raw_input("Choose a available position in the buffer:")
        self.insert(text, int(choice_position))

        if int(choice_position) >= self.noposition:
            self.insert(text, int(choice_position))
            print "This insertion on the position {} is success".format(choice_position)
            print self.buffer
        elif int(choice_position) < self.noposition:
            self.buffer.remove(text)
            print "This insertion on the position {} is not available " \
                  "retry with a another position available".format(choice_position)


if __name__ == '__main__':
    textbuffer = TextBuffer()
    # print ("Text:      :" + str(textbuffer.get_char_count()))
    # print ("Text:      :" + str(textbuffer.get_line_count(textbuffer.buffer)))
    # print textbuffer.insert('Ceci est un texte', 0)
    # print textbuffer.insert_at_cursor("blabla")
    print textbuffer.insert_interactive("toto")
