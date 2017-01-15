#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    ###########################
    # Justification Constants #
    ###########################
    @constant
    def JUSTIFY_LEFT():
        """The text is placed at the left edge of the label."""
        return 'JUSTIFY_LEFT'

    @constant
    def JUSTIFY_RIGHT():
        """The text is placed at the right edge of the label."""
        return 'JUSTIFY_RIGHT'

    @constant
    def JUSTIFY_CENTER():
        """The text is placed in the center of the label."""
        return 'JUSTIFY_CENTER'

    @constant
    def JUSTIFY_FILL():
        """The text is placed is distributed across the label."""
        return 'JUSTIFY_FILL'

    #####################################
    # ProgressBar Orientation Constants #
    #####################################
    # The ProgressBar Orientation constants specify the orientation and growth direction for a visible progress bar.
    # A horizontal progress bar growing from left to right.
    @constant
    def PROGRESS_LEFT_TO_RIGHT():
        return 'PROGRESS_LEFT_TO_RIGHT'
    
    # A horizontal progress bar growing from right to left.
    @constant
    def PROGRESS_RIGHT_TO_LEFT():
        return 'PROGRESS_RIGHT_TO_LEFT'
    
    # A vertical progress bar growing from bottom to top.
    @constant
    def PROGRESS_BOTTOM_TO_TOP():
        return 'PROGRESS_BOTTOM_TO_TOP'
    
    # A vertical progress bar growing from top to bottom.
    @constant
    def PROGRESS_TOP_TO_BOTTOM():
        return 'PROGRESS_TOP_TO_BOTTOM'

    #########################
    # Shadow Type Constants #
    #########################
    # The Shadow Type constants specify the appearance of an outline typically provided by a Frame.
    # No outline
    @constant
    def SHADOW_NONE():
        return 'SHADOW_NONE'

    # The outline is beveled inward.
    @constant
    def SHADOW_IN():
        return 'SHADOW_IN'

    # The outline is beveled outward like a button.
    @constant
    def SHADOW_OUT():
        return 'SHADOW_OUT'

    # The outline itself is an inward bevel, but the frame bevels outward
    @constant
    def SHADOW_ETCHED_IN():
        return 'SHADOW_ETCHED_IN'

    # The outline itself is an outward bevel, but the frame bevels inward
    @constant
    def SHADOW_ETCHED_OUT():
        return 'SHADOW_ETCHED_OUT'

    # SizeGroup Mode Constants #
    ############################
    # The SizeGroup Mode constants specify the directions in which the size group affects
    # the requested sizes of its component widgets.
    # The group has no affect
    @constant
    def SIZE_GROUP_NONE():
        return 'SIZE_GROUP_NONE'

    # The group affects horizontal requisition
    @constant
    def SIZE_GROUP_HORIZONTAL():
        return 'SIZE_GROUP_HORIZONTAL'

    # The group affects vertical requisition
    @constant
    def SIZE_GROUP_VERTICAL():
        return 'SIZE_GROUP_VERTICAL'

    # The group affects both horizontal and vertical requisition
    @constant
    def SIZE_GROUP_BOTH():
        return 'SIZE_GROUP_BOTH'

    # Wrap Mode
    # wrap lines at word boundaries.
    @constant
    def WRAP_WORD():
        return 'WRAP_WORD'

    # wrap lines at character boundaries.
    @constant
    def WRAP_CHAR():
        return 'WRAP_CHAR'

    # wrap lines at word boundaries, but fall back to character boundaries if there is not enough space for a full word.
    @constant
    def WRAP_WORD_CHAR():
        return 'WRAP_WORD_CHAR'

    # InputPurpose
    # Describes primary purpose of the input widget.
    # This information is useful for on-screen keyboards and similar input methods
    # to decide which keys should be presented to the user.

    # Allow any character
    @constant
    def INPUT_PURPOSE_FREE_FORM():
        return 'INPUT_PURPOSE_FREE_FORM'

    # Allow only alphabetic characters
    @constant
    def INPUT_PURPOSE_ALPHA():
        return 'INPUT_PURPOSE_ALPHA'

    # Allow only digits
    @constant
    def INPUT_PURPOSE_DIGITS():
        return 'INPUT_PURPOSE_DIGITS'

    # Edited field expects numbers
    @constant
    def INPUT_PURPOSE_NUMBER():
        return 'INPUT_PURPOSE_NUMBER'

    @constant
    def INPUT_PURPOSE_PHONE():
        """Edited field expects phone number"""
        return 'INPUT_PURPOSE_PHONE'

    @constant
    def INPUT_PURPOSE_URL():
        """Edited field expects URL"""
        return 'INPUT_PURPOSE_URL'

    @constant
    def INPUT_PURPOSE_EMAIL():
        """Edited field expects email address"""
        return 'INPUT_PURPOSE_EMAIL'

    @constant
    def INPUT_PURPOSE_NAME():
        """Edited field expects the name of a person"""
        return 'INPUT_PURPOSE_NAME'

    @constant
    def INPUT_PURPOSE_PASSWORD():
        """Like INPUT_PURPOSE_FREE_FORM , but characters are hidden"""
        return 'INPUT_PURPOSE_PASSWORD'

    @constant
    def INPUT_PURPOSE_PIN():
        """Like INPUT_PURPOSE_DIGITS , but characters are hidden"""
        return 'INPUT_PURPOSE_PIN'

    ################
    # Border Style #
    ################
    # Describes how the border of a UI element should be rendered.
    @constant
    def BORDER_STYLE_NONE():
        """No visible border"""
        return 'BORDER_STYLE_NONE'

    @constant
    def BORDER_STYLE_SOLID():
        """A single line segment"""
        return 'BORDER_STYLE_SOLID'

    @constant
    def BORDER_STYLE_INSET():
        """Looks as if the content is sunken into the canvas"""
        return 'BORDER_STYLE_INSET'

    @constant
    def BORDER_STYLE_OUTSET():
        """Looks as if the content is coming out of the canvas"""
        return 'BORDER_STYLE_OUTSET'

    @constant
    def BORDER_STYLE_HIDDEN():
        """Same as BORDER_STYLE_NONE"""
        return 'BORDER_STYLE_HIDDEN'

    @constant
    def BORDER_STYLE_DOTTED():
        """A series of round dots"""
        return 'BORDER_STYLE_DOTTED'

    @constant
    def BORDER_STYLE_DASHED():
        """A series of square-ended dashes"""
        return 'BORDER_STYLE_DASHED'

    @constant
    def BORDER_STYLE_DOUBLE():
        """Two parallel lines with some space between them"""
        return 'BORDER_STYLE_DOUBLE'

    @constant
    def BORDER_STYLE_GROOVE():
        """Looks as if it were carved in the canvas"""
        return 'BORDER_STYLE_GROOVE'

    @constant
    def BORDER_STYLE_RIDGE():
        """Looks as if it were coming out of the canvas"""
        return 'BORDER_STYLE_RIDGE'

glxc = Constants()
