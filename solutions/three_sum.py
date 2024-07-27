"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from collections import Counter
from typing import Iterator


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

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = tuple(nums)
        sums = {}
        results = []
        nums_freq = Counter(nums)

        for pair, freq in self.iter_unique_pairs(nums_freq):
            num_sum = sum(pair)
            sums.setdefault(num_sum, [])
            sums[num_sum].extend(pair for _ in range(freq))

        for num_val, num_freq in nums_freq.items():
            diff = 0 - num_val
            if diff in sums:
                for pair in sums[diff]:
                    trip = sorted(pair + (num_val,))
                    trip_c = Counter(trip)
                    if all(trip_c[n] <= nums_freq[n] for n in trip) and trip not in results:
                        results.append(trip)
        return results
