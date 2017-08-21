# W.I.P
# !/usr/bin/env python
# -*- coding: utf-8 -*-


class Tag(object):

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
            'off': "\033[0;0m"
        }

        self.buffer = ['toto', 'tata', 'tutu', 'titi']

    def text_tag(self, text,  start, end, attribute, attribute2='off', attribute3='off'):
        print self.color[attribute] + self.color[attribute2] + self.color[attribute3] + str(text[start:end])

    def tag_bold(self):
        print self.text_tag(self.buffer, 0, 4, 'bold')

    def tag_underline(self):
        print self.text_tag(self.buffer, 0, 4, 'underline')

if __name__ == '__main__':
    tag = Tag()

    print tag.text_tag(tag.buffer, 0, 1, 'bold')
    print tag.tag_bold()
    print tag.tag_underline()

