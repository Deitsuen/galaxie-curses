import unittest
from GLXCurses import Entry
from GLXCurses.Utils import glxc_type

entry = Entry()
entry.set_text('test')


class Entry(unittest.TestCase):
    def test_type(self):
        """Test TextBuffer type"""
        self.assertTrue(glxc_type(entry))

    def test_add_text(self):
        entry.add_text('one')
        self.assertEqual(entry.get_text(), 'test' + 'one')
        self.assertEqual(len(entry.get_text()), len('test') + 3)

    def test_remove_text(self):
        while entry.get_text() != 'tes':
            entry.remove_text()
        self.assertEqual(entry.get_text(), 'tes')
        self.assertEqual(len(entry.get_text()), 3)


if __name__ == '__main__':
    unittest.main()
