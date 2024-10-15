"""
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
Title: Maximum Length of Repeated Subarray
No: 718
Difficulty: Medium
Category: Algorithms
Problem:
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
 
Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
Explanation: The repeated subarray with maximum length is [0,0,0,0,0].

 
Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100


"""


class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        max_length = 0
        current_length = 0
        for i in range(len(nums1)):
            j = 0
            while j < len(nums2) and nums2[j] != nums1[i]:
                j += 1
            if j < len(nums2):
                k = i
                while k < len(nums1) and j < len(nums2) and nums1[k] == nums2[j]:
                    current_length += 1
                    k += 1
                    j += 1
                if current_length > max_length:
                    max_length = current_length
            else:
                current_length = 0
        return max_length
