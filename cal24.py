import cal24op

# Given 2 Cal24op objects, see if they can make out 24
def two_two_1 (op1, op2):
    op1.cal()
    op2.cal()
    if (op1.valid and op2.valid) == False:
        return 0
    for s in ["+","-", "*", "/"]:
        op3 = cal24op.Cal24op(op1.result, op2.result, s)
        op3.cal()
        if op3.valid:
          if (op3.result == 24):
            print (op1.print_result + s + op2.print_result + " = 24 \n")
            return 24
    return 0

def two_two_2 (numbers):
    op1list = []
    op2list = []
    for s in ["+","-", "*", "/"]:
        op1 = cal24op.Cal24op(numbers[0], numbers[1], s)
        op1list.append(op1)
        op2 = cal24op.Cal24op(numbers[2], numbers[3], s)
        op2list.append(op2)
    for op1 in op1list:
        for op2 in op2list:
            if two_two_1(op1, op2) == 24:
                return 1
    return 0

# This is not correct!
def two_one_one (numbers):
    op1list = []
    op2list = []
    for s in ["+","-", "*", "/"]:
        op1 = cal24op.Cal24op(numbers[0], numbers[1], s)
        op1list.append(op1)
        op2 = cal24op.Cal24op(numbers[2], numbers[3], s)
        op2list.append(op2)
    for op1 in op1list:
        for op2 in op2list:
            if two_two_1(op1, op2) == 24:
                return 1
    return 0


def two_two_methods (numbers):
    print(numbers)
    if two_two_2(numbers) == 1:
        return

    tmp = numbers[1]
    numbers[1] = numbers[2]
    numbers[2] = tmp
    print(numbers)
    if two_two_2(numbers) == 1:
        return
    
    tmp = numbers[3]
    numbers[3] = numbers[1]
    numbers[1] = tmp
    print(numbers)
    if two_two_2(numbers) == 1:
        return