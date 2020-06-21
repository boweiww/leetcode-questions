class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # print strs;
        if strs == []:
            return ""
        public = strs[0];

        for str in strs:    
            public = public[0:len(str)];
            for i in range(0, len(str)):
               # print(len(public));
                if len(public)<=i:
                    continue;
                    
                if public[i] != str[i]:
                    public = public[0:i]
                    if i == 0:
                        return ""
        return public
            