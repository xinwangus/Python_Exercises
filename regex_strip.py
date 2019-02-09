#!/usr/bin/env python3
from xwlibString import stripUsingRe

if __name__ == '__main__':
    s1 = "  asdsaf  fdsahfas  "
    print(s1.strip())
    print(stripUsingRe(s1))
    assert s1.strip() == stripUsingRe(s1)	
    s2 = "asdsaf  fdsahfas"
    print(s2.strip('as'))
    print(stripUsingRe(s2, 'as'))
    assert s2.strip('as') == stripUsingRe(s2, 'as')	
