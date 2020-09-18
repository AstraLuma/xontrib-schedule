**xontrib-schedule** defines the ``schedule`` builtin, which is strongly based on schedule_ with some
additions for non-periodic tasks.

Installation
------------

To install use pip:

.. code-block:: bash

    xpip install xontrib-schedule  # or from git: xpip install git+https://github.com/AstraLuma/xontrib-schedule
    # and load:
    xontrib load schedule

Usage
-----

``schedule.when(<time>).do()`` performs a task at some absolute time in the future.

``schedule.delay(<time>).do()`` performs a task after a delay.


Example
-------

.. code-block:: bash

    schedule.delay(5).do(lambda: print('hello!'))
    # wait 5 sec
    hello!
    


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
