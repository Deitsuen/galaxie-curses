#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


# Ref Dc: https://developer.gnome.org/gtk3/stable/gtk3-Bindings.html
class Bindings(object):
    """
    Bindings — Key bindings for individual widgets
    """

    def __init__(self):
        self.toto = 0

    def _create_a_binding_set(
            self,
            set_name,
            priority,
            widget_path_pspecs,
            widget_class_pspecs,
            class_branch_pspecs,
            entries,
            current,
            parsed
            ):
        if widget_path_pspecs is None:
            widget_path_pspecs = list()
        if widget_class_pspecs is None:
            widget_class_pspecs = list()
        if widget_path_pspecs is None:
            widget_path_pspecs = list()
        self.toto = 1
        return [
            set_name,
            priority,
            widget_path_pspecs,
            widget_class_pspecs,
            class_branch_pspecs,
            entries,
            current,
            parsed
        ]
