#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import uuid
from copy import deepcopy


# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Adam Bouadil alias "Deitsuen" <adamb27750@orange.fr> all rights reserved


class TextBuffer(object):
    def __init__(self):

        """
            Create the new textBuffer object
        """

        self.text = 'toto'
        self.text2 = "tatitatatoto"
        self.buffer = ["Noedit", "Edit1", "Edit2", "Edit3", "Edit4", "Edit5"]
        self.slice = ""

        self.tag_no_edit = [0, 1, 2, 3]
        self.tag = "bold"
        self.tag_table = [self.tag_no_edit]
        self.table = [self.tag_no_edit, self.text]
        self.table2 = [self.tag, self.text2]
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

    def insert(self, iter, text):
        """
        The insert() method inserts the contents of text into the textbuffer at the position specified by iter.
        The "insert_text" signal is emitted and the text insertion actually occurs in the default handler for the signal.
        iter is invalidated when insertion occurs (because the buffer contents change),
        but the default signal handler revalidates it to point to the end of the inserted text.

        :param self.text: UTF-8 format text to insert
        :param iter: a position in the buffer
        """
        self.iter = iter

        lenght_of_byte = len(text)
        if lenght_of_byte == -1:
            self.text = None
            self.buffer.insert(iter, text)
            self.emit_insert_text()

        else:
            self.buffer.insert(iter, text)
            self.emit_insert_text()

        return str(self.buffer)

    def insert_at_cursor(self, text):
        """
        The insert_at_cursor() method is a convenience method that calls the insert() method,
        using the current cursor position as the insertion point.
        :param text: UTF-8 format text to insert
        """
        print self.insert(self.iter, text)

    def emit_insert_text(self):
        # Create a Dict with everything
        instance = {
            'class': self.__class__.__name__,
            'type': 'insert-text',
            'id': self.id
        }
        # EVENT EMIT

        return instance

    def view_edit(self):
        """
        view_edit() method print a position editable and no editable
        """

        for c, value in enumerate(self.buffer):
            try:
                if c == self.tag_no_edit[self.noposition]:
                    self.noposition += 1
                    print c, "no editable"
            except IndexError:
                print c, "editable"

    def insert_interactive(self, iter, text):
        """
        Like insert() method,
        but the insertion will not occur if iter is at a non-editable location in the buffer.
        Usually you want to prevent insertions at ineditable locations,
        if the insertion results from a user action (is interactive).
        view_edit indicates the editability of text that doesn't have a tag affecting editability applied to it.
        Typically the result of view_get_editable() method is appropriate here.
        :param text: some UTF-8 text
        """
        self.iter_insert_interactive = iter
        self.insert(int(iter), text)

        if int(iter) >= self.noposition:
            print "This insertion on the position {} is a success".format(iter)
            print self.buffer

        elif int(iter) < self.noposition:
            self.buffer.remove(text)
            print "This insertion on the position {} is not available " \
                  "retry with a another position available".format(iter)
            print self.buffer

    def insert_interactive_at_cursor(self, text):
        print textbuffer.insert_interactive(self.iter_insert_interactive, text)

    def insert_range(self, iter, start, end):
        """
        insert_range() method Copies text,tags,and pixbufs
        between start and end (the order of start and end doesn’t matter) and inserts the copy at iter .
        Used instead of simply getting/inserting text because it preserves images and tags.
        If start and end are in a different buffer from buffer , the two buffers must share the same tag table.
        Implemented via emissions of the insert_text and apply_tag signals, so expect those.

        :param start: a position in a TextBuffer
        :param end: another position in the same buffer as start
        """
        text = deepcopy(self.table[start])
        tag = deepcopy(self.table[end])
        if tag not in self.tag_table:
            raise Exception("this tag not in tag_table please choose a another tag in tag_table")

        iter.insert(0, text)
        iter.insert(0, tag)

    def insert_range_interactive(self, iter, position, start, end):
        """
        Same as insert_range(),
        but does nothing if the insertion point isn’t editable.
        The view_edit() method indicates whether the text is editable at iter if no tags enclosing iter affect editability.
        Typically the result of gtk_text_view_get_editable() is appropriate here.
        :param start: a position in a TextBuffer
        :param end: another position in the same buffer as start
        :param iter: a position in a textbuffer
        :param position: a position in iter
        """

        text = deepcopy(self.table[start])
        tag = deepcopy(self.table[end])
        if tag not in self.tag_table:
            raise Exception("this tag not in tag_table please choose a another tag in tag_table")

        iter.insert(position, text)
        iter.insert(position, tag)

        if int(position) >= self.noposition:
            print "This insertion on the position {} is a success".format(position)
            print self.buffer

        elif int(position) < self.noposition:
            self.buffer.remove(text)
            self.buffer.remove(tag)
            print "This insertion on the position {} is not available " \
                  "retry with a another position available".format(position)
            print self.buffer

if __name__ == '__main__':
    textbuffer = TextBuffer()
    # print ("Text:      :" + str(textbuffer.get_char_count()))
    # print ("Text:      :" + str(textbuffer.get_line_count(textbuffer.buffer)))
    # print textbuffer.insert('Ceci est un texte', 0)
    # print textbuffer.insert_at_cursor("blabla")
    # print textbuffer.insert_range_interactive(textbuffer.buffer, 1, 0)
    # print textbuffer.insert_range(textbuffer.buffer, 1, 0)
    # print textbuffer.insert_interactive(1, "toto")
    print textbuffer.view_edit()
    print textbuffer.insert_range_interactive(textbuffer.buffer, 4, 1, 0)
