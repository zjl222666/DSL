import logging

# setting user logging
user_logging_level = logging.INFO

# setting core logging level
core_logging_level = logging.DEBUG 

# setting path of user database
database_path = "user.sqlite"
database_header = [
    'id',
    'name',
    'age',
    'balance',
    'phone'

]
database_table_name = 'user'

# setting listen method
listen_method = "default"

# setting speak method
speak_method = 'default'

# setting analyzer
analyzer_chosen = 'contain'

# setting process start pattern
user_setting = 'input'  
'''
 - input: console input
 - random: automatically generate
 - None: none user information
 3 modules are support now
'''
user_num = 3


