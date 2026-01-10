# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

 
class Solution(object):
    def myAtoi(self, s):
        res= []
        st=0
        for x in s:
            if s[st]== " ":
                st+=1
            else:
                break
        print(st)
        if st < len(s) and (s[st] == '-' or s[st] == '+'):
            res.append(s[st])
            st+=1
        if not s[st].isdigit():
            return 0
        
        while st < len(s) and s[st] == "0":
            st += 1



        for x in s[st:]:
            if not x.isdigit(): 
                if len(res)<=1:
                    return 0
                break
            else:
                res.append(x)
        
        num = int("".join(res))

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num



a=Solution()
print(a.myAtoi("-91283472332"))

        

#  not working go check a video on yt