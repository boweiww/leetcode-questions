'''
Tring to solve this question when I see this problem first time. However usingg dictionary is obviousily easier to write and comprehense.
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

                pre = roman_dict[i]
        return ans