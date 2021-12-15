Quick Start
##############

运行你的第一个Serwise脚本
==================================

``demo.svl`` 

.. code-block:: c++

    speak: "您好，请告诉我您的姓名"
    set: $welcome, " ，欢迎使用SerWise"
    listen: $name
    speak: $name + $welcome

以上是一个简单的Serwise脚本，serWise脚本的后缀统一规定为*.svl，在成功使用pip安装Serwise后，您可以直接在命令行中输入以下命令运行该脚本

.. code-block:: bash

    serwise  demo.svl

.. only:: html

    .. figure:: images/demo_1.gif
      :width: 600
      :align: center

      dome.svl运行实例



多进程模式
============================

serwise 为脚本编写者提供了多进程服务启动模式， 运行时加入 ``--muti_process`` 选项

.. code-block:: bash

    serwise demo.svl --muti_process


.. only:: html

    .. figure:: images/demo_2.gif       
      :width: 600
      :align: center
      
      多进程运行实例

启动进程
------------------------------------

默认进程创建触发的方式为键盘输入Tab，服务器退出触发方式为键盘输入ESC，更多形式参见 :doc:`解释器配置 <更多配置>`


