'''
DESCRIPTION:

If you finish this kata, you can try Insane Coloured Triangles by Bubbler, which is a much harder version of this one.

A coloured triangle is created from a row of colours, each of which is red, green or blue. Successive rows, each containing one fewer colour than the last, are generated by considering the two touching colours in the previous row. If these colours are identical, the same colour is used in the new row. If they are different, the missing colour is used in the new row. This is continued until the final row, with only a single colour, is generated.

The different possibilities are:

Colour here:        G G        B G        R G        B R
Becomes colour:      G          R          B          G
With a bigger example:

R R G B R G B B
 R B R G B R B
  G G B R G G
   G R G B G
    B B R R
     B G R
      R B
       G
'''


def triangle(s):
    new_s = []

    d_c = dict({'R': 0, 'G': 1, 'B': 2})
    d_c_i = dict({0: 'R', 1: 'G', 2: 'B'})

    if len(s) > 1:
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                new_s.append(s[i])
            else:
                new_s.append(d_c_i[3 - d_c[s[i]] - d_c[s[i + 1]]])
        return triangle(new_s)
    return s[0]