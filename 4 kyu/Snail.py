'''

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
'''

def snail(snail_map):
    result = []
    while len(snail_map) >= 3:
        result = result + get_outer(snail_map)
        snail_map = cut_outer(snail_map)
    result = result + get_outer(snail_map)
    return result


def get_outer(map):
    n = len(map)
    if n == 1:
        return map[0]
    l = map[0]
    r = []
    if n >= 3:
        for i in range(1, n - 1):
            r.append(map[i][n - 1])
    third = map[n - 1]
    third.reverse()
    fourth = []
    if n >= 3:
        for j in range(1, n - 1):
            fourth.append(map[j][0])
    fourth.reverse()
    return l + r + third + fourth


def cut_outer(map):
    n = len(map)
    new = []
    for i in range(1, n - 1):
        new.append(map[i][1:n - 1])
    return new