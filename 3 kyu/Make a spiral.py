'''
DESCRIPTION:

Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000
and with the size 10:

0000000000
.........0
00000000.0
0......0.0
0.0000.0.0
0.0..0.0.0
0.0....0.0
0.000000.0
0........0
0000000000
Return value should contain array of arrays, of 0 and 1, with the first row being composed of 1s. For example for given size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.

'''
def spiralize(n):
    matrix = [[0 for i in range(n)] for j in range(n)]

    up = 0
    down = n - 1
    left = 0
    right = n - 1

    first = True
    tmp = 0

    while up <= down or left <= right:

        for i in range(left, right + 1):
            matrix[up][i] = 1

        for i in range(up, down + 1):
            matrix[i][right] = 1

        for i in range(right, left - 1, -1):
            matrix[down][i] = 1

        for i in range(down, up + 1, -1):
            matrix[i][left] = 1

        if right - left != 3 and n > 2:
            matrix[up + 2][left + 1] = 1

        if right - left == 1:
            matrix[down][left] = 0
            if n > 2:
                matrix[up + 2][left + 1] = 0

        up += 2
        down -= 2
        left += 2
        right -= 2

    return matrix