'''
DESCRIPTION:

Longest Palindrome

Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.

Example:

"a" -> 1
"aab" -> 2
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0

'''

def longest_palindrome(s):
    k = 0
    if len(s) == 0:
        return 0
    for x in range(len(s)):
        for y in range(len(s)):
            if x != y:
                if s[min(x, y):max(x, y)] == s[max(x, y):min(x, y):-1] and len(s[min(x, y):max(x, y)]) > k:
                    k = len(s[min(x, y): max(x, y)])
    return k +1
