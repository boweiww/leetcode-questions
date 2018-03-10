class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len (height)
        if length ==1:
            return 0
        mx = 0
        j = length - 1
        i = 0
        while(j > i):
            mx = max(mx, (j - i)* min(height[i],height[j]))
            if (height[i] > height[j]):
                j -= 1
            else:
                i += 1
        return mx