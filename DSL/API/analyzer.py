'''
overview:
    define your Analyzer here

rules: 
    input: 
        - pattern: need 
        - s:
        - kwarg
    output: boolean
    note:    
        you need to make the analyzer correspond to a string one by one in dict `Analyzer_dict`:
'''
import re


def equal_analyzer(pattern : str, s: str, kwarg):
    return pattern == s


def contain_analyzer(pattern :str, s: str, kwarg):
    
    if "len" in kwarg and pattern.isdigit():
        return len(s) == int(pattern)
    if pattern == "合法姓名":
        p = r"^[a-z]*$"
        if re.match(p, s):
            return True
        else:
            return False
    return pattern in s
Analyzer_dict = {
    "default": equal_analyzer,
    "contain": contain_analyzer
}


