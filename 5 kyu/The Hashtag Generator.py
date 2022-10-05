'''
DESCRIPTION:

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
'''


def generate_hashtag(s):
    l = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    u = list('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')
    l1 = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    u1 = list('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
    dal1 = dict(zip(l1,u1))
    al = zip(l, u)
    dal = dict(al)
    lin = s.split()
    if ''.join(lin) == '':
        return(False)
    else:
        for i in range(len(lin)):
            lin[i] = list(lin[i])
            lin[i][0] = dal[lin[i][0]]
            for t in range(1, len(lin[i])):
                lin[i][t] = dal1[lin[i][t]]
            lin[i] = ''.join(lin[i])
        lin = ''.join(lin)
        if len(lin) > 140:
            return(False)
        else:
            return('#' + lin)