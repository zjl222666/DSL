Installation
##############

Prerequisites
=================

System version:

    * Centos 7
    * Windows 10
    * MacOS 

Python version: 3.6.8

Get and install gobigger
=============================

First get and download the official repository with the following command line.

.. code-block:: bash

    git clone git@gitlab.bj.sensetime.com:zhangming/gobigger.git

You can install from source:

.. code-block:: bash

    # install for use
    # Note: use `--user` option to install the related packages in the user own directory(e.g.: ~/.local)
    pip install . --user
     
    # install for development(if you want to modify DI-drive)
    pip install -e . --user


