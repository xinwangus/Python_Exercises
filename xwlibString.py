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

    
# A program to decode North America VIN
# see: https://en.wikipedia.org/wiki/Vehicle_identification_number
def vinCheck(s):
    """Check information about a Vehicle identification number"""
    '''
    This is to demon string slice including left index, NOT include
    right index position!!!
    '''
    # A lot codes are skipped.
    cm_map = {\
	"JA":"Japan Isuzu",\
	"JHL":"Japan Honda",\
	"JHM":"Japan Honda",\
	"JM6":"Japan Mazda",\
	"JT":"Japan Toyota",\
	"1HG":"USA Honda",\
	"4T":"USA Toyota",\
	"2HH":"Canada Acura",\
        "2HN":"Canada Acura",\
    }
    model_year_map = {\
	"A":2010,\
	"B":2011,\
	"C":2012,\
	"D":2013,\
	"E":2014,\
	"F":2015,\
	"G":2016,\
	"H":2017,\
	"J":2018\
    }

    if len(s) != 17:
        return("Invalid Vehicle identification number")

    ret = "Country and Manufacturer: "
    cm2 = s[0:2]
    cm3 = s[0:3]
    if cm3 in cm_map.keys():
        ret += cm_map[cm3]
    elif cm2 in cm_map.keys():
        ret += cm_map[cm2]
    else:
        ret += "Unknown"

    ret += ". Model Year: "
    if s[9] in model_year_map:
        ret += str(model_year_map[s[9]])
    else:
        ret += "Unknown"
        
    return ret 
