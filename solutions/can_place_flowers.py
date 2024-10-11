"""
https://leetcode.com/problems/can-place-flowers/
Title: Can Place Flowers
No: 605
Difficulty: Easy
Category: Algorithms
Problem:
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
 
Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

 
Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length


"""
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], flowers: int) -> bool:
        i = 0
        while i < len(flowerbed) and flowers > 0:
            if i == 0:
                rng = flowerbed[i: i + 2]
            elif i == len(flowerbed) - 1:
                rng = flowerbed[i - 1 : i + 1]
            else:
                rng = flowerbed[i - 1 : i + 2]
            if all(spot == 0 for spot in rng):
                flowerbed[i] = 1
                flowers -= 1
                i += 2
            else:
                i += 1

        return flowers == 0

