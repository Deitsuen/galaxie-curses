# W.I.P
# !/usr/bin/env python
# -*- coding: utf-8 -*-


class TextTag(object):

    def __init__(self):
        self.color = {
            'white': "\033[0;37m",
            'yellow': "\033[0;33m",
            'green': "\033[0;32m",
            'blue': "\033[0;34m",
            'cyan': "\033[0;36m",
            'red': "\033[0;31m",
            'magenta': "\033[0;35m",
            'black': "\033[0;30m",
            'bold': "\033[1m",
            'underline': "\033[4m",
            'off': "\033[0;0m",
        }

        self.buffer = ['toto', 'tata', 'tutu', 'titi']

    def text_tag(self, text,  start, end, attribute, attribute2='off', attribute3='off'):

        test_tags_apply_one_tags = self.color[attribute] + str(text[start:end])

        if attribute2 or attribute3 != 'off':
            test_tags_apply_tags = self.color[attribute] + self.color[attribute2] + self.color[attribute3] + str(text[start:end])
            return test_tags_apply_tags

        else:
            return test_tags_apply_one_tags

if __name__ == '__main__':
    tag = TextTag()

    print tag.text_tag(tag.buffer, 0, 1, 'bold', 'red', 'underline')

