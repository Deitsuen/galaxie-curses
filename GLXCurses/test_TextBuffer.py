import unittest
from TextBuffer import TextBuffer

class text_functions(unittest.TestCase):

    def test_buffer(self):
        buffer = TextBuffer.__doc__
        assert buffer

    def test_buffer_new(self):
        buffer_new = TextBuffer.text_buffer_new.__doc__
        assert buffer_new

    def test_buffer_get_line_count(self):
        buffer_get_line_count = TextBuffer.text_buffer_get_line_count.__doc__
        assert buffer_get_line_count

    def test_buffer_get_char_count(self):
        buffer_get_char_count = TextBuffer.text_buffer_get_char_count.__doc__
        assert buffer_get_char_count

    def text_buffer_tag_table(self):
        buffer_get_tag_table = TextBuffer.text_buffer_get_tag_table.__doc__
        assert buffer_get_tag_table

    def test_buffer_insert(self):
        buffer_insert= TextBuffer.text_buffer_insert.__doc__
        assert buffer_insert


if __name__ == '__main__':
    unittest.main()