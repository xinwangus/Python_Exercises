#!/usr/bin/env python3
import re

def myStrip(s, chars=' '):
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
    
if __name__ == '__main__':
    s1 = "  asdsaf  fdsahfas  "
    print(s1.strip())
    print(myStrip(s1))
    s2 = "asdsaf  fdsahfas"
    print(s2.strip('as'))
    print(myStrip(s2, 'as'))
