'''
DESCRIPTION:

This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
'''


def zero(x=-1):
    if x==-1:
        return 0
    if x[0]=='1':
        return 0+int(x[1])
    if x[0]=='2':
        return 0-int(x[1])
    if x[0]=='3':
        return 0*int(x[1])
    if x[0]=='4':
        return 0//int(x[1])
def one(x=-1):
    if x==-1:
        return 1
    if x[0]=='1':
        return 1+int(x[1])
    if x[0]=='2':
        return 1-int(x[1])
    if x[0]=='3':
        return 1*int(x[1])
    if x[0]=='4':
        return 1//int(x[1])
    return 1#your code here
def two(x=-1):
    if x==-1:
        return 2
    if x[0]=='1':
        return 2+int(x[1])
    if x[0]=='2':
        return 2-int(x[1])
    if x[0]=='3':
        return 2*int(x[1])
    if x[0]=='4':
        return 2//int(x[1])
    return 2#your code here
def three(x=-1):
    if x==-1:
        return 3
    if x[0]=='1':
        return 3+int(x[1])
    if x[0]=='2':
        return 3-int(x[1])
    if x[0]=='3':
        return 3*int(x[1])
    if x[0]=='4':
        return 3//int(x[1])
    return 3#your code here
def four(x=-1):
    if x==-1:
        return 4
    if x[0]=='1':
        return 4+int(x[1])
    if x[0]=='2':
        return 4-int(x[1])
    if x[0]=='3':
        return 4*int(x[1])
    if x[0]=='4':
        return 4//int(x[1])
    return 4
    #your code here
def five(x=-1):
    if x==-1:
        return 5
    if x[0]=='1':
        return 5+int(x[1])
    if x[0]=='2':
        return 5-int(x[1])
    if x[0]=='3':
        return 5*int(x[1])
    if x[0]=='4':
        return 5//int(x[1])
    return 5#your code here
def six(x=-1):
    if x==-1:
        return 6
    if x[0]=='1':
        return 6+int(x[1])
    if x[0]=='2':
        return 6-int(x[1])
    if x[0]=='3':
        return 6*int(x[1])
    if x[0]=='4':
        return 6//int(x[1])
    return 6#your code here
def seven(x=-1):
    if x==-1:
        return 7
    if x[0]=='1':
        return 7+int(x[1])
    if x[0]=='2':
        return 7-int(x[1])
    if x[0]=='3':
        return 7*int(x[1])
    if x[0]=='4':
        return 7//int(x[1])
    return 7#your code here
def eight(x=-1):
    if x==-1:
        return 8
    if x[0]=='1':
        return 8+int(x[1])
    if x[0]=='2':
        return 8-int(x[1])
    if x[0]=='3':
        return 8*int(x[1])
    if x[0]=='4':
        return 8//int(x[1])
    return 8#your code here
def nine(x=-1):
    if x==-1:
        return 9
    if x[0]=='1':
        return 9+int(x[1])
    if x[0]=='2':
        return 9-int(x[1])
    if x[0]=='3':
        return 9*int(x[1])
    if x[0]=='4':
        return 9//int(x[1])
    return 9#your code here

def plus(a):
    return '1'+str(a)#your code here
def minus(a):
    return '2'+str(a)#your code here
def times(a):
    return '3'+str(a)#your code here
def divided_by(a):
    return '4'+str(a)#your code here