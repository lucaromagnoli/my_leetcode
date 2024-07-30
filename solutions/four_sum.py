"""
https://leetcode.com/problems/4sum/
Title: 4Sum
No: 18
Difficulty: Medium
Category: Algorithms
Problem:
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

from collections import Counter
from typing import Iterator


class Solution:
    def iter_unique_pairs(self, nums_freq: Counter) -> Iterator[list[int]]:
        seen = set()
        for i_val, i_frq in nums_freq.items():
            for j_val, j_frq in nums_freq.items():
                if not (i_val == j_val and i_frq == j_frq == 1):
                    pair = (i_val, j_val) if i_val <= j_val else (j_val, i_val)
                    if pair not in seen:
                        seen.add(pair)
                        freq = i_frq - 1 if i_val == j_val else i_frq * j_frq
                        yield pair, freq

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums = tuple(nums)
        sums = {}
        results = []
        nums_freq = Counter(nums)

        for pair, freq in self.iter_unique_pairs(nums_freq):
            num_sum = sum(pair)
            sums.setdefault(num_sum, [])
            sums[num_sum].extend(pair for _ in range(freq))

        for pair, freq in self.iter_unique_pairs(nums_freq):
            num_sum = sum(pair)
            num_diff = target - num_sum
            if num_diff in sums:
                for other_pair in sums[num_diff]:
                    quad = sorted([*pair, *other_pair])
                    quad_counter = Counter(quad)
                    if (
                        all(quad_counter[n] <= nums_freq[n] for n in quad_counter)
                        and quad not in results
                    ):
                        results.append(quad)
        return sorted(results)
