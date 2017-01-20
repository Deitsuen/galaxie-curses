#!/usr/bin/env python
# -*- coding: utf-8 -*-

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved

from GLXCurses import Widget
from GLXCurses import Application
import curses
import uuid
import logging

__author__ = 'Tuux'


class Statusbar(Widget):
    """
    A Statusbar is usually placed along the bottom of an Application. It may provide a regular
    commentary of the application's status (as is usually the case in a web browser, for example), or may be used to
    simply output a message when the status changes, (when an upload is complete in an FTP client, for example).

    Status bars in GLXCurses maintain a stack of messages.
    The message at the top of the each bar’s stack is the one that will currently be displayed.

    Any messages added to a statusbar’s stack must specify a context id that is used to uniquely identify
    the source of a message. This context id can be generated by
    :func:`GLXCurses.Statusbar.get_context_id() <GLXCurses.Statusbar.Statusbar.get_context_id>`, given a message
    and the statusbar that it will be added to. Note that messages are stored in a stack,
    and when choosing which message to display, the stack structure is adhered to, regardless of the context
    identifier of a message.

    One could say that a statusbar maintains one stack of messages for display purposes, but allows multiple message
    producers to maintain sub-stacks of the messages they produced (via context ids).

    Status bars are created using
    :func:`GLXCurses.Statusbar.new() <GLXCurses.Statusbar.Statusbar.new>`.

    Messages are added to the bar’s stack with
    :func:`GLXCurses.Statusbar.push() <GLXCurses.Statusbar.Statusbar.push>`.

    The message at the top of the stack can be removed using
    :func:`GLXCurses.Statusbar.pop() <GLXCurses.Statusbar.Statusbar.pop>`.

    A message can be removed from anywhere in the stack if its message id was recorded at the time it was added.
    This is done using :func:`GLXCurses.Statusbar.remove() <GLXCurses.Statusbar.Statusbar.remove>`.
    """
    def __init__(self):
        Widget.__init__(self)
        self.set_name('Statusbar')

        # Widget Setting
        self.statusbar_stack = []

        # Make a Style heritage attribute
        if self.get_style().attribute:
            self.attribute = self.get_style().attribute

        self.context_id_dict = dict()

    def new(self):
        """
        Creates a new GLXCurses.Statusbar ready for messages.

        :return: the new Statusbar
        :rtype: GLXCurses.Statusbar
        """
        self.__init__()
        return self

    def get_context_id(self, context_description):
        """
        Returns a new context identifier, given a description of the actual context.

        .. note: the description is not shown in the UI.

        :param context_description: textual description of what context the new message is being used in
        :type context_description: str
        :return: an context_id
        :rtype: int
        """
        if context_description not in self._get_context_id_list():
            self._get_context_id_list()[context_description] = uuid.uuid1().int
            logging.debug(
                "STATUSBAR CONTEXT CREATION: context_id={0} context_description={1}".format(
                    self._get_context_id_list()[context_description],
                    str(context_description)
                )
            )

        return self._get_context_id_list()[context_description]

    def push(self, context_id, text):
        """
        Push a new message onto the statusbar's stack.

        :param context_id: the message’s context id, as returned by get_context_id()
        :type context_id: int
        :param text: the message to add to the statusbar
        :type text: str
        :return: a message id that can be used with remove().
        :rtype: int
        """
        message_id = uuid.uuid1().int
        self.statusbar_stack.append([context_id, text, message_id])
        self.emit_text_pushed(context_id, text)
        return message_id

    def pop(self, context_id):
        """
        Removes the first message in the Statusbar’s stack with the given context id.

        Note that this may not change the displayed message, if the message at the top of the stack has a different
        context id.

        :param context_id: a context identifier
        :type context_id: int
        """
        count = 0
        last_found = None
        last_element = None
        for element in self.statusbar_stack:
            if context_id == element[0]:
                last_found = count
                last_element = element
            count += 1

        if last_found is None:
            pass
        else:
            self.statusbar_stack.pop(last_found)
            self.emit_text_popped(last_element[0], last_element[2])

    def remove(self, context_id, message_id):
        """
        Forces the removal of a message from a statusbar’s stack.
        The exact **context_id** and **message_id** must be specified.

        :param context_id: a context identifier
        :type context_id: int
        :param message_id: a message identifier, as returned by Statusbar.push()
        :type message_id: int
        """
        count = 0
        last_found = None
        last_element = None
        for element in self.statusbar_stack:
            if context_id == element[0] and message_id == element[2]:
                last_found = count
                last_element = element
            count += 1
        if last_found is None:
            pass
        else:
            logging.debug(
                "STATUSBAR REMOVE: index={0} context_id={1} text={2} message_id={3}".format(
                    str(last_found),
                    str(last_element[0]),
                    str(last_element[1]),
                    str(last_element[2])
                )
            )
            self.statusbar_stack.pop(last_found)

    def remove_all(self, context_id):
        """
        Forces the removal of all messages from a statusbar's stack with the exact context_id .

        :param context_id: a context identifier
        :type context_id: int
        """
        for element in self.statusbar_stack:
            if context_id == element[0]:
                self.remove(element[0], element[2])

    def get_message_area(self):
        """
        **NOT IMPLEMENTED: raise NotImplementedError**

        Retrieves the box containing the label widget.

        :return: a Container Box Widget
        :rtype: GLXCurses.Box
        """
        raise NotImplementedError

    def draw(self):
        # Place the status bar from the end of the screen by look if it have a tool bar before
        if self.parent.toolbar:
            line_from_max_screen_height = 2
        else:
            line_from_max_screen_height = 1

        drawing_area = self.get_screen().subwin(
            0,
            0,
            self.get_screen_height() - line_from_max_screen_height,
            self.get_screen_x()
        )
        self.set_curses_subwin(drawing_area)

        # Clean the entire line
        if curses.has_colors():
            self.curses_subwin.addstr(
                0,
                0,
                str(' ' * (self.get_width() - 1)),
                curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_style().get_attr('white', 'STATE_NORMAL'),
                    bg=self.get_style().get_attr('black', 'STATE_NORMAL'))
                )
            )
            self.curses_subwin.insstr(
                str(' '),
                curses.color_pair(self.get_style().get_curses_pairs(
                    fg=self.get_style().get_attr('white', 'STATE_NORMAL'),
                    bg=self.get_style().get_attr('black', 'STATE_NORMAL'))
                )
            )

        # If it have something inside the Statusbar stack they display it but care about the display size
        if len(self.statusbar_stack):
            message_to_display = self.statusbar_stack[-1][1]
            if not len(message_to_display) <= self.get_width() - 1:
                start, end = message_to_display[:self.get_width() - 1], message_to_display[self.get_width() - 1:]
                self.curses_subwin.addstr(
                    0,
                    0,
                    str(start)
                )
                self.curses_subwin.insstr(
                    0,
                    self.get_width() - 1,
                    str(message_to_display[:self.get_width()][-1:])
                )
            else:
                self.curses_subwin.addstr(
                    0,
                    0,
                    str(message_to_display)
                )

    # Siganles
    def emit_text_popped(self, context_id, text, user_data=None):
        """
        Is emitted whenever a new message is popped off a statusbar's stack.

        :param context_id: the context id of the relevant message/statusbar
        :type context_id: int
        :param text: the message that was just popped
        :type text: str
        :param user_data: user data set when the signal handler was connected.
        :type user_data: list
        """
        if user_data is None:
            user_data = list()
        # Create a Dict with everything
        instance = {
            'class': self.__class__.__name__,
            'type': 'text-popped',
            'id': self.id,
            'context_id': context_id,
            'text': text,
            'user_data': user_data
        }
        # EVENT EMIT
        Application().emit('SIGNALS', instance)

    def emit_text_pushed(self, context_id, text, user_data=None):
        """
        Is emitted whenever a new message is popped off a statusbar's stack.

        :param context_id: the context id of the relevant message/statusbar
        :type context_id: int
        :param text: the message that was just popped
        :type text: str
        :param user_data: user data set when the signal handler was connected.
        :type user_data: list
        """
        if user_data is None:
            user_data = list()
        # Create a Dict with everything
        instance = {
            'class': self.__class__.__name__,
            'type': 'text-pushed',
            'id': self.id,
            'context_id': context_id,
            'text': text,
            'user_data': user_data
        }
        # EVENT EMIT
        Application().emit('SIGNALS', instance)

    # Internal Method's
    def _get_context_id_list(self):
        return self.context_id_dict

