class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        j=0
        i=0
        n=len(nums2)
        m=len(nums1)
        new=[]
        while i< m:
            if  j>=n:
                #It strange to append a string here, but in python 2, always have string > integer 
                nums2.append("")
            if nums1[i]<nums2[j]:
                new.append(nums1[i])
                i+=1
            else:
                new.append(nums2[j])
                j+=1
        while j<n:
            new.append(nums2[j])
            j+=1
        a=len(new)
        if a%2==0:
            return (new[int(round(a/2))]+new[int(round(a/2)-1)])/2.0
        else:
            #a/2 will return a int that rounds down (in float like 1.0), so no need to -1 here
            #if use a/2.0 we should -1 after transfer to int
            return new[int(round(a/2))]
            