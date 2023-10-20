class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i, v1 in enumerate(nums):
            for j, v2 in enumerate(nums):
                if (v1 == v2) and (i == j):
                    pass
                elif (v1 == v2) and (i != j):
                    return True
        
        return False

        