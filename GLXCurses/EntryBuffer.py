#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
#from GLXCurses.Object import Object

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class EntryBuffer(object):
    # initial_chars: initial buffer text, or None.
    # n_initial_chars: number of characters in initial_chars, or -1.
    def __init__(self, initial_chars=None, n_initial_chars=-1):
        #Object.__init__(self)

        self._min_length_hard_limit = 0
        self._max_length_hard_limit = 65536

        # The length (in characters) of the text in buffer. Allowed values: <=65535. Default value: 0.
        self.length = 0
        # The maximum length (in characters) of the text in the buffer. Allowed values: <=65535. Default value: 0.
        self.max_length = 0
        # The contents of the buffer. Default value: "".
        self.text = ""

    def get_text(self):
        return str(self.text)

    def set_text(self, text):
        if self.get_max_length() <= 0:
            self.text = text
        else:
            self.text = text[:self.get_max_length()]

    # Retrieves the length in bytes of the buffer
    # Returns: The byte length of the buffer.
    def get_bytes(self):
        return sys.getsizeof(self.get_text())

    # Retrieves the length in characters of the buffer.
    # Returns: The number of characters in the buffer.
    def get_length(self):
        return len(self.get_text())

    # Retrieves the maximum allowed length of the text in buffer . see set_max_length().
    # Returns: the maximum allowed number of characters in EntryBuffer, or 0 if there is no maximum.
    def get_max_length(self):
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

        # Because we are like that we return something
        return number_of_characters_actually_deleted

    def emit_deleted_text(self):
        pass

    def emit_inserted_text(self):
        pass

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

    print "Text       : " + str(entrybuffer.get_text())
    print "Char(s)    : " + str(entrybuffer.get_length())
    print "Byte(s)    : " + str(entrybuffer.get_bytes())
    print "Max Char(s): " + str(entrybuffer.get_max_length())
    print ""
    #entrybuffer.set_max_length(10)

    test_to_play = 'c\'est que '
    print "Text       : " + str(entrybuffer.get_text())
    print "Ins Char(s): " + str(entrybuffer.insert_text(8, test_to_play))
    print "Text       : " + str(entrybuffer.get_text())
    print "Char(s)    : " + str(entrybuffer.get_length())
    print "Byte(s)    : " + str(entrybuffer.get_bytes())
    print "Max Char(s): " + str(entrybuffer.get_max_length())
    print ""
    print "Del Char(s): " + str(entrybuffer.delete_text(8, len(test_to_play)))
    print "Text       : " + str(entrybuffer.get_text())
    print "Char(s)    : " + str(entrybuffer.get_length())
    print "Byte(s)    : " + str(entrybuffer.get_bytes())
    print "Max Char(s): " + str(entrybuffer.get_max_length())




