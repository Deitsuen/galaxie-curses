#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from GLXCurses import Button
from GLXCurses import Widget
from GLXCurses import Application
from GLXCurses.Utils import *

import sys

import logging

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'
__docformat__ = 'reStructuredText'


class EntryBuffer(Widget):
    """
    EntryBuffer — Text buffer for GLXCurses.Entry
    """

    def __init__(self, initial_chars=None, n_initial_chars=-1):

        """
        Create a new EntryBuffer object.

        Optionally, specify initial text to set in the buffer.

        ***Properties***:
        length - The length (in characters) of the text in buffer. Allowed values: <=65535. Default value: 0.
        max_length - The maximum length (in characters) of the text in the buffer. Allowed values: <=65535. Default value: 0.
        text - The contents of the buffer. Default value: "".

        :param initial_chars: initial buffer text, or None
        :param n_initial_chars: number of characters in initial_chars , or -1
        :return: A new EntryBuffer object.
        :rtype: EntryBuffer object
        """
        Widget.__init__(self)

        # Properties
        self.length = 0
        self.max_length = 0
        self.text = ""

        # Internal Properties
        self._min_length_hard_limit = 0
        self._max_length_hard_limit = 65536
        # Unique ID it permit to individually identify a widget by example for get_focus get_default
        self.id = new_id()

    def get_text(self):
        """
        Retrieves the contents of the buffer.

        The memory pointer returned by this call will not change unless this object emits a signal, or is finalized.

        :return: a pointer to the contents of the widget as a string. This string points to internally allocated storage
         in the buffer and must not be freed, modified or stored.
        :rtype: standard C char type.
        """
        return self.text

    def set_text(self, chars, n_chars=-1):
        """
        Sets the text in the buffer.

        This is roughly equivalent to calling EntryBuffer.delete_text() and EntryBuffer.insert_text().

        .. note:: n_chars is in characters, not in bytes.

        :param chars: the new text
        :param n_chars: the number of characters in text , or -1
        :type chars: standard C char type
        :type n_chars: standard C int type
        """
        if self.get_max_length() <= 0:
            if n_chars <= 0:
                self.text = chars
            else:
                self.text = chars[n_chars]
        else:
            if n_chars <= 0:
                self.text = chars[:self.get_max_length()]
            else:
                self.text = chars[:self.get_max_length()][:n_chars]

    def get_bytes(self):
        """
        Retrieves the length in bytes of the buffer.

        .. seealso:: EntryBuffer.get_length().

        :return: The byte length of the buffer.
        :rtype: standard C int type
        """
        return sys.getsizeof(self.get_text())

    def get_length(self):
        """
        Retrieves the length in characters of the buffer.

        :return: The number of characters in the buffer.
        :rtype: standard C int type
        """
        return len(self.get_text())

    def get_max_length(self):
        """
        Retrieves the maximum allowed length of the text in buffer .

        .. seealso:: EntryBuffer.set_max_length().

        :return: the maximum allowed number of characters in EntryBuffer, or 0 if there is no maximum.
        :rtype: standard C int type
        """
        if 0 >= self.max_length:
            return 0
        else:
            return int(self.max_length)

    # Sets the maximum allowed length of the contents of the buffer.
    # If the current contents are longer than the given length, then they will be truncated to fit.
    # max_length -  the maximum length of the entry buffer, or 0 for no maximum.
    # (other than the maximum length of entries.)
    # The value passed in will be clamped to the range 0-65536.
    def set_max_length(self, max_length):
        max_length = int(max_length)
        if 0 > max_length:
            self.max_length = 0
        elif max_length > 65536:
            self.max_length = 65536
        else:
            self.max_length = max_length
        # If the current contents are longer than the given length, then they will be truncated to fit.
        if len(self.get_text()) > self.get_max_length():
            self.set_text(self.get_text())

    # Inserts n_chars characters of chars into the contents of the buffer, at position position .
    # If n_chars is negative, then characters from chars will be inserted until a null-terminator is found.
    # If position or n_chars are out of bounds, or the maximum buffer text length is exceeded,
    # then they are coerced to sane values.
    #
    # Note:
    # That the position and length are in characters, not in bytes.
    #
    # Parameters:
    # position - the position at which to insert text.
    # chars - the text to insert into the buffer.
    # n_chars - the length of the text in characters, or -1
    #
    # Returns:
    # The number of characters actually inserted.
    def insert_text(self, position, chars, n_chars=-1):
        # Convert the string to a list like a master ...
        hash_list = list(self.get_text())

        # Check n_chars
        if n_chars < 0:
            n_chars = len(self.get_text())
        else:
            n_chars = self._clamp_to_the_range(n_chars)

        # Check max_length
        if self.get_max_length() == 0:
            number_of_characters_actually_inserted = len(chars[:n_chars])
        else:
            number_of_characters_actually_inserted = len(chars[:n_chars]) - position

        # Insertion
        hash_list.insert(position, chars[:n_chars])

        # Re assign the buffer text , it will re apply implicitly the max size contain inside self.set_text()
        self.set_text(''.join(hash_list))

        # Emit a signal
        self.emit_inserted_text()

        # Because we are like that we return something
        return number_of_characters_actually_inserted

    # Deletes a sequence of characters from the buffer. n_chars characters are deleted starting at position.
    # If n_chars is negative, then all characters until the end of the text are deleted.
    # If position or n_chars are out of bounds, then they are coerced to sane values.
    #
    # Note:
    # That the positions are specified in characters, not bytes.
    #
    # Parameters:
    # position - the position at which to insert text.
    # n_chars - the length of the text in characters, or -1
    #
    # Returns:
    # The number of characters deleted.
    def delete_text(self, position, n_chars=-1):
        # Convert the string to a list like a master ...
        hash_list = list(self.get_text())

        # Check n_chars
        if n_chars < 0:
            n_chars = len(self.get_text())
        else:
            n_chars = self._clamp_to_the_range(n_chars)

        # Check max_length
        if self.get_max_length() == 0:
            number_of_characters_actually_deleted = n_chars
        else:
            number_of_characters_actually_deleted = len(self.get_text()) - position

        # Delete
        del hash_list[position:int(position + n_chars)]
        # Re assign the buffer text , it will re apply implicitly the max size contain inside self.set_text()
        self.set_text(''.join(hash_list))

        # Check impossible case of number of deleted thing
        if 0 > number_of_characters_actually_deleted:
            number_of_characters_actually_deleted = 0

        # Emit a signal
        self.emit_deleted_text()

        # Because we are like that we return something
        return number_of_characters_actually_deleted

    def add_text(self, chars):
        # Convert the string to a list like a master ...
        hash_list = list(self.get_text())

        hash_list.insert(-1, chars)
        # Re assign the buffer text , it will re apply implicitly the max size contain inside self.set_text()

        # Check impossible case of number of deleted thing

        # Emit a signal
        self.emit_deleted_text()

        # Because we are like that we return something
        return self.set_text(''.join(hash_list))




    def emit_deleted_text(self):
        # Create a Dict with everything
        instance = {
            'class': self.__class__.__name__,
            'type': 'deleted-text',
            'id': self.id
        }
        # EVENT EMIT
        Application().emit('SIGNALS', instance)

    def emit_inserted_text(self):
        # Create a Dict with everything
        instance = {
            'class': self.__class__.__name__,
            'type': 'inserted-text',
            'id': self.id
        }
        # EVENT EMIT
        Application().emit('SIGNALS', instance)

    # INTERNAL

    def _clamp_to_the_range(self, checked_value):
        if checked_value < self._get_min_length_hard_limit():
            checked_value = self._get_min_length_hard_limit()
        elif checked_value > self._get_max_length_hard_limit():
            checked_value = self._get_max_length_hard_limit()
        return checked_value

    def _get_min_length_hard_limit(self):
        return self._min_length_hard_limit

    def _get_max_length_hard_limit(self):
        return self._max_length_hard_limit


if __name__ == '__main__':
    entrybuffer = EntryBuffer()
    entrybuffer.set_text('Comment la vie est belle !!!')

    print("Text       : " + str(entrybuffer.get_text()))
    print("Char(s)    : " + str(entrybuffer.get_length()))
    print("Byte(s)    : " + str(entrybuffer.get_bytes()))
    print("Max Char(s): " + str(entrybuffer.get_max_length()))
    print("")
    # entrybuffer.set_max_length(10)

    test_to_play = 'c\'est que '
    print("Text       : " + str(entrybuffer.get_text()))
    print("Ins Char(s): " + str(entrybuffer.insert_text(8, test_to_play)))
    print("Text       : " + str(entrybuffer.get_text()))
    print("Char(s)    : " + str(entrybuffer.get_length()))
    print("Byte(s)    : " + str(entrybuffer.get_bytes()))
    print("Max Char(s): " + str(entrybuffer.get_max_length()))
    print("")
    print("Del Char(s): " + str(entrybuffer.delete_text(8, len(test_to_play))))
    print("Text       : " + str(entrybuffer.get_text()))
    print("Char(s)    : " + str(entrybuffer.get_length()))
    print("Byte(s)    : " + str(entrybuffer.get_bytes()))
    print("Max Char(s): " + str(entrybuffer.get_max_length()))
