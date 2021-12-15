import logging

# setting user logging
user_logging_level = logging.INFO

# setting core logging level
core_logging_level = logging.DEBUG 

# setting process create and server quit method
muti_process_method = 'default'

# setting listen method
listen_method = "default"

# setting speak method
speak_method = 'default'

# setting analyzer
analyzer_chosen = 'contain'

# setting process start pattern
user_setting = 'random'  
'''
Optional:
 - input: console input
 - random: automatically generate
 - None: none user information
'''

# setting whether to save the var_cache to sqlite
save_var = True

# setting path of user database
database_path = "user.sqlite"

# setting database header
database_header = [
    'id',
    'name',
    'age',
    'balance',
    'phone'

]

# setting table name to extract
database_table_name = 'user'


