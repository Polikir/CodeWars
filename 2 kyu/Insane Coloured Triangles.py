'''

Disclaimer

This Kata is an insane step-up from Avanta's Kata, so I recommend to solve it first before trying this one.

Problem Description

A coloured triangle is created from a row of colours, each of which is red, green or blue. Successive rows, each containing one fewer colour than the last, are generated by considering the two touching colours in the previous row. If these colours are identical, the same colour is used in the new row. If they are different, the missing colour is used in the new row. This is continued until the final row, with only a single colour, is generated.

For example, different possibilities are:

Colour here:            G G        B G        R G        B R
Becomes colour here:     G          R          B          G
With a bigger example:

R R G B R G B B
 R B R G B R B
  G G B R G G
   G R G B G
    B B R R
     B G R
      R B
       G
You will be given the first row of the triangle as a string and its your job to return the final colour which would appear in the bottom row as a string. In the case of the example above, you would be given 'RRGBRGBB', and you should return 'G'.

Constraints

1 <= length(row) <= 10 ** 5

The input string will only contain the uppercase letters 'B', 'G' or 'R'.

The exact number of test cases will be as follows:

100 tests of 100 <= length(row) <= 1000
100 tests of 1000 <= length(row) <= 10000
100 tests of 10000 <= length(row) <= 100000
Examples

triangle('B') == 'B'
triangle('GB') == 'R'
triangle('RRR') == 'R'
triangle('RGBG') == 'B'
triangle('RBRGBRB') == 'G'
triangle('RBRGBRBGGRRRBGBBBGG') == 'G'
'''


def lucas3(x, y):
    tt = [1, 1, 2]
    tmp = 1
    while x > 0:
        tx = (x % 3)
        ty = (y % 3)

        if tx > ty:
            return 0
        tmp *= int(tt[ty] / (tt[tx] * tt[ty - tx]))
        x //= 3
        y //= 3
    return tmp


def triangle(seq):
    d_c = dict({'R': 0, 'G': 1, 'B': 2})
    d_c_i = dict({0: 'R', 1: 'G', 2: 'B'})

    dig = []

    n = len(seq)

    for i in range(n):
        dig.append(d_c[seq[i]])

    sum = 0

    for i in range(n):

        tt = [1, 1, 2]
        lucas35 = 1
        x = i
        y = n - 1
        while x > 0:
            tx = (x % 3)
            ty = (y % 3)

            if tx > ty:
                lucas35 = 0
                break
            lucas35 *= int(tt[ty] / (tt[tx] * tt[ty - tx]))
            x //= 3
            y //= 3

        sum += dig[i] * lucas35 % 3  # sum += dig[i] * math.comb(n - 1, i) % 3

    if n % 2 == 1:
        id = 1
    else:
        id = -1
    return (d_c_i[sum * id % 3])