.. title:: Galaxie Curses, NCurses ToolKit

============================
Galaxie Curses Documentation
============================
.. figure::  images/logo_galaxie.png
   :align:   center

The Project
-----------
**Galaxie Curses** is a free software ToolKit for the NCurses API.
It can be consider as a text based implementation of the famous GTK+ Library.

Originally the project have start in 2016 when the author Jérôme.O have start to learn Python.

The Mission
-----------
Provide a Text Based ToolKit with powerfull high level Widget (Select Color, Printer Dialog, FileSelector).

During lot of years the main stream was to provide big computer with big GUI Toolkit,
unfortunately almost nobody have care about ultra low profile computer and we are now in a situation where no mature
ToolKit is ready to use on **pen computer**. Time's change then it's time to change the world ...

The goal of the version 1.0 will be to create a application like Midnight-Commander_ with **GLXCurses**.

.. _Midnight-Commander: https://midnight-commander.org

Example
-------

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    import GLXCurses

    # Create the main Application
    app = GLXCurses.Application()
    app.set_name('Galaxie-Curse Container Demo')

    # Create a Window
    win_main = GLXCurses.Window()

    # Create a Frame
    frame1 = GLXCurses.Frame()
    frame1.set_label('A Container Frame')

    # Add the frame to the main window
    win_main.add(frame1)

    # Add the main window inside the application
    app.add_window(win_main)

    # The super function call when press keys
    def handle_keys(self, event_signal, *event_args):
        if event_args[0] == ord('q'):
            # Key "q" was pressed
            GLXCurses.mainloop.quit()

    # Signal
    app.connect('CURSES', handle_keys)

    # Main loop start
    GLXCurses.mainloop.run()

More examples can be found here: https://github.com/Tuuux/galaxie-curses/tree/master/examples

Features
--------
* MainLoop
* Signal
* Application Class
* Component like Button, Container, ProgressBar
* Have GTK+ design as roadmap
* Auto Rezize
* Minimize NCurses crash
* Common thing for a text based graphic interface tool kit :)

Contribute
----------
The GTK+ documentation is our model: https://developer.gnome.org/gtk3/stable/

- Issue Tracker: https://github.com/Tuuux/galaxie-curses/issues
- Source Code: https://github.com/Tuuux/galaxie-curses

Documentations
--------------
.. toctree::
   :maxdepth: 2

   install
   GLXCurses

Note for GTK+ Project Developer's
---------------------------------
I'm really confuse about the big copy/past i making from the GTK+ documentation during the creation of
the Galaxie-Curses documentation, that because english is not my primary language and i'm a bit limited for make a
ToolKit documentation without that ...
Consider that actual documentation of Galaxie-Curse as the better i can do and it
include to copy/past large parts of the GTK+ documentation. (sorry about that)

As you probably see **Galaxie-Curses** is a Text Based **GTK+** like, then the GTK+ Doc is the **roadmap**.

License
-------
GNU GENERAL PUBLIC LICENSE Version 3

See the LICENCE_

.. _LICENCE: https://github.com/Tuuux/galaxie-curses/blob/master/LICENSE

Indices and tables
------------------
* :ref:`genindex`
* :ref:`search`