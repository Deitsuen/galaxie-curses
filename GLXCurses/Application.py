#!/usr/bin/env python
# -*- coding: utf-8 -*-

import GLXCurses

import curses
import sys
import os
import locale
import uuid

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

    def __call__(cls, *args, **kw):
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

            ``x`` location of the ``main_window`` supposed to be the children widgets area, it value can change when a \
            menu is added

              +---------------+-------------------------------+
              | Type          | :py:data:`int`                |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | 0                             |
              +---------------+-------------------------------+

        .. py:data:: y

            ``y`` location of the ``main_window`` supposed to be the children widgets area, it value can change when a \
            menu is added

              +---------------+-------------------------------+
              | Type          | :py:data:`int`                |
              +---------------+-------------------------------+
              | Flags         | Read / Write                  |
              +---------------+-------------------------------+
              | Default value | 0                             |
              +---------------+-------------------------------+


        """
        self.glxc_type = 'GLXCurses.Application'
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

        # Curses setting
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
        self.attribute = self.get_style().get_attribute_states()

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
        ``x`` location of the ncurses subwin call ``main_window``, it area is use to display a \
        :class:`Window <GLXCurses.Window.Window>`

        :return: ``x`` location in char, 0 correspond to left
        :rtype: int
        """
        return self.x

    def set_x(self, x):
        """
        ``x`` location of the ncurses subwin call ``main_window``, it area is use to display a \
        :class:`Window <GLXCurses.Window.Window>`

        :param x: ``x`` location in char, 0 correspond to left

        """
        if type(x) == int:
            if self.get_x() != x:
                self.x = x
        else:
            raise TypeError(u'>x< parameter is not int type')

    def get_y(self):
        """
        ``y`` location of the ncurses subwin call ``main_window``, it area is use to display a \
        :class:`Window <GLXCurses.Window.Window>`

        :return: ``y`` location in char, 0 correspond to top
        :rtype: int
        """
        return self.y

    def set_y(self, y):
        """
        ``y`` location of the ncurses subwin call ``main_window``, it area is use to display a \
        :class:`Window <GLXCurses.Window.Window>`

        :param y: ``y`` location in char, 0 correspond to top
        :type y: int
        """
        if type(y) == int:
            if self.get_y() != y:
                self.y = y
        else:
            raise TypeError(u'>x< parameter is not int type')

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
        """
        Set the Style, it must be a :class:`Style <GLXCurses.Style.Style>` class, with a valid attribute_states

        .. seealso:: :class:`Style <GLXCurses.Style.Style>`

        :param style: a :class:`Style <GLXCurses.Style.Style>` previously declared
        :type style: GLXCurses.Style
        :raise TypeError: if ``style`` parameter is not a :class:`Style <GLXCurses.Style.Style>` type
        """
        if hasattr(style, 'glxc_type') and style.glxc_type == 'GLXCurses.Style':
            if style != self.get_style():
                self.style = style
        else:
            raise TypeError(u'>style< is not a GLXCurses.Style type')

    def get_style(self):
        """
        Return the global Galaxie Curses Style

        .. seealso:: :class:`Style <GLXCurses.Style.Style>`

        :return: a Galaxie Curses Style dictionary
        :rtype: dict
        """
        return self.style

    def add_window(self, window):
        """
        Add a :class:`Window <GLXCurses.Window.Window>` widget to the\
        :class:`Application <GLXCurses.Application.Application>` windows children's list.

        :param window: a window to add
        :type window: GLXCurses.Window
        :raise TypeError: if ``window`` parameter is not a :class:`Window <GLXCurses.Window.Window>` type
        """
        # Check if window is a Galaxie Class
        if hasattr(window, 'glxc_type') and window.glxc_type == 'GLXCurses.Window':
            # set the Application it self as parent of the child window
            window.set_parent(self)
            # create a dictionary structure for add it to windows list
            self._add_child_to_windows_list(window)
            # Make the last element active
            self._set_active_window(self._get_windows_list()[-1]['WIDGET'])
            #self._set_active_window(window)
            #self.refresh()
        else:
            raise TypeError(u'>window< is not a GLXCurses.Window type')

    def remove_window(self, window):
        """
        Remove a :class:`Window <GLXCurses.Window.Window>` widget from the\
        :class:`Application <GLXCurses.Application.Application>` windows children's list.

        Set"application" and "parent' attribute of the :func:`GLXCurses.Window <GLXCurses.Window.Window>`
        to :py:obj:`None`.

        :param window: a window to add
        :type window: GLXCurses.Window
        """
        if hasattr(window, 'glxc_type') and window.glxc_type == 'GLXCurses.Window':
            # Detach the children
            window.set_parent(None)
            window.set_application(None)

            # Search for the good window id and delete it from the window list
            count = 0
            last_found = None
            for child in self._get_windows_list():
                if child['ID'] == window.get_widget_id():
                    last_found = count
                count += 1

            if last_found is not None:
                self._get_windows_list().pop(last_found)
                if len(self._get_windows_list()) - 1 >= 0:
                    self._set_active_window(self._get_windows_list()[-1]['WIDGET'])

            self.refresh()
        else:
            raise TypeError(u'>window< is not a GLXCurses.Window type')

    def add_menubar(self, menubar):
        """
        Sets the menubar of application .

        This can only be done in the primary instance of the application, after it has been registered.
        “startup” is a good place to call this.

        :param menubar: a :class:`MenuBar <GLXCurses.MenuBar.MenuBar>`
        :type menubar: GLXCurses.MenuBar or
        """
        if hasattr(menubar, 'glxc_type') and menubar.glxc_type == 'GLXCurses.MenuBar':
            menubar.set_parent(self)
            self._set_menubar(menubar)
            self.refresh()
        else:
            raise TypeError(u'>menubar< is not a GLXCurses.MenuBar')

    def remove_menubar(self):
        """
        Unset the menubar of application
        """
        if self._get_menubar() is not None:
            self._get_menubar().set_parent(None)
        self._set_menubar(None)
        self.refresh()

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

        It's a central refresh point for the entire application.
        """
        # Clean the screen
        self.screen.clear()

        # Calculate the Main Window size
        self.draw()

        # Check main curses_subwin to display
        if self.curses_subwin is not None:
            if self._get_active_window() is not None:
                self._get_active_window().draw()

        if hasattr(self._get_menubar(), 'glxc_type') and self._get_menubar().glxc_type == 'GLXCurses.MenuBar':
            self._get_menubar().draw()

        if self.statusbar is not None:
            self.statusbar.draw()

        if self.toolbar is not None:
            self.toolbar.draw()

        # After have redraw everything it's time to refresh the screen
        self.get_screen().refresh()

    def draw(self):
        """
        Special code for rendering to the screen
        """
        parent_height, parent_width = self.screen.getmaxyx()

        if self._get_menubar() is not None:
            menu_bar_height = 1
        else:
            menu_bar_height = 0

        if self.statusbar is not None:
            status_bar_height = 1
        else:
            status_bar_height = 0

        if self.message_bar is not None:
            message_bar_height = 1
        else:
            message_bar_height = 0

        if self.toolbar is not None:
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
        A Application must be close properly for permit to Curses to clean up everything and get back the tty \
        in startup condition

        Generally that is follow  by a sys.exit(0) for generate a exit code.
        """
        # Set everything back to normal
        self.screen.keypad(False)
        curses.echo()
        curses.nocbreak()
        curses.endwin()

    # Focus and Selection
    def get_default(self):
        return self.widget_it_have_default

    def set_default(self, widget_unique_id):
        self.widget_it_have_default = widget_unique_id

    def get_is_focus(self):
        """
        Return the unique id of the widget it have been set by \
        :func:`Application.set_is_focus() <GLXCurses.Application.Application.set_is_focus()>`

        .. seealso:: \
         :func:`Application.set_is_focus() <GLXCurses.Application.Application.set_is_focus()>`

         :func:`Widget.get_widget_id() <GLXCurses.Widget.Widget.get_widget_id()>`

        :return: a unique id
        :rtype: int
        """
        return self.widget_it_have_focus

    def set_is_focus(self, widget):
        """
        Determines if the widget is the focus widget within its toplevel. \
        (This does not mean that the “has-focus” property is necessarily set; “has-focus” will only be set \
        if the toplevel widget additionally has the global input focus.)

        .. seealso:: \
        :func:`Application.get_is_focus() <GLXCurses.Application.Application.get_is_focus()>`

        :param widget: a GLXCurses Widget
        :type widget: :class:`Widget <GLXCurses.Widget.Widget>`
        """
        if widget is None:
            self.widget_it_have_focus = None
        else:
            self.widget_it_have_focus = widget.get_widget_id()

    def get_tooltip(self):
        return self.widget_it_have_tooltip

    def set_tooltip(self, widget_unique_id):
        self.widget_it_have_tooltip = widget_unique_id

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
            # GLXCurses.signal.connect(detailed_signal, handler, args)

    def disconnect(self, detailed_signal, handler):

        if detailed_signal in self._get_signal_handlers_dict():
            self._get_signal_handlers_dict()[detailed_signal].remove(handler)

    def dispatch(self, detailed_signal, args=None):
        if args is None:
            args = []

        if detailed_signal in self._get_signal_handlers_dict():
            for handler in self._get_signal_handlers_dict()[detailed_signal]:
                handler(self, detailed_signal, args)

        if self._get_active_window():
            self._get_active_window().handle_and_dispatch_event(detailed_signal, args)

    # Internal
    def _get_signal_handlers_dict(self):
        return self.event_handlers

    def _get_windows_list(self):
        """
        Internal method for return self.windows list

        :return: Windows children list
        :rtype: list
        """
        return self.windows

    def _set_windows_list(self, windows_list=list()):
        """
        Internal method for set self.windows list

        :param windows_list: a windows children list
        :type windows_list: list
        """
        if type(windows_list) == list:
            if windows_list != self._get_windows_list():
                self.windows = windows_list
        else:
            raise TypeError(u'>windows_list< is not a int type')

    def _add_child_to_windows_list(self, window):
        """
        Create a dictionary structure for add it to windows list

        :param window: a Window to add on children windows list
        :type window: GLXCurses.Window
        """
        child_info = dict()
        child_info['WIDGET'] = window
        child_info['TYPE'] = window.glxc_type
        child_info['ID'] = window.get_widget_id()
        self._get_windows_list().append(child_info)

    def _set_active_window_id(self, window_id):
        """
        Set the active_window_id attribute

        :param window_id: a uuid generate by Widget
        :type window_id: long
        """
        if type(window_id) == type(uuid.uuid1().int):
            if window_id != self._get_active_window_id():
                self.active_window_id = window_id
        else:
            raise TypeError(u'>window_id< is not a long type')

    def _get_active_window_id(self):
        """
        Return the active_window_id attribute

        :return: active_window_id attribute
        :rtype: list
        """
        return self.active_window_id

    def _set_active_window(self, window):
        """
        Set the window widget passed as argument as active

        :param window: a window to add
        :type window: GLXCurses.Window
        :return:
        """
        if window.get_widget_id() != self._get_active_window_id():
            self._set_active_window_id(window.get_widget_id())

    def _get_active_window(self):
        """
        Return A :class:`Window <GLXCurses.Window.Window>` widget if any.

        A return to None mean it have no :class:`Window <GLXCurses.Window.Window>` to display

        :return: A :class:`Window <GLXCurses.Window.Window>` widget if any or None
        :rtype: GLXCurses.Window or None
        """
        # Search for the good window id to display
        windows_to_display = None
        for child in self._get_windows_list():
            if child['ID'] == self._get_active_window_id():
                windows_to_display = child['WIDGET']

        # If a active window is found
        if windows_to_display is not None:
            return windows_to_display
        else:
            return None

    def _set_menubar(self, menubar=None):
        """
        Set the menubar attribute

        :param menubar: A :class:`MenuBar <GLXCurses.MenuBar.MenuBar>` or None
        :type menubar: GLXCurses.MenuBar or None
        """
        if (hasattr(menubar, 'glxc_type') and menubar.glxc_type == 'GLXCurses.MenuBar') or (menubar is None):
            self.menubar = menubar
        else:
            raise TypeError(u'>menubar< is not a GLXCurses.MenuBar or None type')

    def _get_menubar(self):
        """
        Return menubar attribute

        :return: A :class:`MenuBar <GLXCurses.MenuBar.MenuBar>`
        :rtype: GLXCurses.MenuBar or None
        """
        return self.menubar
