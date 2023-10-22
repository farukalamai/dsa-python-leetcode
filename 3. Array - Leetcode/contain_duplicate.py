

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        original_length = len(nums)
        nums_set_length = len(set(nums)) 
        if original_length == nums_set_length:
            return False
        else:
            return True