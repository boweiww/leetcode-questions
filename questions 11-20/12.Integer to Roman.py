class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # indicates all the represents and special cases, then process it.
        # Remember that the python dictionary has no sequence, so you cannot use dictionary to do this.
        characters = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
        ]

        result = ""

        for roman, integer in characters:
            while num >= integer:
                num -= integer
                result += roman

        return result