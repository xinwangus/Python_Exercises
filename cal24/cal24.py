#!/usr/bin/env python
import cal24op

# Given 2 Cal24op objects, see if they can make out 24
def can_make_24 (op1, op2):
    can_make = False
    if (op1.valid and op2.valid) == False:
        return can_make 
    for s in ["+","-", "*", "/"]:
        op3 = cal24op.Cal24op(op1, op2, s)
        if op3.valid and (op3.result == 24):
            print (op3.print_result + " = 24 \n")
            can_make = True
    return can_make

def two_two (op1, op2, op3, op4):
    ok = 0
    opllist = []
    oprlist = []
    for s in ["+","-", "*", "/"]:
        opl = cal24op.Cal24op(op1, op2, s)
        opllist.append(opl)
        opr = cal24op.Cal24op(op3, op4, s)
        oprlist.append(opr)
    for opl in opllist:
        for opr in oprlist:
            if can_make_24(opl, opr):
                ok = 1
    return ok


def two_two_methods (op1, op2, op3, op4):
    ok = 0
    if two_two(op1, op2, op3, op4) == 1:
        ok = 1
    if two_two(op1, op3, op2, op4) == 1:
        ok = 1
    if two_two(op1, op4, op2, op3) == 1:
        ok = 1
    return ok

def two_one_one (op1, op2, op3, op4):
    ok = 0
    opllist = []
    oprlist = []
    for s in ["+","-", "*", "/"]:
        opl = cal24op.Cal24op(op1, op2, s)
        opllist.append(opl)
        
    for opl in opllist:
        for s in ["+","-", "*", "/"]:
            opr = cal24op.Cal24op(opl, op3, s)
            oprlist.append(opr)
            
    for opr in oprlist:
            if can_make_24(opr, op4):
                ok = 1
    return ok


def two_one_one_methods (op1, op2, op3, op4):
    ok = 0
    if two_one_one(op1, op2, op3, op4) == 1:
        ok = 1
    if two_one_one(op1, op2, op4, op3) == 1:
        ok = 1
    if two_one_one(op1, op3, op2, op4) == 1:
        ok = 1
    if two_one_one(op1, op3, op4, op2) == 1:
        ok = 1  
    if two_one_one(op1, op4, op2, op3) == 1: 
        ok = 1
    if two_one_one(op1, op4, op3, op2) == 1:
        ok = 1
    if two_one_one(op2, op3, op1, op4) == 1: 
        ok = 1
    if two_one_one(op2, op3, op4, op1) == 1:
        ok = 1
    if two_one_one(op2, op4, op1, op3) == 1:
        ok = 1
    if two_one_one(op2, op4, op3, op1) == 1:
        ok = 1
    if two_one_one(op3, op4, op1, op2) == 1:
        ok = 1
    if two_one_one(op3, op4, op2, op1) == 1:
        ok = 1
    return ok
    
while True:
	n1str = input("First Number: ")
	n1 = int(n1str)
	n2str = input("Second Number: ")
	n2 = int(n2str)
	n3str = input("Third Number: ")
	n3 = int(n3str)
	n4str = input("Forth Number: ")
	n4 = int(n4str)

	n1o = cal24op.Cal24op(n1)
	n2o = cal24op.Cal24op(n2)
	n3o = cal24op.Cal24op(n3)
	n4o = cal24op.Cal24op(n4)

	m1 = two_two_methods (n1o, n2o, n3o, n4o)
    	m2 = two_one_one_methods (n1o, n2o, n3o, n4o) 

	if m1 == 0 and m2 == 0:
		print("Can not make 24!\n")


