'''

DESCRIPTION:

What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
'''

def anagrams(word, words):
    e = []
    dw = dict()
    for i in word:
        dw[i] = dw.get(i, 0) + 1
    for x in words:
        d1 = dict()
        for t in x:
            d1[t] = d1.get(t, 0) + 1
        if d1 == dw:
            e.append(x)
    return e
