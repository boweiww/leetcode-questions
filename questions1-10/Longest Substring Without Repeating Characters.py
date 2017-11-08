#This method may not pass time test of leetcode I am trying to improve it
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if use method like  chars=[["",0]]*len(s) to make a list of list, all the lists will be connect to each other
        if s =="":
            return 0
        max=0
        i=0
        handle=[]
        while i <len(s):
            if handle !=[]:
                #print handle
                for j in range (len(handle)):
                    #print handle[len(handle)-1]
                    if s[i] in handle[j][0]:
                        if len(handle[j][0])>max:
                            max=len(handle[j][0])
                        handle[j][1]=0
                    else:
                        handle[j][0]+=s[i]

            handle.append([s[i],1])
            for element in handle:
                if element[1]==0:
                    handle.remove(element)
                    

            i+=1
        print handle
        if handle !=[]:
            for i in range (len(handle)):
                if len(handle[i][0]) >max:
                    max = len(handle[i][0])
        return max
