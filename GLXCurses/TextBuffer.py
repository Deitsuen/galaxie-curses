#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import uuid
from copy import deepcopy
from TextTag import *

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Adam Bouadil alias "Deitsuen" <adamb27750@orange.fr> all rights reserved


class TextBuffer(object):
    def __init__(self):

        """
            Create the new textBuffer object
        """
        # It's a GLXCurse Type
        self.glxc_type = 'GLXCurses.TextBuffer'

        self.text = 'toto'
        self.text2 = "tatitatatoto"
        self.buffer = ["Noedit", "Edit1", "Edit2", "Edit3", "Edit4", "Edit5", "Edit6"]
        self.slice = ""
        self.tag_no_edit = [0, 1, 2, 3]
        self.tag = "bold"
        self.tag_table = [self.tag_no_edit]
        self.table = [self.text, self.tag_no_edit]
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

        return len(''.join(self.buffer))

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

        :param text: UTF-8 format text to insert
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
        return self.buffer

    def insert_at_cursor(self, text):
        """
        The insert_at_cursor() method is a convenience method that calls the insert() method,
        using the current cursor position as the insertion point.

       :param text: UTF-8 format text to insert
        """

        return self.insert(self.iter, text)

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

            print "This insertion on the position {0} is a success".format(iter)
            return self.buffer

        elif int(iter) < self.noposition:
            self.buffer.remove(text)

            print 'This insertion on the position {0} is not available ' \
                  'retry with a another position available \n {1}'.format(iter, self.buffer)
            return []

    def insert_interactive_at_cursor(self, text):
        return self.insert_interactive(self.iter_insert_interactive, text)

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

        iter.insert(0, tag)
        iter.insert(0, text)
        return iter

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
            print " \n \n This insertion on the position {0} is a success".format(position)
            return self.buffer

        elif int(position) < self.noposition:
            iter.remove(text)
            iter.remove(tag)
            print 'This insertion on the position {0} is not available ' \
                  'retry with a another position available \n {1}'.format(position, self.buffer)
            return []

    def insert_with_tags(self, iter, text, tags='off', tags2='off', tags3='off'):
        """
        The insert_with_tags() method inserts the specified text into the textbuffer at the location specified by iter,
        applying any optional tags following the first two parameters to the newly-inserted text.
        This method is a convenience method that is equivalent to calling the insert() method,
        then the apply_tag() method on the inserted text.

        :param iter: a position in the buffer
        :param text: UTF-8 text
        :param tags: more optional Tag objects to apply to text
        :param tags2: more optional Tag objects to apply to text
        :param tags3: more optional Tag objects to apply to text
        :return:
        """
        lenght_of_byte = len(text)

        if lenght_of_byte == -1:
            self.text = None
            self.buffer.insert(iter, text)
            self.emit_insert_text()

        elif tags != 'off':
            text_tag_apply = TextTag().text_tag(text, 0, 42, tags, tags2, tags3)
            self.buffer.insert(iter, text_tag_apply)
            self.emit_insert_text()
            return text_tag_apply

        elif tags == 'off':
            self.buffer.insert(iter, text)
            self.emit_insert_text()
            return self.buffer

if __name__ == '__main__':
    textbuffer = TextBuffer()
    # print ("Text:      :" + str(textbuffer.get_char_count()))
    # print ("Text:      :" + str(textbuffer.get_line_count(textbuffer.buffer)))
    # print textbuffer.insert(0, 'Ceci est un texte')
    # print textbuffer.insert_at_cursor("blabla")
    # print textbuffer.insert_range(textbuffer.buffer, 1, 0)
    # print textbuffer.insert_interactive(4, 'toto')
    # print textbuffer.insert_range_interactive(textbuffer.buffer, 0, 0, 1)
    # print textbuffer.view_edit()
    print textbuffer.insert_with_tags(4, 'test', 'blue', 'bold', 'underline')

