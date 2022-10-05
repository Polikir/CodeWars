'''
DESCRIPTION:

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''


def ay(x):
    if x == '.' or x==',' or x == '!' or x == '?':
        return x
    return x[1:] + x[0] + 'ay'


def pig_it(text):
    text = text.split()
    for i in range(len(text)):
        text[i] = ay(text[i])
    return ' '.join(text)