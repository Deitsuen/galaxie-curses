import unittest
from GLXCurses import TextBuffer
from GLXCurses.Utils import glxc_type

# Unitest

position = 0
textbuffer = TextBuffer.TextBuffer()


class TestTextBuffer(unittest.TestCase):

    def test_type(self):
        """Test TextBuffer type"""
        self.assertTrue(glxc_type(textbuffer))

    def test_get_line_count_char(self):
        """Test get_line_count() and get_char_count()"""
        self.assertEqual(textbuffer.get_line_count(), 7)
        self.assertEqual(textbuffer.get_char_count(), 36)

    def test_insert(self):
        textbuffer_insert = TextBuffer.TextBuffer().insert
        self.assertEqual(textbuffer_insert(position, 'test')[position], 'test')

    def test_insert_at_cursor(self):
        textbuffer.insert(position, 'Ceci est un texte')
        self.assertEqual(textbuffer.insert_at_cursor("blabla").index('blabla'), position)

    def test_insert_interactive(self):
        textbuffer.view_edit()

        # 0 no editable
        # 1 no editable
        # 2 no editable
        # 3 no editable
        # 4 editable
        # 5 editable
        # 6 editable

        # No Editable
        self.assertFalse(textbuffer.insert_interactive(0, 'toto'))
        self.assertFalse(textbuffer.insert_interactive(1, 'toto'))
        self.assertFalse(textbuffer.insert_interactive(2, 'toto'))
        self.assertFalse(textbuffer.insert_interactive(3, 'toto'))

        # Editable
        self.assertTrue(textbuffer.insert_interactive(4, 'toto'))
        self.assertTrue(textbuffer.insert_interactive(5, 'toto'))
        self.assertTrue(textbuffer.insert_interactive(6, 'toto'))


if __name__ == '__main__':
    unittest.main()
