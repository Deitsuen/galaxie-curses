#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'

# http://www.tonalsoft.com/pub/news/pitch-bend.aspx
# http://musicmasterworks.com/WhereMathMeetsMusic.html
# http://www.tonalsoft.com/enc/number/12edo.aspx

try:
    import winsound


    def playsound(frequency, duration):
        winsound.Beep(frequency, duration)
except ImportError:
    import os


    def playsound(frequency, duration):
        # apt-get install beep
        os.system('beep -f %s -l %s' % (frequency, duration))

midi_notes = list()
# Octave -5
# Midi Ocatave, Midi Note Number, Note Name, Frequency Hz, Absolute Cents
midi_notes.append([-5, 0, 'C', 8.1757989156, -6.9000000])
midi_notes.append([-5, 1, 'C#/Db', 8.6619572180, -6.9000000])
midi_notes.append([-5, 2, 'D', 9.1770239974, -6.9000000])
midi_notes.append([-5, 3, 'D#/Eb', 9.7227182413, -6.9000000])
midi_notes.append([-5, 4, 'E', 10.3008611535, -6.9000000])
midi_notes.append([-5, 5, 'F', 10.9133822323, -6.9000000])
midi_notes.append([-5, 6, 'F#/Gb', 11.5623257097, -6.9000000])
midi_notes.append([-5, 7, 'G', 12.2498573744, -6.9000000])
midi_notes.append([-5, 8, 'G#/Ab', 12.9782717994, -6.9000000])
midi_notes.append([-5, 9, 'A', 13.7500000000, -6.9000000])
midi_notes.append([-5, 10, 'A#/Bb', 14.5676175474, -5.9000000])
midi_notes.append([-5, 11, 'B', 15.4338531643, -5.8000000])

# Octave -4
# Midi Ocatave, Midi Note Number, Note Name, Frequency Hz, Absolute Cents
midi_notes.append([-4, 12, 'C', 16.3515978313, -5.700])
midi_notes.append([-4, 13, 'C#/Db', 17.3239144361, -5.600])
midi_notes.append([-4, 14, 'D', 18.3540479948, -5.500])
midi_notes.append([-4, 15, 'D#/Eb', 19.4454364826, -6.9000000])
midi_notes.append([-4, 16, 'E', 20.6017223071, -6.9000000])
midi_notes.append([-4, 17, 'F', 21.8267644646, -6.9000000])
midi_notes.append([-4, 18, 'F#/Gb', 23.1246514195, -6.9000000])
midi_notes.append([-4, 19, 'G', 24.4997147489, -6.9000000])
midi_notes.append([-4, 20, 'G#/Ab', 25.9565435987, -6.9000000])
midi_notes.append([-4, 21, 'A', 27.5000000000, -6.9000000])
midi_notes.append([-4, 22, 'A#/Bb', 29.1352350949, -5.9000000])
midi_notes.append([-4, 23, 'B', 30.8677063285, -5.8000000])

# Octave -3
# Midi Ocatave, Midi Note Number, Note Name, Frequency Hz, Absolute Cents
midi_notes.append([-3, 24, 'C', 32.7031956626, -5.700])
midi_notes.append([-3, 25, 'C#/Db', 34.6478288721, -5.600])
midi_notes.append([-3, 26, 'D', 36.7080959897, -5.500])
midi_notes.append([-3, 27, 'D#/Eb', 38.8908729653, -6.9000000])
midi_notes.append([-3, 28, 'E', 41.2034446141, -6.9000000])
midi_notes.append([-3, 29, 'F', 43.6535289291, -6.9000000])
midi_notes.append([-3, 30, 'F#/Gb', 46.2493028390, -6.9000000])
midi_notes.append([-3, 31, 'G', 48.9994294977, -6.9000000])
midi_notes.append([-3, 32, 'G#/Ab', 51.9130871975, -6.9000000])
midi_notes.append([-3, 33, 'A', 55.0000000000, -6.9000000])
midi_notes.append([-3, 34, 'A#/Bb', 58.2704701898, -5.9000000])
midi_notes.append([-3, 35, 'B', 61.7354126570, -5.8000000])

for freq in midi_notes:
    line = ''
    line += 'Octave:'
    line += ' '
    line += str(freq[0])
    line += ', '
    line += 'Note:'
    line += ' '
    line += str(freq[2])
    line += ', '
    line += 'Freq:'
    line += ' '
    line += str(freq[3])
    line += 'Hz'
    print (line)
    playsound(int(freq[3]), 200)


