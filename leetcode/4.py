                # Container With Most Water
# ==========================================================
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.


# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         left, right =0,len(height)-1
#         maxi=0

#         for x in range(len(height)):
#             for y in range(x+1,len(height)):
#                 mini= min(height[x],height[y])
#                 res= mini*(y-x)
#                 if res>maxi:
#                     maxi=res
#                     print("operation:",res,x,y)
#         return maxi


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        maxi = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            maxi = max(maxi, area)
            print(height[left] ,height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxi



a=Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))