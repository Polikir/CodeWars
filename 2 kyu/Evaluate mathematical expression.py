'''

Instructions

Given a mathematical expression as a string you must return the result as a number.

Numbers

Number may be both whole numbers and/or decimal numbers. The same goes for the returned result.

Operators

You need to support the following mathematical operators:

Multiplication *
Division / (as floating point division)
Addition +
Subtraction -
Operators are always evaluated from left-to-right, and * and / must be evaluated before + and -.

Parentheses

You need to support multiple levels of nested parentheses, ex. (2 / (2 + 3.33) * 4) - -6

Whitespace

There may or may not be whitespace between numbers and operators.

An addition to this rule is that the minus sign (-) used for negating numbers and parentheses will never be separated by whitespace. I.e all of the following are valid expressions.

1-1    // 0
1 -1   // 0
1- 1   // 0
1 - 1  // 0
1- -1  // 2
1 - -1 // 2
1--1   // 2

6 + -(4)   // 2
6 + -( -4) // 10
And the following are invalid expressions

1 - - 1    // Invalid
1- - 1     // Invalid
6 + - (4)  // Invalid
6 + -(- 4) // Invalid
Validation

You do not need to worry about validation - you will only receive valid mathematical expressions following the above rules.

Restricted APIs

NOTE: eval and exec are disallowed in your solution.
'''

def mult(a, b):
    return a * b


def divis(a, b):
    return a / b


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def separation(line):
    dig = '0123456789.'
    operat = dict({'*': mult, '/': divis, '+': plus, '-': minus})
    i = 0
    components = []
    start = []
    lb = dict({})
    rb = dict({})
    while i < len(line):
        if line[i] == ' ':
            i += 1
            continue
        elif line[i] in dig:
            j = 0
            while (i + j < len(line) and line[i + j] in dig):
                j += 1
            components.append(float(line[i:i + j]))
            i += (j)
        else:
            if line[i] == '(':
                start.append(len(components))
            if line[i] == ')':
                x = len(components)
                lb[x] = start.pop()
                rb[lb[x]] = x
            components.append(line[i])
            i += 1

    return components, lb, rb


def calc(line):
    dig = '0123456789.'
    operat = dict({'*': mult, '/': divis, '+': plus, '-': minus})
    components, lb, rb = separation(line)

    def muldiv(components):
        val, oper = 1, '*'
        for comp in components:
            if isinstance(comp, float):
                val = operat[oper](val, comp)
            else:
                oper = comp
        return val

    def calc_pod(st_ind, end_ind):

        ind = st_ind
        no_bac_comp = []

        while ind <= end_ind:
            if components[ind] == '(':

                val = calc_pod(ind + 1, rb[ind] - 1)



                no_bac_comp.append(val)
                ind = rb[ind]
            else:
                no_bac_comp.append(components[ind])
            ind += 1

        ind = 0
        no_neg_comp = []

        while ind < len(no_bac_comp):
            if no_bac_comp[ind] != '-':
                no_neg_comp.append(no_bac_comp[ind])


            else:
                if ind > 0 and type(no_bac_comp[ind-1]) == float:
                    no_neg_comp.append('-')

                else:
                    j = ind
                    while not isinstance(no_bac_comp[ind],float) :
                        ind += 1

                    n_neg = ind - j

                    val = no_bac_comp[ind] * ((-1) ** (n_neg % 2))
                    no_neg_comp.append(val)

            ind += 1
        ind_sub = [-1]
        for ind, comp in enumerate(no_neg_comp):
            if comp == '+' or comp == '-':
                ind_sub.append(ind)
        val, oper = 0, '+'

        for i in range(1, len(ind_sub)):
            j, k = ind_sub[i - 1], ind_sub[i]
            val1 = muldiv(no_neg_comp[j + 1 : k])
            val = operat[oper](val, val1)
            oper = no_neg_comp[k]

        val = operat[oper](val, muldiv(no_neg_comp[ind_sub[-1] + 1:]))

        return val

    return calc_pod(0, len(components) - 1)



