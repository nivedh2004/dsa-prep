# 88. Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements
# that should be merged, and the last n elements are set to 0 and should be ignored.
# nums2 has a length of n.
#
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
#
# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
#
# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
#
# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_index_num1 = m + n - 1
        i = m - 1
        j = n - 1

        # Merge from the end of both arrays
        while i != -1 and j != -1:
            if nums1[i] > nums2[j]:
                nums1[last_index_num1] = nums1[i]
                i -= 1
            else:
                nums1[last_index_num1] = nums2[j]
                j -= 1
            last_index_num1 -= 1

        # Copy any remaining elements from nums2
        while j >= 0:
            nums1[last_index_num1] = nums2[j]
            last_index_num1 -= 1
            j -= 1

        print("nums after merging is:", nums1)


# Example test runs
if __name__ == "__main__":
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    s.merge(nums1, 3, nums2, 3)

    nums1 = [1]
    nums2 = []
    s.merge(nums1, 1, nums2, 0)

    nums1 = [0]
    nums2 = [1]
    s.merge(nums1, 0, nums2, 1)
