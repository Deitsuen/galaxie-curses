# -*- coding: utf-8 -*-
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Deitsuen

class TextBuffer():
    """
    :Description:

    You may wish to begin by reading the text widget conceptual overview which gives an overview of all the objects
    and data types related to the text widget and how they work together.

    """
    pass

    def text_buffer_new(self):
        """
         Creates a new :class:`TextBuffer <GLXCurses.TextBuffer.TextBuffer>`

         Returns a new :class:`TextBuffer <GLXCurses.TextBuffer.TextBuffer>`

        """
        pass

    def text_buffer_get_line_count(self):
        """
        Obtains the number of lines in the buffer.
        This value is cached, so the function is very fast.
        """
        pass

    def text_buffer_get_char_count(self):
        """
        Gets the number of characters in the buffer;
        :Note:
        That characters and bytes are not the same,
        you can’t e.g. expect the contents of the buffer in string form to be this many bytes long.
        The character count is cached, so this function is very fast.
        """
        pass

    def text_buffer_get_tag_table(self):
        """
        Get the :class:`TextTagTable <GLXCurses.TextTagTable.TextTagTable>` associated with this buffer.
        """
        pass

    def text_buffer_insert(self):
        """
        Inserts :class:`len <GLXCurses.len.len>` of :class:`text <GLXCurses.text.text>` at position :class:`iter <GLXCurses.iter.iter>`.
        If :class:`len <GLXCurses.len.len>` is -1,
        :class:`text <GLXCurses.text.text>` must be nul-terminated and will be inserted in its entirety.
        Emits the “insert-text” signal;
        insertion actually occurs in the default handler for the signal.
        :class:`iter <GLXCurses.iter.iter>` is invalidated when insertion occurs (because the buffer contents change),
        but the default signal handler revalidates it to point to the end of the inserted text.

        :Parameter:

        +---------------+-------------------------------+
        | Buffer        | :py:data:`TextBuffer`         |
        +---------------+-------------------------------+
        | Iter          | a position in the buffer      |
        +---------------+-------------------------------+
        | Text          | text in UTF-8 format          |
        +---------------+-------------------------------+
        | Len           | length of text in bytes, or -1|
        +---------------+-------------------------------+

        """
        pass

# W.I.P (Work In Progress)
