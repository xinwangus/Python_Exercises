#!/usr/bin/env python
import cal24op

# Given 2 Cal24op objects, see if they can make out 24
def two_two_1 (op1, op2):
    if (op1.valid and op2.valid) == False:
        return 0
    for s in ["+","-", "*", "/"]:
        op3 = cal24op.Cal24op(op1, op2, s)
        if op3.valid:
          if (op3.result == 24):
            print (op3.print_result + " = 24 \n")
            return 24
    return 0

def two_two_2 (op1, op2, op3, op4):
    opllist = []
    oprlist = []
    for s in ["+","-", "*", "/"]:
        opl = cal24op.Cal24op(op1, op2, s)
        opllist.append(opl)
        opr = cal24op.Cal24op(op3, op4, s)
        oprlist.append(opr)
    for opl in opllist:
        for opr in oprlist:
            if two_two_1(opl, opr) == 24:
                return 1
    return 0


def two_two_methods (op1, op2, op3, op4):
    if two_two_2(op1, op2, op3, op4) == 1:
        return 1  
    if two_two_2(op1, op3, op2, op4) == 1:
        return 1  
    if two_two_2(op1, op4, op2, op3) == 1:
        return 1
    return 0

def two_one_one (op1, op2, op3, op4):
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
            if two_two_1(opr, op4) == 24:
                return 1
    return 0


def two_one_one_methods (op1, op2, op3, op4):
    if two_one_one(op1, op2, op3, op4) == 1:
        return 1  
    if two_one_one(op1, op3, op2, op4) == 1:
        return 1  
    if two_one_one(op2, op3, op1, op4) == 1:
        return 1
    
    if two_one_one(op1, op2, op4, op3) == 1:
        return 1
    if two_one_one(op1, op4, op2, op3) == 1:
        return 1
    if two_one_one(op2, op4, op1, op3) == 1:
        return 1

    if two_one_one(op1, op3, op4, op2) == 1:
        return 1
    if two_one_one(op1, op4, op3, op2) == 1:
        return 1
    if two_one_one(op3, op4, op1, op2) == 1:
        return 1

    if two_one_one(op2, op3, op4, op1) == 1:
        return 1
    if two_one_one(op2, op4, op3, op1) == 1:
        return 1
    if two_one_one(op3, op4, op2, op1) == 1:
        return 1
    return 0

    
    

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

if two_two_methods (n1o, n2o, n3o, n4o) == 0:
    two_one_one_methods (n1o, n2o, n3o, n4o) 


