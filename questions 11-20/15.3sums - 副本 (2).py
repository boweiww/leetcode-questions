#believe it could work
#not work for over time limit

class Solution(object):
    global  merge
    global mergesort
    def threeSum(self, nums):
        
        sort=mergesort(nums)
        print(sort);
        cur=-1
        zeros=[]
        result=[]
        send=-1
        bend=-1
        bresult=[]
        for i in range(len(sort)):
            if sort[i] ==0:
                zeros.append(0)
        if len(zeros)>=3:
            result.append([0,0,0])
        for i in range(len(sort)):
            if sort[i] >=0:
                send=i
                break
        
        for i in range(len(sort)-1,0,-1):
            if sort[i] <=0:
                bend=i
                break
        print send
        print bend
        if send>bend:
            bend =send
        for i in range(send):
            for j in range (i+1,send):
                for k in range (bend,len(sort)):
                    if sort[i]+sort[j]+sort[k] ==0:
                        bresult.append([sort[i],sort[j],sort[k]])
                        

        for i in range(send):
            for j in range (bend,len(sort)):
                for k in range (j+1,len(sort)):
                    if sort[i]+sort[j]+sort[k] ==0:
                        bresult.append([sort[i],sort[j],sort[k]])
        for i in range (len(bresult)):
            exist =False
            for j in range (len(result)):
                if bresult[i] == result[j]:
                    exist =True
            if exist==False:
                result.append (bresult[i])
        return result
                
        
def merge(a,b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

# Code for merge sort

def mergesort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)/2
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a,b)
        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        