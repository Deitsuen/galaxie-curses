#!/usr/bin/env python
# -*- coding: utf-8 -*-
from GLXCurses.Bin import Bin

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


def constant(f):
    def fset(self, value):
        raise TypeError

    def fget(self):
        return f()

    return property(fget, fset)


class Constants(object):
    ############################
    # Selection Mode Constants #
    ############################
    #####################################
    # ProgressBar Orientation Constants #
    #####################################
    # The ProgressBar Orientation constants specify the orientation and growth direction for a visible progress bar.
    # A horizontal progress bar growing from left to right.
    @constant
    def PROGRESS_LEFT_TO_RIGHT(self):
        return 'PROGRESS_LEFT_TO_RIGHT'
    # A horizontal progress bar growing from right to left.
    @constant
    def PROGRESS_RIGHT_TO_LEFT(self):
        return 'PROGRESS_RIGHT_TO_LEFT'
    # A vertical progress bar growing from bottom to top.
    @constant
    def PROGRESS_BOTTOM_TO_TOP(self):
        return 'PROGRESS_BOTTOM_TO_TOP'
    # A vertical progress bar growing from top to bottom.
    @constant
    def PROGRESS_TOP_TO_BOTTOM(self):
        return 'PROGRESS_TOP_TO_BOTTOM'

    #########################
    # Shadow Type Constants #
    #########################
    # The Shadow Type constants specify the appearance of an outline typically provided by a Frame.
    # No outline
    @constant
    def SHADOW_NONE(self):
        return 'SHADOW_NONE'

    # The outline is beveled inward.
    @constant
    def SHADOW_IN(self):
        return 'SHADOW_IN'

    # The outline is beveled outward like a button.
    @constant
    def SHADOW_OUT(self):
        return 'SHADOW_OUT'

    # The outline itself is an inward bevel, but the frame bevels outward
    @constant
    def SHADOW_ETCHED_IN(self):
        return 'SHADOW_ETCHED_IN'

    # The outline itself is an outward bevel, but the frame bevels inward
    @constant
    def SHADOW_ETCHED_OUT(self):
        return 'SHADOW_ETCHED_OUT'

    # SizeGroup Mode Constants #
    ############################
    # The SizeGroup Mode constants specify the directions in which the size group affects
    # the requested sizes of its component widgets.
    # The group has no affect
    @constant
    def SIZE_GROUP_NONE(self):
        return 'SIZE_GROUP_NONE'

    # The group affects horizontal requisition
    @constant
    def SIZE_GROUP_HORIZONTAL(self):
        return 'SIZE_GROUP_HORIZONTAL'

    # The group affects vertical requisition
    @constant
    def SIZE_GROUP_VERTICAL(self):
        return 'SIZE_GROUP_VERTICAL'

    # The group affects both horizontal and vertical requisition
    @constant
    def SIZE_GROUP_BOTH(self):
        return 'SIZE_GROUP_BOTH'


glxc = Constants()
