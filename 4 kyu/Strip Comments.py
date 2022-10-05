'''

DESCRIPTION:

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

'''

def solution(string,markers):
    s_list = string.split("\n")
    n_list = []

    for item in s_list:
        a = ""
        for char in item:
            if char in markers:
                break
            else:
                a = a + char
        n_list.append(a.strip())
    return "\n".join(n_list)