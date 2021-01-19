#!/bin/python3

class Solution:
    """
    Find the kth largest element in an unsorted array. Note that it is the
    kth largest element in the sorted order, not the kth distinct element.

    """
    def findKthLargest(self, nums, k) -> int:
        nums.sort()
        return nums[len(nums)-k]


sol = Solution()
print(sol.findKthLargest([3, 2, 1, 2, 4, 5, 5, 6], 4))
