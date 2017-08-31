import unittest
from GLXCurses import TextBuffer
from GLXCurses.Utils import glxc_type

# Unitest

position = 0
textbuffer = TextBuffer()


class TestTextBuffer(unittest.TestCase):

    def test_type(self):
        """Test TextBuffer type"""
        self.assertTrue(glxc_type(textbuffer))

    def test_get_line_count_char(self):
        """Test get_line_count() and get_char_count()"""
        self.assertEqual(textbuffer.get_line_count(), 7)
        self.assertEqual(textbuffer.get_char_count(), 36)

    def test_insert(self):
        self.assertEqual(textbuffer.insert(position, 'test').index('test'), position)
        self.assertEqual(textbuffer.insert(position, 'test')[position], 'test')

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

    def test_insert_range(self):

        # text = textbuffer.table[0]
        # tag = textbuffer.table[1]
        text = 0
        tag = 1
        buffer_test = []

        print textbuffer.insert_range(buffer_test, text, tag)[0]

        self.assertEqual(textbuffer.insert_range(buffer_test, text, tag)[0], textbuffer.table[0])
        self.assertIn(textbuffer.insert_range(buffer_test, text, tag)[0], textbuffer.table)

        self.assertEqual(textbuffer.insert_range(buffer_test, text, tag)[1], textbuffer.table[1])
        self.assertIn(textbuffer.insert_range(buffer_test, text, tag)[1], textbuffer.table)

    def test_insert_range_interactive(self):
        textbuffer.view_edit()
        buffer_test = []

        # 0 no editable
        # 1 no editable
        # 2 no editable
        # 3 no editable
        # 4 editable
        # 5 editable
        # 6 editable

        # No Editable
        self.assertFalse(textbuffer.insert_range_interactive(buffer_test, 0, 0, 1))
        self.assertFalse(textbuffer.insert_range_interactive(buffer_test, 1, 0, 1))
        self.assertFalse(textbuffer.insert_range_interactive(buffer_test, 2, 0, 1))
        self.assertFalse(textbuffer.insert_range_interactive(buffer_test, 3, 0, 1))

        # Editable
        self.assertTrue(textbuffer.insert_range_interactive(buffer_test, 4, 0, 1))
        self.assertTrue(textbuffer.insert_range_interactive(buffer_test, 5, 0, 1))
        self.assertTrue(textbuffer.insert_range_interactive(buffer_test, 6, 0, 1))


if __name__ == '__main__':
    unittest.main()
