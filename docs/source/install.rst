.. _instalation:

============
Installation
============


Before you start, make sure that you already have installed Python, pip 
and git.

For a Debian system:


    apt-get install python python-pip git

Then clone Glaxie Curses project from GitHub::


    git clone https://github.com/Tuuux/galaxie-curses.git

It will create a folder name ``galaxie-curses`` it contain the ``GLXCurses`` module:

Creat a Directory for you program:

.. code:: bash

   mkdir SuperApplication


Enter inside ``SuperApplication`` :

.. code:: bash

   cd ./SuperApplication


Move the GLXCurses diretcory inside thz SuperApplication folder:

.. code:: bash

   mv ../galaxie-curses/GLXCurses ./

Creat a MainApp file and import the GLXCurses package

.. code:: python

   #!/usr/bin/env python
   # -*- coding: utf-8 -*-
   import GLXCurses


