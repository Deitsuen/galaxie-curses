.. _instalation:

============
Installation
============


Before you start, make sure that you already have installed **Python**, **pip**
and **git**.

For a Debian system:
--------------------

* Install packages

.. code:: bash

    apt-get install python python-pip git


* Then clone Galaxie Curses project from GitHub:

.. code:: bash

    git clone https://github.com/Tuuux/galaxie-curses.git


It will create a folder name ``galaxie-curses`` it contain the ``GLXCurses`` module:

* Create a directory for you program:

.. code:: bash

   mkdir ./SuperApplication


* Enter inside ``SuperApplication`` :

.. code:: bash

   cd ./SuperApplication


* Move the GLXCurses directory inside the ``SuperApplication`` folder:

.. code:: bash

   mv ../galaxie-curses/GLXCurses ./

* Create a MainApp file and import the GLXCurses package

.. code:: python

   #!/usr/bin/env python
   # -*- coding: utf-8 -*-
   import GLXCurses

Next Step:
----------

* Take a look on our example's files
* Enjoy ;-)
