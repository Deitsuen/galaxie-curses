import sys
import os

rows, columns = os.popen('stty size', 'r').read().split()
columns = int(columns)

sys.stdout.write('\r')
sys.stdout.write('{:{width}.{width}}'.format(str('_' * columns), width=columns))
sys.stdout.write('\n\n\r')
sys.stdout.write('{:{width}.{width}}'.format('Galaxie-Curses Unit Test script'.upper(), width=columns))
sys.stdout.write('\n\r')
sys.stdout.write('{:{width}.{width}}'.format(str('_' * columns), width=columns))
sys.stdout.write('\n\r')
sys.stdout.flush()
