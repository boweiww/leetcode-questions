import math
# The hint is a little misleading, all negative numbers are not palindromes
# We just return false is a negative number is passed in 
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        biggest=0
        nums=str(x)
        m=len(nums)-1
        if x<0:
            return False
        else:
            new_num=""
        
        while m>=0:
            if nums[m]=="-":
                break
            new_num+=nums[m]
            m=m-1
        n=int(new_num)
        
        if x== n:
            return True
        else:
            return False
            
                
