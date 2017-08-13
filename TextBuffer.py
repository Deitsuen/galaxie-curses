#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import uuid
from copy import deepcopy


# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Adam Bouadil alias "Deitsuen" <adamb27750@orange.fr> all rights reserved


class TextBuffer(object):
    def __init__(self, table=None):

        """
            Create the new textBuffer object
        """

        self.text = 'abc def ghi jkl'
        self.text2 = "tatitatatoto"
        self.buffer = []
        self.slice = ""

        self.tag_no_edit = [0, 1, 2, 3]
        self.tag = "bold"
        self.tag_table = [self.tag_no_edit]
        self.table = [self.tag_no_edit, self.text]
        self.table2 = [self.tag , self.text2]
        # internal
        # Unique ID it permit to individually identify a widget by example for get_focus get_default
        self.id = uuid.uuid1().int
        self.noposition = 0

    def get_line_count(self):

        """
        The get_line_count() method returns the number of lines in the buffer.
        This value is cached, so the function is very fast.

        :param self.buffer
        :return number of line in the buffer
        """

        return len(str(self.buffer).split(' '))

    def get_char_count(self):

        """
        The get_char_count() method returns the number of characters in the buffer;
        note that characters and bytes are not the same,
        you can't e.g. expect the contents of the buffer in string form to be this many bytes long.
        The character count is cached,
        so this function is very fast.

        :return  number of characters in the buffer
        """
        return len(str(self.buffer))

    def text_buffer_get_tag_table(self):
        """
        Get the GtkTextTagTable associated with this buffer.
        """
        pass

    def insert(self, iter):
        """
        The insert() method inserts the contents of text into the textbuffer at the position specified by iter.
        The "insert_text" signal is emitted and the text insertion actually occurs in the default handler for the signal.
        iter is invalidated when insertion occurs (because the buffer contents change),
        but the default signal handler revalidates it to point to the end of the inserted text.

        :param selftext: UTF-8 format text to insert
        :param iter: a position in the buffer
        """
        self.iter = iter

        lenght_of_byte = len(self.text)
        if lenght_of_byte == -1:
            self.text = None
            self.buffer.insert(iter, self.text)
            self.emit_insert_text()

        else:
            self.buffer.insert(iter, self.text)
            self.emit_insert_text()

        return str(self.buffer)

    def insert_at_cursor(self):
        """
        The insert_at_cursor() method is a convenience method that calls the insert() method, using the current cursor position as the insertion point.
        :param text:
        :return:
        """
        print self.insert(self.text, self.iter)

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
            print "This insertion on the position {} is a success".format(choice_position)
            print self.buffer

        elif int(choice_position) < self.noposition:
            self.buffer.remove(text)
            print "This insertion on the position {} is not available " \
                  "retry with a another position available".format(choice_position)
            print self.buffer

    def insert_range(self, start, end):

        text = deepcopy(self.table[start])
        tag = deepcopy(self.table[end])
        if tag not in self.tag_table:
            raise Exception("this tag not in tag_table please choose a another tag in tag_table")

        iter = []
        iter.insert(0, text)
        iter.insert(0, tag)

        print iter


if __name__ == '__main__':
    textbuffer = TextBuffer()
    # print ("Text:      :" + str(textbuffer.get_char_count()))
    # print ("Text:      :" + str(textbuffer.get_line_count(textbuffer.buffer)))
    # print textbuffer.insert('Ceci est un texte', 0)
    # print textbuffer.insert_at_cursor("blabla")
    # print textbuffer.insert_interactive("toto")
    print textbuffer.insert_range(1, 0)
