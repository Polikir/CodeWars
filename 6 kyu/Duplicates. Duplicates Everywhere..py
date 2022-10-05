'''

DESCRIPTION:

You are given a table, in which every key is a stringified number, and each corresponding value is an array of characters, e.g.

{
  "1": ["A", "B", "C"],
  "2": ["A", "B", "D", "A"],
}
Create a function that returns a table with the same keys, but each character should appear only once among the value-arrays, e.g.

{
  "1": ["C"],
  "2": ["A", "B", "D"],
}
Rules

Whenever two keys share the same character, they should be compared numerically, and the larger key will keep that character. That's why in the example above the array under the key "2" contains "A" and "B", as 2 > 1.
If duplicate characters are found in the same array, the first occurance should be kept.

'''

def remove_duplicate_ids(dic):
    new_dic = dict({})
    all = set()
    keys = []
    for x in dic:
        for el in dic[x]:
            all.add(el)
        keys.append(x)
    keys = [str(y) for y in sorted([int(x) for x in keys])[::-1]]#sorted(keys)[::-1]

    for key in keys:
        a = dic[key]
        b = []
        for x in a:
            if x in all:
                b.append(x)
                all.remove(x)
        new_dic[key] = ((b))
    return new_dic