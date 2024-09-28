"""
https://leetcode.com/problems/find-pairs-with-a-certain-sum/
Title: Finding Pairs With a Certain Sum
No: 1865
Difficulty: Medium
Category: Algorithms
Problem:
You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:

Add a positive integer to an element of a given index in the array nums2.
Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 <= i < nums1.length and 0 <= j < nums2.length).

Implement the FindSumPairs class:

FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object with two integer arrays nums1 and nums2.
void add(int index, int val) Adds val to nums2[index], i.e., apply nums2[index] += val.
int count(int tot) Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.


Example 1:

Input
["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
Output
[null, 8, null, 2, 1, null, null, 11]

Explanation
FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
findSumPairs.count(7);  // return 8; pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
findSumPairs.add(3, 2); // now nums2 = [1,4,5,4,5,4]
findSumPairs.count(8);  // return 2; pairs (5,2), (5,4) make 3 + 5
findSumPairs.count(4);  // return 1; pair (5,0) makes 3 + 1
findSumPairs.add(0, 1); // now nums2 = [2,4,5,4,5,4]
findSumPairs.add(1, 1); // now nums2 = [2,5,5,4,5,4]
findSumPairs.count(7);  // return 11; pairs (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) make 2 + 5 and pairs (5,3), (5,5) make 3 + 4


Constraints:

1 <= nums1.length <= 1000
1 <= nums2.length <= 105
1 <= nums1[i] <= 109
1 <= nums2[i] <= 105
0 <= index < nums2.length
1 <= val <= 105
1 <= tot <= 109
At most 1000 calls are made to add and count each.


"""

from collections import Counter
from typing import List
import numpy as np


class FindSumPairs(object):
    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self._nums2 = np.array(nums2, dtype=int)
        self._nums1_freq_map = Counter(nums1)
        self._nums2_freq_map = Counter(nums2)

    @property
    def nums2(self):
        return self._nums2

    @property
    def nums1_freq_map(self):
        return self._nums1_freq_map

    @property
    def nums2_freq_map(self):
        return self._nums2_freq_map

    def add(self, index: int, val: int):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        old_val = self._nums2[index]
        new_val = old_val + val
        self._nums2[index] = new_val
        if new_val in self._nums2_freq_map:
            self._nums2_freq_map[new_val] += 1
        else:
            self._nums2_freq_map[new_val] = 1
        self._nums2_freq_map[old_val] -= 1

    def filter_frequency_map(self, freq_map: dict, tot: int):
        return {k: v for k, v in freq_map.items() if v <= tot}

    def count(self, tot: int) -> int:
        """
        :type tot: int
        :rtype: int
        """

        counter = 0
        filtered_map1 = self.filter_frequency_map(self.nums1_freq_map, tot)
        filtered_map2 = self.filter_frequency_map(self.nums2_freq_map, tot)
        smallest_map, largest_map = (
            (
                filtered_map1
                if len(filtered_map1) <= len(filtered_map2)
                else filtered_map2
            ),
            (
                filtered_map2
                if len(filtered_map1) <= len(filtered_map2)
                else filtered_map1
            ),
        )
        for n1, n1_freq in smallest_map.items():
            diff = tot - n1
            if diff in largest_map:
                n2_freq = largest_map[diff]
                counter += n1_freq * n2_freq
        return counter
