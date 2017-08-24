import unittest
from GLXCurses import TextBuffer
from GLXCurses.Utils import glxc_type

# Unitest


class TestTextBuffer(unittest.TestCase):

    def test_type(self):
        """Test TextBuffer type"""
        textbuffer = TextBuffer.TextBuffer()
        self.assertTrue(glxc_type(textbuffer))

    def test_get_line_count_char(self):
        """Test get_line_count() and get_char_count()"""
        get_line = TextBuffer.TextBuffer()
        self.assertEqual(get_line.get_line_count(), 2)
        self.assertEqual(get_line.get_char_count(), 7)

    def test_insert(self):
        textbuffer_insert = TextBuffer.TextBuffer().insert
        print textbuffer_insert(0, 'test')[0]
        self.assertEqual(textbuffer_insert(0, 'test')[0], 'test')


