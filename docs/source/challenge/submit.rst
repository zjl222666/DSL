Submit
##############

Overview
==================================

Here in ``gobigger/submit/``, we provide examples of submission for all teams in our challenge. We also provide basic code here, and participants should implements their owned submission based on the code.

.. code-block:: python

    class BaseSubmission:

        def __init__(self, team_name, player_names):
            self.team_name = team_name
            self.player_names = player_names

        def get_actions(self, obs):
            '''
            Overview:
                You must implement this function.
            '''
            raise NotImplementedError

Note that all submission should extend with ``BaseSubmission``. We will provide ``team_name`` and ``player_names`` for each submission as their basic parameters. ``team_names`` means the name of team which this submission controls. We also know that there are several players in a team, which is relative with the ``player_names`` in the parameters. We will call ``get_actions()`` when we try to get actions from this submission. So that participants should implements ``get_actions()`` in their submission. This function will receive ``obs`` as its parameters, which is the same as what we provide in ``tutorial``. For example, submissions will get ``obs`` as following:

.. code-block:: python

    global_state, player_state = obs

``global_state`` in details:

.. code-block:: python

    {
        'border': [map_width, map_height], # the map size
        'total_time': match_time, # the duration of a game
        'last_time': last_time,   # the length of time a game has been played
        'leaderboard': {
            team_name: team_size
        } # the team with its size in this game
    }

Participants can find their ``team_name`` in submission matched with the ``team_name`` in ``leaderboard``.

``player_state`` in details:

.. code-block:: python

    {
        player_name: {
            'rgb': numpy.ndarray, # vision of this player
            'feature_layers': list(numpy.ndarray), # features of player
            'rectangle': [left_top_x, left_top_y, right_bottom_x, right_bottom_y], # the vision's position in the map
            'overlap': {
                'food': [{'position': position, 'radius': radius}, ...], # the length of food is not sure
                'thorns': [{'position': position, 'radius': radius}, ...], # the length of food is not sure
                'spore': [{'position': position, 'radius': radius}, ...], # the length of food is not sure
                'clone': [{'position': position, 'radius': radius, 'player': player_name, 'team': team_name}, ...], # the length of food is not sure
            }, # all balls' info in vision
            'team_name': team_name, # the team which this player belongs to 
        }
    }

However, we will only provide the submission with the ``player_state`` matched with its players. That means, if ``player_a`` and ``player_b`` (both are player name) are in the team belongs to this submission, and ``player_c`` not belongs to this team, participants will only get ``player_a`` and ``player_b`` in the submission.

After getting the ``obs``, submissions should return ``actions`` in ``get_actions()``. ``actions`` should look like:

.. code-block:: python

    {
        player_a: actions_a,
        player_b: actions_b
    }

Remember that both ``player_a`` and ``player_b`` should be the name in your submission's ``player_names``. And ``actions_a`` should be a list, which contains there items, which are the same with what we propose in action space.


Examples and Test
==================================

We provide ``RandomSubmission`` and ``BotSubmission`` in ``gobigger/submit/``. ``RandomSubmission`` provide actions randomly, and ``BotSubmission`` provide actions based on a script. Both of them could be an example of your submission. More details in code.

We also provide an example for the pipeline of the submission. Please refer to ``gobigger/submit/submission_example/`` for more details. You can also develop your agent in this directory. Once you finish your ``my_submission.py``, you can call ``python -u test.py`` to check your submission and finally get the ``.tar.gz`` file to upload.


Supplements
==================================

If you want to add other things in your submission, such as model checkpoints or any other materials, please place them in ``./supplements`` and tar them with submission. 


Finally
==================================
You should place all your code and materials under ``my_submission/``. Use ``tar zcf submission.tar.gz my_submission/`` to get your final submission files. The final ``submission.tar.gz`` should be:

.. code-block:: python

    - my_submission
    | - __init__.py
    | - my_submission.py
    | - supplements/
        | - checkpoints or other materials

.. note::

    ``__init__.py`` should be an empty file.





