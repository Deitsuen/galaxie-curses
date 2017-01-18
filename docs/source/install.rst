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


	mkdir SuperApplication

Enter inside ``SuperApplication`` :


    cd ./SuperApplication

Move the GLXCurses diretcory inside thz SuperApplication folder:


    mv ../galaxie-curses/GLXCurses ./

Creat a MainApp file:


    touch main.py

Import the Module

    
    import GLXCurses


