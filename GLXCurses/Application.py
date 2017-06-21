#!/usr/bin/env python
# -*- coding: utf-8 -*-

import GLXCurses

import curses
import sys
import os
import locale
import functools

# Locales Setting
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved

__author__ = 'Tuux'


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None

    def __call__(cls,*args,**kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance


# https://developer.gnome.org/gtk3/stable/GtkApplication.html
class Application(object):
    """
    :Description:

    Create a Application singleton instance.

    That class have the role of a Controller and a NCurses Wrapper.

    It have particularity to not be a GLXCurses.Widget, then have a tonne of function for be a fake GLXCurses.Widget.

    From GLXCurses point of view everything start with it component. All widget will be display and store inside it
    component.

    Attributes:
        **active_window** --
        The window which most recently had focus.\n
        Default value: :py:obj:`None`


        **app_menu** --
        The GMenuModel for the application menu.\n
        Default value: :py:obj:`None`


        **menubar** --
        The GMenuModel for the menubar.\n
        Default value: :py:obj:`None`


        **register_session** --
        Set this property to :py:obj:`True` to register with the session manager.\n
        Default value: :py:obj:`False`
    """
    __metaclass__ = Singleton

    def __init__(self):
        """
        Initialize the Curses Screen and all attribute
        :Property's Details:

        .. py:data:: width

            The width size in characters, considered as the hard limit.

              +---------------+-------------------------------+
              | Type          | :py:data:`int`                |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | 0                             |
              +---------------+-------------------------------+

        .. py:data:: height

            The height size in characters, considered as the hard limit.

              +---------------+-------------------------------+
              | Type          | :py:data:`int`                |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | 0                             |
              +---------------+-------------------------------+

        .. py:data:: preferred_height

            The preferred height size in characters, considered as the shoft limit.

              +---------------+-------------------------------+
              | Type          | :py:data:`int`                |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | 0                             |
              +---------------+-------------------------------+

        .. py:data:: preferred_width

            The preferred width size in characters, considered as the shoft limit.

              +---------------+-------------------------------+
              | Type          | :py:data:`int`                |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | 0                             |
              +---------------+-------------------------------+

        .. py:data:: name

            Name for the widget Application.

              +---------------+-------------------------------+
              | Type          | :py:data:`char`               |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | Application                   |
              +---------------+-------------------------------+

        .. py:data:: x

            Display Area ``x`` location, that value change when a menu is added.

              +---------------+-------------------------------+
              | Type          | :py:data:`int`                |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | 0                             |
              +---------------+-------------------------------+

        .. py:data:: y

            Display Area ``y`` location, that value change when a menu is added.

              +---------------+-------------------------------+
              | Type          | :py:data:`int`                |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | 0                             |
              +---------------+-------------------------------+


        """
        try:
            # Initialize curses
            os.environ["NCURSES_NO_UTF8_ACS"] = '1'

            self.event_handlers = dict()

            # Initialize curses
            self.screen = curses.initscr()

            # Turn off echoing of keys, and enter cbreak mode,
            # where no buffering is performed on keyboard input
            curses.noecho()
            curses.cbreak()

            # In keypad mode, escape sequences for special keys
            # (like the cursor keys) will be interpreted and
            # a special value like curses.KEY_LEFT will be returned
            self.screen.keypad(1)

        except ValueError:
            sys.stdout.write("Curses library not installed defaulting to standard console output\n")
            sys.stdout.write("Error initializing screen.\n")
            sys.stdout.flush()
            self.close()
            sys.exit(1)

        if not curses.has_colors():
            sys.stdout.write("Your terminal does not support color\n")
            sys.stdout.flush()
            self.close()
            sys.exit(1)
        else:
            curses.start_color()
            curses.use_default_colors()
            self.style = GLXCurses.Style()

        self.screen.clear()

        curses.curs_set(0)
        curses.mousemask(-1)

        # Store GLXC object
        self.menubar = None
        self.main_window = None
        self.statusbar = None
        self.message_bar = None
        self.toolbar = None

        # Store Variables
        self.name = 'Application'
        self.windows_id_number = None
        self.active_window_id = None
        self.windows = list()
        self.attribute = self.style.get_default_style()

        # Controller
        self.widget_it_have_default = None
        self.widget_it_have_focus = None
        self.widget_it_have_tooltip = None

        # Fake Widget
        self.curses_subwin = None
        self.spacing = 0
        self.decorated = 0
        self.screen_height = 0
        self.screen_width = 0
        self.screen_y = 0
        self.screen_x = 0
        self.parent_y = 0
        self.parent_x = 0
        self.parent_width = 0
        self.parent_height = 0
        self.y = 0
        self.x = 0
        self.width = 0
        self.height = 0
        self.preferred_height = 0
        self.preferred_width = 0
        self.natural_height = 0
        self.natural_width = 0
        self.preferred_size = 0

        self.parent_spacing = 0
        self.parent_style = self.style

    # Parent
    def set_parent(self, parent=None):
        """
        Suppose to set the parent, but Application haven't any parent, and don't need.
        That method exist for be compatible with a normal Widget.

        :param parent: what you want it will be ignore
        """
        pass

    def get_parent(self):
        """
        Return the area

        :return:
        """
        return self.curses_subwin

    def get_parent_size(self):
        return self.get_parent().getmaxyx()

    def get_parent_origin(self):
        return self.get_parent().getbegyx()

    def get_parent_spacing(self):
        return self.get_parent().spacing

    def get_parent_style(self):
        return self.style

    # Widget
    def get_curses_subwin(self):
        return self.curses_subwin

    def get_origin(self):
        return self.curses_subwin.getbegyx()

    def get_spacing(self):
        return self.spacing

    def get_decorated(self):
        return self.decorated

    def remove_parent(self):
        pass

    def get_screen(self):
        return self.screen

    def set_screen(self, screen):
        pass

    # Size management
    def get_width(self):
        """
        Get the :class:`Application <GLXCurses.Application.Application>` :py:obj:`width` property value.

        .. seealso:: \
        :func:`Application.set_width() <GLXCurses.Application.Application.set_width()>`

        :return: :py:obj:`width` property
        :rtype: int
        """
        return self.width

    def set_width(self, width):
        """
        Set the :class:`Application <GLXCurses.Application.Application>` :py:obj:`width` property value.

        .. seealso:: :func:`Application.get_width() <GLXCurses.Application.Application.get_width()>`

        :param width:
        :type width: int
        :raise TypeError: if ``width`` parameter is not a :py:data:`int` type
        """
        if type(width) == int:
            if width != self.get_width():
                self.width = width
                # Can emit signal
        else:
            raise TypeError(u'>width< argument must be a int type')

    def get_height(self):
        """
        Get the :py:obj:`height` property value.

        .. seealso:: \
        :func:`Application.set_height() <GLXCurses.Application.Application.set_height()>`

        :return: :py:obj:`height` property value
        :rtype: int
        """
        return self.height

    def set_height(self, height):
        """
        Set the :py:obj:`height` property.

        .. seealso:: \
        :func:`Application.get_height() <GLXCurses.Application.Application.get_height()>`

        :param height:
        :type height: int
        :raise TypeError: if ``height`` parameter is not a :py:data:`int` type
        """
        if type(height) == int:
            if height != self.get_height():
                self.height = height
                # Can emit signal
        else:
            raise TypeError(u'>height< argument must be a int type')

    def get_preferred_height(self):
        """
        Get the :py:obj:`preferred_height` property.

        .. seealso:: \
        :func:`Application.set_preferred_height() <GLXCurses.Application.Application.set_preferred_height()>`

        :return: :py:obj:`preferred_height` property
        :rtype: int
        """
        return self.preferred_height

    def set_preferred_height(self, preferred_height):
        """
        Set the :py:obj:`preferred_height` property.

        .. seealso:: \
        :func:`Application.set_preferred_height() <GLXCurses.Application.Application.set_preferred_height()>`

        :param preferred_height:
        :type preferred_height: int
        :raise TypeError: if ``preferred_height`` parameter is not a :py:data:`int` type
        """
        if type(preferred_height) == int:
            if preferred_height != self.get_preferred_height():
                self.preferred_height = preferred_height
                # Can emit signal
        else:
            raise TypeError(u'>preferred_height< argument must be a int type')

    def get_preferred_width(self):
        """
        Get the :py:obj:`preferred_width` property.

        .. seealso:: \
        :func:`Application.set_preferred_width() <GLXCurses.Application.Application.preferred_width()>`

        :return: :py:obj:`preferred_width` property
        :rtype: int
        """
        return self.preferred_width

    def set_preferred_width(self, preferred_width):
        """
        Set the :py:obj:`preferred_width` property.

        .. seealso:: \
        :func:`Application.set_preferred_width() <GLXCurses.Application.Application.set_preferred_width()>`

        :param preferred_width:
        :type preferred_width: int
        :raise TypeError: if ``preferred_width`` parameter is not a :py:data:`int` type
        """
        if type(preferred_width) == int:
            if preferred_width != self.get_preferred_width():
                self.preferred_width = preferred_width
                # Can emit signal
        else:
            raise TypeError(u'>preferred_width< argument must be a int type')

    def get_preferred_size(self):
        # should preserve the Y X of ncuses ?
        return self.preferred_size

    def set_preferred_size(self):
        # should preserve the Y X of ncuses ?
        return self.preferred_size

    def get_size(self):
        return self.get_curses_subwin().getmaxyx()

    def get_x(self):
        """
        X Location of the subwindow use for display something inside a area of Curses.Screen.
        O mean on left of screen

        :return: X Location in char
        :rtype: int
        """
        return self.x

    def get_y(self):
        """
        Y Location of the subwindow use for display something inside a area of Curses.Screen.
        O mean on top of screen

        :return: Y Location in char
        :rtype: int
        """
        return self.y

    # GLXCApplication function
    def set_name(self, name):
        """
        Like a widget :class:`Application <GLXCurses.Application.Application>` can be named, which allows you to
        refer to them from config file. You can apply a style to widgets with a particular name.

        .. seealso:: \
        :func:`Application.get_name() <GLXCurses.Application.Application.get_name()>`

        :param name: name for the widget, limit to 256 Char
        :type name: str or unicode
        :raise ValueError: if ``name`` argument length is sup to 256 chars
        :raise TypeError: if ``name`` argument length is not a str or unicode type

        """
        # Check the len in case of injection
        if len(name) <= 256:
            # And accept any string type
            if isinstance(name, str) or isinstance(name, unicode):
                # And check if value have to be change
                if name != self.get_name():
                    self.name = name
                    # Can emit signal
            else:
                raise TypeError(u'>name< argument must str or unicode type')
        else:
            raise ValueError(u'>name< argument length must <= 256 chars')

    def get_name(self):
        """
        Get the :py:obj:`name` property.

        .. seealso:: \
        :func:`Application.set_name() <GLXCurses.Application.Application.set_name()>`

        :return: :py:obj:`name` property value, type depends about how it have been stored via \
        :func:`Application.set_name() <GLXCurses.Application.Application.set_name()>`
        :rtype: str or unicode
        """
        return self.name

    def set_style(self, style):
        self.style = style

    def get_style(self):
        return self.style

    def add_window(self, window):
        """
        Adds a Window to Application .

        This call can only happen after the application has started; typically, you should add new application windows
        in response to the emission of the "activate" signal.

        This call is equivalent to setting the "application" attribute of window to application .

        :param window: a window to add
        :type window: GLXCurses.Window
        """
        window.set_parent(self)
        child_info = dict()
        child_info['WIDGET'] = window
        self.windows.append(child_info)
        self.active_window_id = len(self.windows) - 1

    def remove_window(self, window):
        """
        Remove a window from application .

        If window belongs to application then this call is equivalent to setting the
        "application" attribute of :func:`GLXCurses.Window <GLXCurses.Window.Window>` to :py:obj:`None`.

        The application may stop running as a result of a call to this function.

        :param window: a window to add
        :type window: GLXCurses.Window
        """
        # Detach the children
        window.set_parent(None)
        window.application = None

        # Search for the good window id and delete it from the window list
        count = 0
        last_found = None
        for children_window in self.windows:
            if children_window.id == window.id:
                last_found = count
            count += 1
        if last_found is None:
            pass
        else:
            self.windows.pop(last_found)

        # Update the active_window_id
        self.active_window_id = len(self.windows) - 1

    def add_menubar(self, menu_bar):
        """
        Sets or unsets the menubar of application .

        This can only be done in the primary instance of the application, after it has been registered.
        “startup” is a good place to call this.

        :param menu_bar: a MenuModel or None
        :type menu_bar: a MenuModel or None
        """
        menu_bar.set_parent(self)
        self.menubar = menu_bar

    def remove_menubar(self):
        self.menubar = None

    def add_statusbar(self, glx_statusbar):
        glx_statusbar.set_parent(self)
        self.statusbar = glx_statusbar

    def remove_statusbar(self, glx_statusbar):
        glx_statusbar.un_parent()
        self.statusbar = None

    def add_toolbar(self, glx_toolbar):
        glx_toolbar.set_parent(self)
        self.toolbar = glx_toolbar

    def remove_toolbar(self, glx_toolbar):
        glx_toolbar.un_parent()
        self.toolbar = None

    def refresh(self):
        """
        Refresh the NCurses Screen, and redraw each contain widget's

        It's a central refresh point.
        """
        # Clean the screen
        self.screen.clear()

        # Calculate the Main Window size
        self.draw()

        # Check main curses_subwin to display
        if self.curses_subwin:
            try:
                self.windows[self.active_window_id]['WIDGET'].draw()
            except TypeError:
                pass

        if self.menubar:
            self.menubar.draw()

        if self.statusbar:
            self.statusbar.draw()

        if self.toolbar:
            self.toolbar.draw()

        # After have redraw everything it's time to refresh the screen
        self.get_screen().refresh()

    def draw(self):
        """
        Special code for rendering to the screen
        """
        parent_height, parent_width = self.screen.getmaxyx()
        if self.menubar:
            menu_bar_height = 1
        else:
            menu_bar_height = 0
        if self.statusbar:
            status_bar_height = 1
        else:
            status_bar_height = 0
        if self.message_bar:
            message_bar_height = 1
        else:
            message_bar_height = 0
        if self.toolbar:
            tool_bar_height = 1
        else:
            tool_bar_height = 0

        interface_elements_height = 0
        interface_elements_height += menu_bar_height
        interface_elements_height += message_bar_height
        interface_elements_height += status_bar_height
        interface_elements_height += tool_bar_height

        self.set_height(parent_height - interface_elements_height)
        self.set_width(0)
        begin_y = menu_bar_height
        begin_x = 0
        self.curses_subwin = self.screen.subwin(
            self.get_height(),
            self.get_width(),
            begin_y,
            begin_x
        )
        self.set_preferred_height(self.get_height())
        self.set_preferred_width(self.get_width())
        self.x = begin_x
        self.y = begin_y

    def getch(self):
        """
        Use by the Mainloop for interact with teh keyboard and the mouse.

        getch() returns an integer corresponding to the key pressed. If it is a normal character, the integer value
        will be equivalent to the character. Otherwise it returns a number which can be matched with the constants
        defined in curses.h.

        For example if the user presses F1, the integer returned is 265.

        This can be checked using the macro KEY_F() defined in curses.h. This makes reading keys portable and easy
        to manage.

        .. code-block:: python

           ch = Application.getch()

        getch() will wait for the user to press a key, (unless you specified a timeout) and when user presses a key,
        the corresponding integer is returned. Then you can check the value returned with the constants defined in
        curses.h to match against the keys you want.

        .. code-block:: python

           if ch == curses.KEY_LEFT
               print("Left arrow is pressed")


        :return: an integer corresponding to the key pressed.
        :rtype: int
        """
        return self.screen.getch()

    def close(self):
        """
        A Application must be close for permit to Curses to clean up everything and get back the tty in good condition

        Generaly that is follow  by a sys.exit(0)
        """
        # Set everything back to normal
        self.screen.keypad(False)
        curses.echo()
        curses.nocbreak()
        curses.endwin()

    # Main Loop
    def adopt(self, orphan):
        """
        not implemented yesr
        :param orphan: a poor widget orphan
        """
        pass

    # should be replace by a EventBus
    def emit(self, detailed_signal, args=None):
        if args is None:
            args = list()
        GLXCurses.mainloop.emit(detailed_signal, args)

    def connect(self, detailed_signal, handler, args=None):
        if args is None:
            args = list()

        # check if it's all ready connect if not create it
        if detailed_signal not in self._get_signal_handlers_dict():
            self._get_signal_handlers_dict()[detailed_signal] = list()

        self._get_signal_handlers_dict()[detailed_signal].append(handler)

        if args:
            self._get_signal_handlers_dict()[detailed_signal].append(args)

        # Test about EventBus
        #GLXCurses.signal.connect(detailed_signal, handler, args)

    def disconnect(self, detailed_signal, handler):

        if detailed_signal in self._get_signal_handlers_dict():
            self._get_signal_handlers_dict()[detailed_signal].remove(handler)

    def dispatch(self, detailed_signal, args=None):
        if args is None:
            args = []
        if detailed_signal in self._get_signal_handlers_dict():
            for handler in self._get_signal_handlers_dict()[detailed_signal]:
                handler(self, detailed_signal, args)

        self.windows[self.active_window_id]['WIDGET'].handle_and_dispatch_event(detailed_signal, args)

    # Focus and Selection
    def get_default(self):
        return self.widget_it_have_default

    def set_default(self, widget_unique_id):
        self.widget_it_have_default = widget_unique_id

    def get_is_focus(self):
        return self.widget_it_have_focus

    def set_is_focus(self, widget):
        if widget is None:
            self.widget_it_have_focus = None
        else:
            self.widget_it_have_focus = widget.get_widget_id()

    def get_tooltip(self):
        return self.widget_it_have_tooltip

    def set_tooltip(self, widget_unique_id):
        self.widget_it_have_tooltip = widget_unique_id

    # Internal
    def _get_signal_handlers_dict(self):
        return self.event_handlers
