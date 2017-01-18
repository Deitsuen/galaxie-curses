#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved

from GLXCurses.Constants import glxc
from GLXCurses.Application import Application
from GLXCurses.MainLoop import MainLoop
from GLXCurses.EventBus import EventBus
from GLXCurses.Style import Style
from GLXCurses.Object import Object
from GLXCurses.Widget import Widget
from GLXCurses.Container import Container
from GLXCurses.Bin import Bin
from GLXCurses.Window import Window
from GLXCurses.Frame import Frame
from GLXCurses.Box import Box
from GLXCurses.VBox import VBox
from GLXCurses.HBox import HBox
from GLXCurses.MenuModel import MenuModel
from GLXCurses.Statusbar import Statusbar
from GLXCurses.Toolbar import Toolbar
from GLXCurses.Misc import Misc
from GLXCurses.Label import Label
from GLXCurses.ProgressBar import ProgressBar
from GLXCurses.Button import Button
from GLXCurses.RadioButton import RadioButton
from GLXCurses.CheckButton import CheckButton
from GLXCurses.HSeparator import HSeparator
from GLXCurses.VSeparator import VSeparator
from GLXCurses.EntryBuffer import EntryBuffer

__author__ = "Jerome Ornech"
__copyright__ = "Copyright 2016-2017, The Galaxie Curses Project"
__credits__ = ["Jerome Ornech alias Tuux", "Aurelien Maury alias Mo"]
__license__ = "GNU GENERAL PUBLIC LICENSE 3.0"
__version__ = "0.1"
__maintainer__ = "Jerome Ornech"
__email__ = "tuux@rtnp.org"
__status__ = "Development"

application = Application()
mainloop = MainLoop()
