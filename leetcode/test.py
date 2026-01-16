class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        clo = 0
        for x in nums:
            # print(x,target,x-target)
            if 0<(x-target)<clo or 0<(x+target)<clo:
                clo=x
        return clo
    


kk=Solution()
print(kk.threeSumClosest([-1,2,1,-4],1))