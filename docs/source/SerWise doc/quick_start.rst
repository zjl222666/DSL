Quick Start
##############

运行你的第一个Serwise脚本
==================================

``demo.svl`` 

.. code-block:: c++

    set: $welcome, "您好，欢迎使用SerWise"
    listen: $name
    speak: $name + $welcome

以上是一个简单的Serwise脚本


Customize your config
============================

Class ``Server`` use default config to generate a game environment. To customize your environment, you can change the parameters and parse them to ``Server``.

Add more players in a game
------------------------------------

For example, you may want to allow 6 teams and 2 players per team in your game, and then please add ``team_num`` and ``player_num_per_team`` in config and parse it to ``Server``.

.. code-block:: python

    from gobigger.server import Server

    server = Server(dict(
        team_num=6, 
        player_num_per_team=2
    ))

Extend the game time
------------------------------------
If you want to extend the game time to 20 minutes (1200 seconds), you can use the following codes.

.. code-block:: python

    from gobigger.server import Server

    server = Server(dict(
        match_time=1200
    ))

Change the size of the map
------------------------------------

If you want to have a larger map, you can change ``map_width`` and ``map_height`` in config.

.. code-block:: python

    from gobigger.server import Server
    
    server = Server(dict(
        map_width=1000,
        map_height=1000,
    ))


