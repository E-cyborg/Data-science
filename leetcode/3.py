class Solution(object):
    
    def isMatch(self, s, p):
        if p == s:
            return True
        for x in range(len(p)):
            if p[x] == "*":
                continue
            if p[x] == '.':
                if p[x+1] == '*'or len(p) == 1:
                    return True
            else:
                if p[x] !='*':
                    if x+1 ==len(p):
                        if p[x+1] == '*':
                            continue
                    if p[x] not in s:
                        return False
                    else:
                        return False
                
        return True



z=Solution()
print(z.isMatch(s = "aab", p = "c*a*b"))



# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.

# A -Z            65-90
# a-z             97-122


# . any koi bhi
# * zeros or one char

# .*
# a*
# a*b
# .a