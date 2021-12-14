
'''
syntax rules:
'''
Parameters_patern = {
    "var": r'^\$[a-z0-9_]+$',
    "expr": r'^((".*")|(\$[a-z0-9_]+))(([\s]*)(\+)([\s]*)((".*")|(\$[a-z0-9_]+)))*$',
    "step_name": r'^[a-z_]+$',
    "path": r'^.*$'
}
Parameter_split = ','
command = {r'step' : ['step_name'], 
           r'stepover': [],  
           r'set': ['var', 'expr'],
           r'import': ['path'],
           r'goto': ['step_name'],
           r'switch': ['expr'],
           r'listen': ['var', 'kwarg'],
           r'branch': ['expr', 'step_name', 'kwarg'],
           r'speak': ['expr', 'kwarg']}
command_split = ':'
change_to_lower = True
comment_char = '#'
