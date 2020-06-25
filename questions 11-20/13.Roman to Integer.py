'''
Tring to solve this question when I see this problem first time. However usingg dictionary is obviousily easier to write and comprehense.
This one is pretty similar to question 12, Use dictionary or tuple list can solve it easily. 
A little bit different between this one and the 12 is that you need to solve the cases like IV IX, that means you need to hold the previous char.
that means we cannot simply use only one directoty to solve that. However we can still use subscract to do that, that saves memory.
'''

class Solution(object):
    def romanToInt(self, s):

        ans = 0  # answer(int)
        pre = 0  # the previous number
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in s:
            if i in roman_dict:
                ans += roman_dict[i]

                if roman_dict[i] > pre:
                    ans -= 2 * pre
					'''
					substract double pre e.g:CM=M-C, we added c before hence ans+= (M-C)-C
					'''
                pre = roman_dict[i]
        return ans

