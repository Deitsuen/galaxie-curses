import unittest
from TextBuffer import TextBuffer


class test_functions(unittest.TestCase):
    def setUp(self):
        # Before the test start
        self.text_buffer = TextBuffer

    def test_buffer(self):
        assert self.text_buffer.__doc__
        
    def test_buffer_get_line_count(self):
        assert self.text_buffer.text_buffer_get_line_count.__doc__

    def test_buffer_get_char_count(self):
        assert self.text_buffer.text_buffer_get_char_count.__doc__

    def text_buffer_tag_table(self):
        assert self.text_buffer.text_buffer_get_tag_table.__doc__

    def test_buffer_insert(self):
        assert self.text_buffer.text_buffer_insert.__doc__


if __name__ == '__main__':
    unittest.main()
