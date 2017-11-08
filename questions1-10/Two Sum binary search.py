class Solution(object):
    def twoSum(self, nums, target):
        
        
        #:type nums: List[int]
        #:type target: int
        #:rtype: List[int]
        number=nums
        number = nums[:]
        number.sort()
        count=len(number)
        c=count/2
        a=[0,0]
        for j in range (0,count):
            c=self.handle(0,count-1,number,j,target)
            if(  c!=0 and j!=c):
                a=[j,c]
                break
        first=True
        b=[2,9999]
        for i in range (0,count):
            
            if (number[a[0]]==nums[i] and first) :
                b[0]=i
                first=False
            
            elif (number[a[1]]==nums[i]):
                b[1]=i
        return b
            
            
            
    def handle(self,lowbound,upbound,num,cur,target):
        mid=(lowbound+upbound)/2
        if (num[mid]+num[cur]==target):
            return mid
        if ( upbound-lowbound==1):
            if (num[upbound]+num[cur]==target):
                return upbound
            else:
                return 0
        if (num[mid]+num[cur]>target):
            return self.handle(lowbound,mid,num,cur,target)
        
        if (num[mid]+num[cur]<target):
            return self.handle(mid,upbound,num,cur,target)
        if (num[mid]+num[cur]==target):
            return mid