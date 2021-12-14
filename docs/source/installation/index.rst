安装教程
##############

前置配置要求
=================

操作系统:

    * Centos 7
    * Windows 10
    * MacOS 

Python版本: 3.8.8

获取并安装SerWise解释器
=============================

用以下命令下载SerWise项目包

.. code-block:: bash

    git clone https://github.com/zjl222666/DSL.git

进入下载路径，使用pip工具包安装该项目包:

.. code-block:: bash

    # install for use
    # Note: use `--user` option to install the related packages in the user own directory(e.g.: ~/.local)
    pip install . --user
     
    # install for development(if you want to modify the core)
    pip install -e . --user


