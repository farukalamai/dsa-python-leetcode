class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """     
        nums = list(map(int, nums))


        for i in range(0, len(nums)+1):
            if i in nums:
                pass
            else:
                return i