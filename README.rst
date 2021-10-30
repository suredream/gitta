gitta
========================

This is a tiny tool just for myself to manager credential tokens and coding snippets structure. Simply, it enable me to quickly fetch such information
from my private github repo into any new cloud instance (such as, colab, kaggle, etc) without concerning that these information might leak. Also it automates 
the installation of the tools to save some keystrokes and time.


Usage
-----

Clone this repository and adopt the bootstrap structure for your own project.
This is just a starting point, but I hope a good one. From there on, you should
read and follow https://packaging.python.org/,
the definite resource on Python packaging.

!pip install -q git+https://git@github.com/suredream/gitta.git@main
!gitta aws
!gitta doc/short.md > README.md

Behavior
--------

Flexible invocation
*******************

The application can be run right from the source directory, in different
ways:

1) Treating the bootstrap directory as a package *and* as the main script::

    $ python -m bootstrap arg1 arg2
    Executing bootstrap version 0.2.0.
    List of argument strings: ['arg1', 'arg2']
    Stuff and Boo():
    <class 'bootstrap.stuff.Stuff'>
    <bootstrap.bootstrap.Boo object at 0x7f43d9f65a90>
    
2) Using ``setup.py develop`` (documented `here <https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode>`_)::

    # This installs the bootstrap command linking back
    # to the current checkout, quite neat for development!
    $ python setup.py develop
    ...
    $ bootstrap arg1 arg2


3) Using the bootstrap-runner.py wrapper::

    $ ./bootstrap-runner.py arg1 arg2
    Executing bootstrap version 0.2.0.
    List of argument strings: ['arg1', 'arg2']
    Stuff and Boo():
    <class 'bootstrap.stuff.Stuff'>
    <bootstrap.bootstrap.Boo object at 0x7f149554ead0>

   
Installation sets up bootstrap command
**************************************

Situation before installation::

    $ gitta
    bash: bootstrap: command not found

Installation right from the source tree (or via pip from PyPI)::

    $ python setup.py install

Now, the ``bootstrap`` command is available::

    $ bootstrap arg1 arg2
    Executing bootstrap version 0.2.0.
    List of argument strings: ['arg1', 'arg2']
    Stuff and Boo():
    <class 'bootstrap.stuff.Stuff'>
    <bootstrap.bootstrap.Boo object at 0x7f366749a190>


On Unix-like systems, the installation places a ``bootstrap`` script into a
centralized ``bin`` directory, which should be in your ``PATH``. On Windows,
``bootstrap.exe`` is placed into a centralized ``Scripts`` directory which
should also be in your ``PATH``.
