# personal solve, with simple idea and strategy

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
            # if the length of current char is larger than the common prefix, continue to check next.
                if len(public)<=i:
                    continue;
            # if there is any different between the current string and the prefix, cut the prefix, if the lenth of prefix is 0, return "".
                if public[i] != str[i]:
                    public = public[0:i]
                    if i == 0:
                        return ""
        return public
            