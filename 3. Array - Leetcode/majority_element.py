class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        
        # Count the occurrences of each element in the array
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Find the element with the maximum count
        majority = max(count, key=count.get)
        
        return majority


