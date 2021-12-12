
'''
syntax rules:
'''
Parameters_patern = {
    "var": r'^\$[a-z0-9_]+$',
    "expr": r'^((".*")|(\$[a-z0-9_]+))(([\s]*)(\+)([\s]*)((".*")|(\$[a-z0-9_]+)))*$',
    "step_name": r'^[a-z]+$',
    "path": r'^.*$'
}
Parameter_split = ','
command = {r'step' : ['step_name'], 
           r'stepover': [],  
           r'speak': ['expr'],
           r'set': ['var', 'expr'],
           r'listen': ['var'],
           r'import': ['path'],
           r'switch': ['var'],
           r'branch': ['expr', 'step_name'],
           r'default': ['step_name']}
command_split = ':'
change_to_lower = True
comment_char = '#'
