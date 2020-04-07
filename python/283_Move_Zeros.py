# https://leetcode.com/problems/move-zeroes/
from typing import List

class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     for _ in range(nums.count(0)):
    #         nums.remove(0)
    #         nums.append(0)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        nums[:] = [i for i in nums if i != 0]
        nums.extend([0]*zero_count)

if __name__ == '__main__':
    s = Solution()