class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        strings = [str(integer) for integer in digits]
        a_string = "".join(strings)
        an_integer = int(a_string) + 1

        digits = [int(i) for i in str(an_integer)]

        return digits

        