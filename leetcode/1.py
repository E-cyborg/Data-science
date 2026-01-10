# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# class Solution(object):
#     def convert(self, s, numRows):
#         a=[]
#         x= (2*numRows)-2
#         curr=0
#         a.append(s[0])
#         z=1
#         for i in range(len(s)):
#             curr=curr+x
#             if curr >= len(s):
#                 print(f"curr: {curr}, len: {len(s)}")
#                 # curr=curr-len(s)
#                 curr=z
#                 z=+1
                


#             a.append(s[curr])
#             # curr+=1
#             print(f"x={x}, cur = {curr},a= {a}")






class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        a = [""] * numRows   # each index is a row
        curr = 0             # current row
        direction = 1        # 1 = down, -1 = up

        for i in range(len(s)):
            a[curr] += s[i]

            # change direction at boundaries
            if curr == 0:
                direction = 1
            elif curr == numRows - 1:
                direction = -1

            curr += direction
            print(f"i={i}, cur = {curr},a= {a}")
        return "".join(a)


a=Solution()
print(a.convert("PAYPALISHIRING",3))

    # P A H N A P L S I I G Y I R
# p cur =0     x=