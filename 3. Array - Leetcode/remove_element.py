class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Initialize two pointers, one at the beginning and one at the end of the list.
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == val:
                # If the element at the left pointer is equal to val, swap it with the element at the right pointer.
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                # If the element at the left pointer is not equal to val, move the left pointer to the right.
                left += 1

        # The left pointer now points to the first element equal to val, so the number of elements not equal to val is left.
        return left        

