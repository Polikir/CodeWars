'''
DESCRIPTION:

Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
'''

def array_diff(a, b):
    sa = set({})
    sb = set({})
    for k in a:
        sa.add(k)
    for k in b:
        sb.add(k)
    sp = list(sa&sb)
    for x in sp:
        if x in a:
            i = 0
            while -1 < i <  len(a) and x in a:
                i = a.index(x)
                a.pop(i)
    return a