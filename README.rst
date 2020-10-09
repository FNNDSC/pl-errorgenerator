pl-errormessage
===============

.. image:: https://badge.fury.io/py/errorgenerator.svg
    :target: https://badge.fury.io/py/errorgenerator

.. image:: https://travis-ci.org/FNNDSC/errorgenerator.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/errorgenerator

.. image:: https://img.shields.io/badge/python-3.5%2B-blue.svg
    :target: https://badge.fury.io/py/errorgenerator

.. contents:: Table of Contents


Abstract
--------

``errorgenerator`` is a simple app that raises an error message of `errorType`. If called with an optional ``--customErrorMessage`` the plugin will append the message to the error.

Synopsis
--------

.. code::

    python errorgenerator.py                                        \
        [-v <level>] [--verbosity <level>]                          \
        [--errorType <typeError>]                                   \
        [--customErrorMessage <message>]                            \
        [--delayTime <secondsDelay>]                                \
        [--version]                                                 \
        [--man]                                                     \
        [--meta]                                                    \
        /tmp



Run
----

This ``plugin`` can be run in two modes: natively as a python package or as a containerized docker image.

Using PyPI
~~~~~~~~~~

To run from PyPI, simply do a

.. code:: bash

    pip install errorgenerator

and run with

.. code:: bash

    errorgenerator.py --errorType Exception /tmp

to attach a message to the error, simply do

.. code:: bash

    errorgenerator.py --errorType Exception             \
                      --customErrorMessage Errored      \
                      /tmp


Using ``docker run``
~~~~~~~~~~~~~~~~~~~~

To run using ``docker``, prefix all calls with

.. code:: bash

    docker run --rm                                     \
        fnndsc/pl-errorgenerator errorgenerator.py                        


Examples
--------

Raise a Built-In Error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    docker run --rm                                     \
        fnndsc/pl-errorgenerator errorgenerator.py      \
        --errorType UnboundLocalError                   \
        /tmp


Raise a Built-In Error with a message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    docker run --rm                                     \
        fnndsc/pl-errorgenerator errorgenerator.py      \
        --errorType UnboundLocalError                   \
        --customErrorMessage ErrorOccured               \
        /tmp

Raise a Built-In Error with a Delay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    docker run --rm                                     \
        fnndsc/pl-errorgenerator errorgenerator.py      \
        --errorType UnboundLocalError                   \
        --delayTime 5                                   \
        /tmp

