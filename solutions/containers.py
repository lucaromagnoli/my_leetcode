"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""

class Solution:

    def maxArea(self, height: list[int]) -> int:
        max_area = None
        for l_idx in range(len(height)):
            r_idx = len(height) - 1
            if height[l_idx] < min(height[l_idx], height[r_idx]):
                continue
            while l_idx < r_idx:
                l_val, r_val = height[l_idx], height[r_idx]
                area = (r_idx - l_idx) * min(l_val, r_val)
                if max_area is None or area > max_area:
                    max_area = area
                r_idx -= 1
        return max_area or 0
