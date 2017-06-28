xontrib-schedule
===============================

Defines the ``schedule`` builtin, which is strongly based on schedule_ with some
additions for non-periodic tasks:

``schedule.when(<time>).do()`` performs a task at some absolute time in the future.

``schedule.delay(<time>).do()`` performs a task after a delay.

This module prioritizes task execution over accurate timing.

Installation / Usage
--------------------

To install use pip:

    $ xip install xontrib-schedule


Or clone the repo:

    $ git clone https://github.com/astronouth7303/xontrib-schedule.git
    $ xip install ./xontrib-schedule

And then load it:

    $ xontrib load schedule

Contributing
------------

Fork, submit a pull request, and we'll have a discussion. Keep to PEP8.

Example
-------

TBD

Credits
---------

This package was created with cookiecutter_ and the xontrib_ template.

.. _schedule: https://schedule.readthedocs.io/en/stable/
.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _xontrib: https://github.com/laerus/cookiecutter-xontrib
