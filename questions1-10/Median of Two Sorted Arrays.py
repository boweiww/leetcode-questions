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
        print new
        a=len(new)
        print a
        if a%2==0:
            return ((new[int(round(a/2))]+new[int(round(a/2)-1)])/2.0)
        else:
            return new[int(round(a/2))]