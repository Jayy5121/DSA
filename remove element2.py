#27. Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        i=0
        while i<len(nums):
            if nums[i]==val:
                nums.pop(i)
            else:
                i+=1
        print(len(nums),nums)
        return len(nums),nums
s1=Solution()
nums=[0,1,2,2,3,0,4,2]
val=2
s1.removeElement(nums,val)

        