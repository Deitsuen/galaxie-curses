.. _instalation:

============
Installation
============
You can found the Galaxie Curses Repository here:
https://github.com/Tuuux/galaxie-curses

In any case it consist to copy the package GLXCurses inside you developing project directory.

Before you start, make sure that you already have installed **Python**, **pip** and **git**.

* Then clone Galaxie Curses project from GitHub:

.. code:: bash

    git clone https://github.com/Tuuux/galaxie-curses.git


It will create a folder name ``galaxie-curses`` it contain the ``GLXCurses`` package:

* Create a directory for you application project:

.. code:: bash

   mkdir ./SuperApplication


* Enter inside ``SuperApplication`` :

.. code:: bash

   cd ./SuperApplication


* Move the GLXCurses directory inside the ``SuperApplication`` folder:

.. code:: bash

   mv ../galaxie-curses/GLXCurses ./


Now you can import the GLXCuses package

.. code:: python

   #!/usr/bin/env python
   # -*- coding: utf-8 -*-
   import GLXCurses

Next Step:
----------

* Take a look on our example's files
* Enjoy ;-)
