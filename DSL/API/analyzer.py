'''
overview:
    define your Analyzer here

rules: 
    input: object need to analysed
    output: boolean
    note:    
        you need to make the analyzer correspond to a string one by one in dict `Analyzer_dict`:
'''

def is_query(s: str) -> bool:
    if "查询" in s:
        return True
    else: 
        return False

def is_repay(s: str) -> bool:
    if "还款" in s:
        return True
    else: 
        return False

def is_end(s: str) -> bool:
    if "结束" in s:
        return True
    else: 
        return False


Analyzer_dict = {
   "查询": is_query,
   "还款": is_repay,
   "结束": is_end
}


