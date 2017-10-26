class Solution(object):
    def twoSum(self, nums, target):
        
        
        #:type nums: List[int]
        #:type target: int
        #:rtype: List[int]
        
        count=len(nums)
        
        for i in range (0,count):
            for j in range (0,count):
                if(i==j):
                    continue
                if (nums[i]+ nums[j] == target):
                    return [i,j]
        
