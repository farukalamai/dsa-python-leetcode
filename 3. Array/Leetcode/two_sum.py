class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = list(map(int, nums))
        for index1, value1 in enumerate(nums):
            for index2, value2 in enumerate(nums):
                if (value1 == value2) and (index1 == index2):
                    pass
                else:
                    sum = value1 + value2
                    if sum == target:
                        return list([index1, index2])
