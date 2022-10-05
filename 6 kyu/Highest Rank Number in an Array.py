'''
DESCRIPTION:

Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples

[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3

'''

def highest_rank(arr):
    di = dict()
    x = []
    for y in arr:
        di[y] = di.get(y,0) + 1
    for t in di:
        x.append((di[t], t))
    x.sort()
    return x[-1][1]
