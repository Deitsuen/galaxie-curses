#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyaudio
from math import sin, pi
from struct import pack
from random import sample, randrange

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


try:
    import winsound

    def playsound(frequency, duration):
        winsound.Beep(frequency, duration)
except ImportError:
    import os

    def playsound(frequency, duration):
        #apt-get install beep
        os.system('beep -f %s -l %s' % (frequency, duration))

for freq in range(1, 750, 1):
    playsound(freq, 10)

