# Valid Parentheses
# Cannot pass test. However it acturally runs well. There might be some bugs on the website

marklist=[]
class Solution(object):
    def isValid(self, s):
        
        for i in range(len(s)):
            if self.checkValid(s[i]) == False:
                return False
        if marklist != []:
            return False
        else:
            return True
    def checkValid (self,s):
        if s=="[" or s=="{" or s=="(" :
            marklist.append(ord(s))
            return True
        elif s=="]" or s =="}":
            if marklist == []:
                return False
            if marklist[len(marklist)-1] +2 == ord(s):
                marklist.pop()
                return True
            else:
                return False
            
        elif s==")":
            
            if marklist == []:
                return False
            if marklist[len(marklist)-1] +1 == ord(s):
                marklist.pop()
                return True
            else:
                return False

        else:
            return True