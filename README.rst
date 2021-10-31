gitta
========================

This is a tiny tool just for myself to manager credential tokens and coding snippets structure. Simply, it enable me to quickly fetch such information
from my private github repo into any new cloud instance (such as, colab, kaggle, etc) without concerning that these information might leak. Also it automates 
the installation of the tools to save some keystrokes and time.


Usage
-----

!pip install -q git+https://git@github.com/suredream/gitta.git@main
!gitta aws
!gitta doc/short.md > README.md

Behavior
--------

Setup colab in a few commands
*******************

The application can be used for:

1) clone a private repository:

    $ gitta <repo>
    
2) update a private repository, with git commands:

    $ git commit
    ...
    $ gitta push


3) fetch a single file (snippet) from private repo

    $ giita helpers.py -o

