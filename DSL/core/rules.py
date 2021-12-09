
Parameters = {
    "string": r'".*"',
    "var": r'\$[a-z0-9_]*',
    "expr": r'[".*"|\$[a-z0-9_]] [+[".*"|\$[a-z0-9_]]]*',
    "step_name": r'[a-z]*'
}
Parameter_split = ','
key_word = [r'step', r'stepover', r'branch', r'speak', r'set', r'listen', r'import', r'swtich']
key_word_split = ':'
need_to_replace = [' ']
change_to_lower = True
comment_char = '#'
