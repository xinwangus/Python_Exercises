""" Xin's own Python library code related to string"""
'''
Copyright @Xin Wang
''' 
def isProperlyClosed (s, dic={'[':']', '{':'}', '(':')'}):
    """Check if brackets in a string are properly closed, no interlace."""
    nextToClose = []
    left_b = dic.keys()
    right_b = dic.values()
    for c in s:
        if c in left_b:
            nextToClose.append(c)
        elif c in right_b:
            # List already empty
            if (len(nextToClose) == 0):
                return False
            else:
                assert nextToClose[-1] in left_b
            # close does not match open
            if (c != dic[nextToClose[-1]]):
                return False
            else:   
                nextToClose.pop()	
    if len(nextToClose) != 0:
        return False
    else:
        return True

import re
def stripUsingRe(s, chars=' '):
    """Just like Python's string strip function,
       but implemented with regular expression.
       Default is to strip spaces from both ends."""
    if (chars == ' '):
        headp = re.compile(r"^\s*")
        tailp = re.compile(r"\s*$")
        return tailp.sub('', headp.sub('', s))
    else:
        head_re = r"^" + re.escape(chars)
        tail_re = re.escape(chars) + r"$"
        headp = re.compile(head_re)
        tailp = re.compile(tail_re)
        return tailp.sub('', headp.sub('', s))
    
